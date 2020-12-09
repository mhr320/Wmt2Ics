from wmt2ics.sendemail import SendEmail
from wmt2ics.configemail import ConfigEmail
from datetime import datetime, timedelta
from icalendar import Calendar, Event
import os
import csv

class Wmt2Ics:
    '''Converts wmtscheduler.faa.gov Views:My Schedule to ics file'''
   
    def __init__(self, run_method='desktop'):
        self.run_method = run_method
        self.basepath = os.path.dirname(__file__)
        self.config_file = os.path.abspath(os.path.join(self.basepath,"wmtconfig.json"))
        self.cats_file = os.path.abspath(os.path.join(self.basepath,"shift_cats.data"))
        self.save_as = os.path.abspath(os.path.join(self.basepath,"Pay_Period_"))
        self.eval_run_method()

    def eval_run_method(self):
        '''Determines where file is saved: desktop or attached to email'''
        if self.run_method == "desktop":
            self.desktop = os.path.expanduser("~/Desktop")
            self.save_as = os.path.abspath(os.path.join(self.desktop,"Pay_Period_"))
            self.obtainData()
            self.buildShiftCats()
            self.addNewCategory()
            self.createCalendar()
        elif self.run_method == "email":
            ConfigEmail().get_config()
            self.obtainData()
            self.buildShiftCats()
            self.addNewCategory()
            self.createCalendar()
            SendEmail(self.pay_period, self.outfile).send_mail()
            self.removeFile()

    def obtainData(self):
        '''Terminal Interface for naming Pay Period and pasting schedule data'''
        self.schedule = []
        self.pay_period = input("ENTER PAY PERIOD -> ")
        print("PASTE SCHEDULE")
        while True:
            self.schedule.append(input())
            if len(self.schedule) == 42:
                break
        self.shifts = self.schedule[2::3]
        self.dates = self.schedule[1::3]

    def buildShiftCats(self):
        '''Assigns shift_cats.data to shift_cats{}'''
        with open(self.cats_file, 'r') as f:
            self.reader = csv.reader(f)
            self.shift_cats = {row[0]:(row[1], int(row[2]), row[3],) for row in self.reader}

    def addNewCategory(self):
        '''If shift in pasted schedule does not have an entry in shift_cats{}, add'''
        for shift in self.shifts:
            if shift not in self.shift_cats:
                self.time = input(shift + " Not found. Enter Start Time (format: 00:00:00) -> ")
                self.length = input("Enter Shift Length in Hours -> ")
                self.shift_name = input("Display Name for Calendar -> ")
                self.new_category = [shift, self.time, self.length, self.shift_name]
                with open(self.cats_file, "a+", newline='') as f:
                    self.csv_writer = csv.writer(f)
                    self.csv_writer.writerow(self.new_category)
                self.shift_cats.clear()
                self.buildShiftCats()

    def createCalendar(self):
        '''icalendar method to parse schedule into ics file'''
        self.ical = []
        self.events =[]
        self.outfile = self.save_as+self.pay_period+".ics"
        for i in range(len(self.shifts)):
            if self.shifts[i] in self.shift_cats.keys():
                self.name = self.shift_cats[self.shifts[i]][2]
                self.date_time = self.dates[i] + " " + self.shift_cats[self.shifts[i]][0]
                self.date_time = datetime.strptime(self.date_time, "%m/%d/%Y %H:%M:%S")
                self.time = self.shift_cats[self.shifts[i]][0]
                self.hours = self.shift_cats[self.shifts[i]][1]
                self.ical.append((self.name, self.date_time, self.hours))
        for x, i in enumerate(self.ical):
            event = Event()
            if i[0] == "RDO":
                event.add("summary", i[0])
                event.add("description", "ZOB")
                event.add("dtstamp", i[1])
                event.add("dtstart", i[1].date())
                event.add("dtend", i[1].date())
                self.events.append(event)
            else:
                event.add("summary", i[0])
                event.add("description", "ZOB")
                event.add("dtstamp", i[1])
                event.add("dtstart", i[1])
                event.add("dtend", i[1] + timedelta(hours=i[2]))
                self.events.append(event)
        self.cal = Calendar()
        self.cal.add('prodid', '-//Michael H. Roberts//WMT TO ICS//')
        self.cal.add('version', '2.0')
        self.cal.add('calscale', 'GREGORIAN')
        for evnt in self.events:
            self.cal.add_component(evnt)
        with open(self.outfile, 'wb') as f:
            f.write(self.cal.to_ical())

    def removeFile(self):
        if os.path.exists(self.outfile):
            os.remove(self.outfile)

if __name__ == '__main__':
    Wmt2Ics()