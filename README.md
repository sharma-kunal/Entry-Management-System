# Entry Management Software

An Entry Management System using Django (A Python-based free and open-source web framework) 

In this project you have a management software which will take details from the visitor and when the user `Check's In`, it will inform the host about the meeting (vai Mail and SMS) with all details of the Visitor. 
And when the Visitor `Check's Out` it will inform the Visitor (via Mail and SMS) all details about all the information about the meeting attended.

## Preview

1. First Page will ask the user if he/she want to `Check In` or `Check Out`.

![Index Page](https://github.com/sharma-kunal/internship_project/blob/master/readme_data/Index.png)


2. Now let us suppose you are the Visitor and you want to attend a meeting with all details as follows:
* Visitor's Name: ABC
* Visitor's Phone No: 0000000000 (standard Indian Phone No.)
* Visitor's Email Id: abc@gmail.com
* Host Name: XYZ
* Host Phone No: 1234567890 (standard Indian Phone No.)
* Host Email Id: xyz@gmail.com

![CheckIn](https://github.com/sharma-kunal/internship_project/blob/master/readme_data/CheckIn.png)

When you click the `Check In` button, the server will automatically generate a Mail and SMS to the host, informing him/her about the details of the Visitor with their `Check In Time`.

3. Now let us suppose the meeting is over and you want to Check Out. So you just select Check Out option from the Home menu and enter your Phone No. which you used while Checking In. 
   And the server will automatically generate a Mail and SMS and send it to the Visitor with all details with their Check Out Time
   
![Check Out](https://github.com/sharma-kunal/internship_project/blob/master/readme_data/CheckOut.png)

## Requirements

* You will need to provide the server with a Mail Id and Password with which it would send E-Mails.

You can do so by going to the file `Mail.py` and providing with the `SENDER_EMAIL` and `PASSWORD`

```
forms/Mail.py
```

![SENDER_EMAIL and PASSWORD](https://github.com/sharma-kunal/internship_project/blob/master/readme_data/Mail.png)

* You also need to make an ID on the website [way2sms](https://www.way2sms.com/), and copy the `API_KEY` and `Secret_key` from the API section [API](https://www.way2sms.com/userApi) of the website which we will use to send SMS.

* Now Paste the API_KEY and SECRET_KEY in the file `views.py`

```
forms/views.py
```

![API_KEY](https://github.com/sharma-kunal/internship_project/blob/master/readme_data/api_key.png)


## Running

* Run the command 

```
pip3 install -r requirements.txt
```

to install all the required dependencies.

* Now run the command 

```
python3 manage.py runserver
```

to run the Django server on your localhost.

Sometimes an error may be raised, specifying that the port is already in use. So, don't worry just run the command

```
python3 manage.py runserver 127.0.0.1:8090
```

Changing the `8090` with any port number until the error is gone and the server is up and running.

If the browser does not open automatically then,

* Open your favourite browser and type

```
127.0.0.1/<port number you specified above>(by default 8000)
```

Congratulations, the code is up and running
