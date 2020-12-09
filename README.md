# Wmt2Ics

## Description

Using Web Schedules (wmtscheduler or wmt) **Views: My Schedule** as data, highlight and copy the pay period schedule and paste this data into **Terminal** window to be parsed and processed into a Internet Calendar Sharing file (.ics) which can then be imported into Apple iCal, Google Calendar, etc. 

## Information

Built and tested in Python 3.8

This module takes advantage of python library [icalendar](https://pypi.org/project/icalendar/) which is a [RFC5545](https://www.ietf.org/rfc/rfc5545.txt) parser/generator for iCalendar files.

### Use Case 1

1.  Create a python file:

```python3
from wmt2ics import Wmt2Ics as wmt

wmt() # Default run_method='desktop'
```
2. Save the file and **make it executable**.
3. Navigate to [Web Scheduler](https://wmtscheduler.faa.gov/WMT_LogOn/), once logged in, select **Views**, then **My Schedule**.
4. Copy the the pay period by highlighting and ```Ctrl+c``` to copy.
5. Go to **Terminal** and run python3 yourfile.py
   * Enter the pay period number - This will be part of your saved .ics file
   * Next, paste shift data - if you are in linux, you'll have to press ```Shift+Ctrl+v``` to paste in **terminal window**
6. Once completed you should find "Pay_Period_XX.ics" on your desktop. If you are using a Mac, you can open your iCal program and import the file.
   * You can also import to Google Calendar
   * If you have a linux computer, or windows computer, but use an iPhone, I suggest **Use Case #2**

### Use Case 2 (Sligtly more involved)

1.  Create a python file:

```python3
from wmt2ics import Wmt2Ics as wmt
from wmt2ics.configemail import ConfigEmail as cfg

config = cfg()

config.setup_config(smtp='smtp.gmail.com', port='587', send='sender@email.com', 'send_pwd='P@$$w0rd for sendemail accout', dest='receiver@email.com')

wmt(run_method='email') # will now send email with attachment
```
 
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

Once you run ConfigEmail().setup_config(**kwargs) once, you can comment it out, it will create a json file, if you ever need to change it, you can re-run this method
