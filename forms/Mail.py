import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = 'kuunaalsharma88@gmail.com'
PASSWORD = '9639522583'


# Mail(visitor_name, visitor_phone, visitor_email, checkin, checkOut, host_name, host_phone, host_email)
class Mail:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

        self.send_mail()

    def send_mail(self):
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        if self.checkout == "":
            # send message to host
            msg['Subject'] = 'Visitor\'s Details for the Meeting'
            msg['To'] = self.host_email
            text = MIMEText(self.host_message())
            msg.attach(text)
        else:
            # send message to visitor
            msg['Subject'] = 'Details regarding the meeting ' + self.visitor_name
            msg['To'] = self.visitor_email
            text = MIMEText(self.visitor_message())
            msg.attach(text)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(SENDER_EMAIL, PASSWORD)
        print("logged In")
        print("Sending mail to:" + msg['To'])
        s.sendmail(SENDER_EMAIL, msg['To'], msg.as_string())
        print("Mail Sent")
        s.quit()

    def host_message(self):
        msg = "Visitor's Name:\t" + self.visitor_name + "\nVisitor's Phone No:\t" + self.visitor_number \
            + "\nVisitor's Email:\t" + self.visitor_email + "\nVisitor's CheckIn Time:\t" + str(self.checkin)
        print(msg)
        return msg

    def visitor_message(self):
        msg = "Name:\t" + self.visitor_name + "\nPhone No:\t" + str(self.visitor_number) + "\nCheckIn Time:\t" \
            + str(self.checkin) + "\nCheckOut Time:\t" + str(self.checkout) + "\nHost Name:\t" + self.host_name
        print(msg)
        return msg