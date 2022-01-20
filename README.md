# Wmt2Ics

## Description

Using Web Schedules (wmtscheduler or wmt) **Views: My Schedule** as data, highlight and copy the pay period schedule. Once you start the script, enter the pay period number, the module will then automagically paste the copied data (you will not see anything on the terminal window). The information will then be parsed and converted into an **I**nternet **C**alendar **S**haring file (.ics) which can then be imported into Apple iCal, Google Calendar, etc. 

## Information

Built and tested in Python 3.8

This module takes advantage of python library [icalendar](https://pypi.org/project/icalendar/) which is a [RFC5545](https://www.ietf.org/rfc/rfc5545.txt) parser/generator for iCalendar files. It also uses pyperclip to paste the copied data.

### Use Case 1

1.  Create a python file:

```python3
#!/usr/bin/env python3
from wmt2ics import Wmt2Ics as wmt

wmt() # Default run_method='desktop'
```
2. Save the file and **make it executable**.
3. Navigate to [Web Scheduler](https://wmtscheduler.faa.gov/WMT_LogOn/), once logged in, select **Views**, then **My Schedule**.
4. Copy the the pay period by highlighting and ```Ctrl+c``` to copy.
5. Go to **Terminal** and run ```python3 yourfile.py```
   * Enter the pay period number - This will be part of your saved .ics filename
6. Once completed you should find "Pay_Period_XX.ics" on your desktop. If you are using a Mac, you can open your iCal program and import the file.
   * You can also import to Google Calendar
   * If you have a linux computer, or windows computer, but use an iPhone, I suggest **Use Case #2**

### Use Case 2 (Sligtly more involved)

1.  Create a python file:

```python3
#!/usr/bin/env python3
from wmt2ics import Wmt2Ics as wmt
from wmt2ics.configemail import ConfigEmail as cfg

config = cfg() 

config.setup_config(smtp='smtp.gmail.com', port='587', send='sender@email.com', 'send_pwd='P@$$w0rd for sendemail accout', dest='receiver@email.com')

wmt(run_method='email') # will now send email with attachment
```
#### Special Note 1:
* If you omit:
```python
from wmt2ics.configemail import ConfigEmail as cfg
config = cfg()
config.setup_config(**kwargs)
```
and simply run 
```python
wmt(run_method='email')
```

the terminal interface will ask you for smtp,port,send,send_pwd,dest. However there are no checks and no history and no way to change what you entered in the terminal, so you will have to run

```python
from wmt2ics.configemail import ConfigEmail as cfg
config = cfg()
config.setup_config(**kwargs)
```
to overwrite the file.

#### Special Note 2:

kwargs in setup_config have defaults set:

* send='smtp.gmail.com'
* port='587'
* send_pwd = ''

If you do not include these in the setup_config(\*\*kwargs) and only include 

```python
config.setup_config(send='', dest='')
```

The library will set send='smtp.gmail.com' and port='587' which are gmail settings
If you leave send_pwd blank, the library will search for an env variable on your local system named GMAIL_APP_PWD. If you know how to set a persistant env variable on your local machine, this may save you some typing and be slightly more secure. Otherwise, worry not and set send_pwd = 'yourpassword' 

**'smtp.gmail.com'**
The SMTP server for the email account used to send the .ics file

**'587'**
The port number for the SMTP server, here, i've placed the port for gmail's smtp

**'sender@email.com'**
Here I use a gmail address to send the email, I created this email 
account specifically to use as a sender email for this script. You may use whatever you 
wish.

**'password'**
Gmail supports "app passwords", this is where you will place the app password.
if you would rather be slightly more secretive about this, if you leave it blank, the 
method will attempt to use an environment variable named 'GMAIL_APP_PWD' which you will
have to set on your local machine. I set mine in /etc/environment, you'll have to research
how to do so on Google for Windows and Mac.

**'receiver@email.com'**
Where you want it to go!

So all that being said, you'll need to get an app password for an email account or use an account that allows using just your sign in password.

Once you run ConfigEmail().setup_config(\*\*kwargs) once, you can comment it out, it will create a json file, if you ever need to change it, you can re-run this method

## Test Web Page

a test webpage is available to download [Web Test Page](https://github.com/mhr320/wmtTestPage.git)
