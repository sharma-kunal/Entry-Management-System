from django.shortcuts import render
from django.contrib import messages
import time
from .Mail import Mail
from .form import RawForm, CheckOutForm
from .models import Data
import requests

# Create your views here.
PHONE_REGEX = r'\(?\d+\)?[-.\s]?\d+[-.\s]?\d+'
EMAIL_REGEX = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
URL = 'https://www.way2sms.com/api/v1/sendCampaign'
API_KEY = 'PHD345XPDWZNLAUWGMHR5RHCH8V6JHUU'
SECRET_KEY = '6DUTC15GBBRI2SMJ'
ADMIN_NUMBER = '8279718127'


def index(request):
    return render(request, 'index.html')


def checkIn(request):
    form = RawForm()
    success = False
    if request.method == 'POST':
        form = RawForm(request.POST)
        if form.is_valid():
            visitor_name = form['visitor_name'].value()
            visitor_number = form['visitor_number'].value()
            visitor_email = form['visitor_email'].value()
            host_name = form['host_name'].value()
            host_number = form['host_number'].value()
            host_email = form['host_email'].value()
            data = Data.objects.all()
            for d in data:
                if d.visitor_number == visitor_number or d.visitor_email == visitor_email:
                    messages.error(request, 'User with same details has already Checked In')
                    break
            else:
                curr_time = time.asctime(time.localtime(time.time()))
                data = Data(visitor_name=visitor_name, visitor_number=visitor_number, visitor_email=visitor_email,
                            curr_time=curr_time, host_name=host_name, host_number=host_number,
                            host_email=host_email)
                try:
                    Mail(visitor_name=visitor_name, visitor_number=visitor_number, visitor_email=visitor_email,
                         checkin=curr_time, checkout="", host_name=host_name, host_number=host_number, host_email=host_email)
                    # Send Message
                    print("Sending Message to Host")
                    response = send_message(host_number, visitor_name, visitor_number, visitor_email, curr_time, "", host_name,
                                            host_number, host_email)
                    print(response)
                    data.save()
                    success = True
                except:
                    messages.error(request, "Please try again later")
    else:
        form = RawForm()
    context = {
        'form': form,
        'success': success
    }
    return render(request, "checkin.html", context)


def checkOut(request):
    msg = ""
    form = CheckOutForm()
    if request.method == 'POST':
        form = CheckOutForm(request.POST)
        if form.is_valid():
            number = form['number'].value()
            data = Data.objects.all()
            for d in data:
                if d.visitor_number == number:
                    msg = "Checked Out Successfully"
                    checkout = time.asctime(time.localtime(time.time()))
                    Mail(visitor_name=d.visitor_name, visitor_number=d.visitor_number, visitor_email=d.visitor_email,
                         checkin=d.curr_time, checkout=checkout,
                         host_name=d.host_name, host_number=d.host_number, host_email=d.host_email)
                    print("Sending Message to visitor")
                    response = send_message(d.visitor_number, d.visitor_name, d.visitor_number, d.visitor_email,
                                            d.curr_time, checkout, d.host_name, d.host_number, d.host_email)
                    print("Message sent to visitor")
                    d.delete()
                    break
            else:
                messages.error(request, "Please make sure you entered the same Phone No. that you used while Checking In")
    context = {
        'form': form,
        'msg': msg
    }
    return render(request, 'checkout.html', context)


def send_message(send_to, visitor_name, visitor_number, visitor_email, checkin, checkout, host_name, host_number, host_email):
    req_params = {
        'apikey': API_KEY,
        'secret': SECRET_KEY,
        'usetype': 'stage',
        'phone': send_to,
        'message': host_message(visitor_name, visitor_number, visitor_email, checkin) if not checkout else visitor_message(
            visitor_name, visitor_number, checkin, checkout, host_name),
        'senderid': ADMIN_NUMBER
    }
    return requests.post(URL, req_params)


def host_message(visitor_name, visitor_number, visitor_email, checkin):
    msg = "Visitor's Name:\t" + visitor_name + "\nVisitor's Phone No:\t" + visitor_number \
        + "\nVisitor's Email:\t" + visitor_email + "\nVisitor's CheckIn Time:\t" + str(checkin) + " (UTC)"
    print(msg)
    return msg


def visitor_message(visitor_name, visitor_number, checkin, checkout, host_name):
    msg = "Name:\t" + visitor_name + "\nPhone No:\t" + str(visitor_number) + "\nCheckIn Time:\t" \
        + str(checkin) + " (UTC)" + "\nCheckOut Time:\t" + str(checkout) + "\nHost Name:\t" + host_name
    print(msg)
    return msg
