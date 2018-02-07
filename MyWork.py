# import time
# import datetime
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter
import calendar
import datetime

class simpleapp_tk(tkinter.Tk):

    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self._count=0
        self._total = 31
        self.selectedDay = ''
        self.selectedMonth = ''
        self._monthList = {
            "January":1,
            "February":2,
            "March": 3,
            "April": 4,
            "May": 5,
            "june": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "Novermber": 11,
            "December": 12,

        }
        self.initialize()

    def initialize(self):
        self.grid()

        labelEntry0 = tkinter.Label(self,anchor="w",fg="black",bg="white", text="Please enter the first day of your last period.")
        labelEntry0.grid(column=0,row=0,columnspan=2,sticky='EW',pady=10, padx=10)


        labelEntry1 = tkinter.Label(self,text="Enter Day:")
        labelEntry1.grid(column=0, row=1)

        self.entry1 = tkinter.Listbox(self, selectmode="SINGLE", height=1)
        self.entry1.grid(column=1, row=1, sticky='EW')
        self.entry1.bind('<<ListboxSelect>>', self.onSelectDay)

        labelEntry2 = tkinter.Label(self, text="Enter Month:")
        labelEntry2.grid(column=0, row=2)

        self.entry2 = tkinter.Listbox(self,selectmode="SINGLE",height=1)
        for key, value in self._monthList.items():
            self.entry2.insert(value, key)
            # print(key, value)

        self.entry2.grid(column=1, row=2, sticky='EW')
        self.entry2.bind('<<ListboxSelect>>', self.onSelectMonth)

        labelEntry3 = tkinter.Label(self, text="Enter Year:")
        labelEntry3.grid(column=0, row=3)
        self.entry3 = tkinter.Entry(self)
        self.entry3.grid(column=1, row=3, sticky='EW')

        labelEntry4 = tkinter.Label(self, text="Enter Menstrual range:")
        labelEntry4.grid(column=0, row=4)
        v = tkinter.StringVar()
        v.set("28")
        self.entry4 = tkinter.Entry(self, textvariable=v)
        self.entry4.grid(column=1, row=4, sticky='EW')

        button = tkinter.Button(self,text=u"Calculate",
                                command=self.OnButtonClick)
        button.grid(column=0,row=5,columnspan=2,sticky='EW',pady=10, padx=5)

    # result
        self.message = tkinter.StringVar()
        label = tkinter.Label(self,
                              anchor="w",fg="black",bg="white", textvariable=self.message)
        label.grid(column=0,row=6,columnspan=2,sticky='EW',padx=10,pady=10)

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

    def onSelectDay(self, evt):
        _self  = evt.widget
        if self.selectedDay == '':
            self.selectedDay = _self.curselection()

    def onSelectMonth(self, evt):
        _self = evt.widget
        if self.selectedMonth == '':
            self.selectedMonth = _self.curselection()

    def OnButtonClick(self):
        if self.selectedDay:
            if self.selectedMonth:
                if self.entry3.get():
                    periodCycleDays = int(self.entry4.get()) | 28;
                    fertilePhaseStart = periodCycleDays - 20;
                    fertilePhaseEnd = periodCycleDays - 11;
                    ovulation = (fertilePhaseStart - 1) + (fertilePhaseEnd - fertilePhaseStart) / 2;
                    userinputTime = datetime.date(int(self.entry3.get()), self.entry1.get(self.selectedMonth), self.entry1.get(self.selectedDay))
                    curdateTime = datetime.datetime.now().ctime()
                    # display message here
                    periodCalendar = calendar.month(int(self.entry3.get()), self.entry1.get(self.selectedMonth), self.entry1.get(self.selectedDay))
                    self.message.set(periodCalendar)
                else:
                    self.message.set('Year field is required!!')
            else:
                self.message.set('Please select Month!!')
        else:
            self.message.set('Please select Day!!')

    def generateListDay(self):
        if self._count < self._total:
            self._count = self._count + 1
            self.entry1.insert(self._count, self._count)
            self.after(10, self.generateListDay)


    def OnPressEnter(self,event):
        print ("You pressed enter !")

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.generateListDay()
    app.mainloop()

# mydate = datetime.date(2017, 12, 21)  # year, month, day
# print(mydate.strftime("%A"))
 # print (calendar.calendar (2025))
# yy = 2017 # year

# mm = 12 # month
#dd = 1
# print(calendar.month (yy, mm))


#Ask the user for the details (mm, yy)
# yy = int(input("Enter year: "))
# mm = int(input ("Enter Month: "))
# dd = int(input ("Enter day: "))

# display the calendar
# print (calendar.month(yy,mm))

#mycalendar = calendar(2017, 12, 21)
#print(mycalendar.strftime("%A"))
