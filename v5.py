import tkinter as tk
import sqlite3
import time

class NewUserProfile(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('400x275')
        self.title('New User Profile')
        tk.Label(self,text='Pay No.:').grid(column=0,row=0)
        self.pay = tk.Entry(self)
        self.pay.grid(column=1,row=0,sticky='nw')
        tk.Label(self, text="Rank:").grid(column=0,row=1)
        self.variableRank = tk.StringVar(self)
        self.variableRank.set("Station Officer")
        self.rank = tk.OptionMenu(self,self.variableRank,"Station Officer","Sub Officer","Leading Firefighter","Leading Firefighter(D)","Firefighter","Firefighter(D)")
        self.rank.grid(column=1,row=1,sticky='nw')
        tk.Label(self, text="Act Up:").grid(column=0,row=3)
        self.variableAct = tk.StringVar(self)
        self.variableAct.set("No")
        self.act = tk.OptionMenu(self,self.variableAct,"Yes","No")
        self.act.grid(column=1,row=3,sticky='nw')
        tk.Label(self,text='Name:').grid(column=0,row=4)
        self.name = tk.Entry(self)
        self.name.grid(column=1,row=4,sticky='n')
        tk.Label(self,text="Station:").grid(row=5,column=0)
        self.station = tk.Entry(self)
        self.station.grid(column=1,row=5)
        tk.Label(self,text="Skills:").grid(column=0,row=6)
        self.skills = tk.Entry(self)
        self.skills.grid(column=1,row=6)
        tk.Label(self,text='Watch:').grid(column=0,row=7)
        self.variableWatch = tk.StringVar(self)
        self.variableWatch.set('Blue')
        self.watch = tk.OptionMenu(self,self.variableWatch,'Blue','Green','Red','White','Multi')
        self.watch.grid(column=1,row=7,sticky='nw')
        tk.Label(self,text='Preference:').grid(column=0,row=8)
        self.variablePref = tk.StringVar(self)
        self.variablePref.set('None')
        self.pref = tk.OptionMenu(self,self.variablePref,"None",'Night Shifts','Day Shifts')
        self.pref.grid(column=1,row=8,sticky='nw')
        tk.Label(self,text='Contact:').grid(column=0,row=9)
        self.number = tk.Entry(self)
        self.number.grid(column=1,row=9)
        tk.Button(self, text='Submit', command=self.addToDB).grid(column=2, row=9, sticky='s')

    def addToDB(self):
        self.conn = sqlite3.connect('overtimeTEST.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from overtime")
        results = self.cursor.fetchall()
        self.cursor.execute(""" INSERT INTO overtime VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """,
        (len(results)+1,
        str(self.pay.get()).upper(),
        str(self.variableRank.get()),
        str(self.variableAct.get()),
        str(self.name.get()),
        str(self.station.get()),
        str(self.skills.get()),
        str(self.variableWatch.get()),
        str(self.variablePref.get()),
        str(self.number.get()),
        'No',
        'No',
        'No',
        'No',
        'No',
        'No',
        'No',
        'No'))
        self.conn.commit()
        self.SuccessWindow()

    def SuccessWindow(self,):
        self.window = tk.Tk.__init__(self)
        self.window.geometry('100x100')
        self.window.title('Success')
        tk.Label(self.window,text='Completed Successfully.').grid(column=0,row=0,sticky='n')
        tk.Button(self,text='Close',command=self.window.destroy).grid(column=0,row=1,sticky='n')

class NewAvailability(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('New Availability Form')
        tk.Label(self,text='New Availability Form').grid(column=1,row=0,sticky='n')
        tk.Label(self,text='Pay No.:').grid(column=0,row=1)
        self.pay = tk.Entry(self)
        self.pay.grid(column=1,row=1,sticky='e')
        tk.Label(self,text='Night 1').grid(column=0,row=2)
        tk.Label(self,text='Day 2').grid(column=0,row=3)
        tk.Label(self,text='Night 2').grid(column=0,row=4)
        tk.Label(self,text='Day 3').grid(column=0,row=5)
        tk.Label(self,text='Night 3').grid(column=0,row=6)
        tk.Label(self,text='Day 4').grid(column=0,row=7)
        self.variableNightOne = tk.StringVar(self)
        self.variableNightOne.set('No')
        self.nightOne = tk.OptionMenu(self,self.variableNightOne,'Yes','No')
        self.nightOne.grid(column=1,row=2,sticky='w')
        self.variableDayTwo = tk.StringVar(self)
        self.variableDayTwo.set('No')
        self.DayTwo = tk.OptionMenu(self,self.variableDayTwo,'Yes','No')
        self.DayTwo.grid(column=1,row=3,sticky='w')
        self.variableNightTwo = tk.StringVar(self)
        self.variableNightTwo.set('No')
        self.NightTwo = tk.OptionMenu(self,self.variableNightTwo,'Yes','No')
        self.NightTwo.grid(column=1,row=4,sticky='w')
        self.variableDayThree = tk.StringVar(self)
        self.variableDayThree.set('No')
        self.DayThree = tk.OptionMenu(self,self.variableDayThree,'Yes','No')
        self.DayThree.grid(column=1,row=5,sticky='w')
        self.variableNightThree = tk.StringVar(self)
        self.variableNightThree.set('No')
        self.NightThree = tk.OptionMenu(self,self.variableNightThree,'Yes','No')
        self.NightThree.grid(column=1,row=6,sticky='w')
        self.variableDayFour = tk.StringVar(self)
        self.variableDayFour.set('No')
        self.DayFour = tk.OptionMenu(self,self.variableDayFour,'Yes','No')
        self.DayFour.grid(column=1,row=7,sticky='w')

        tk.Button(self,text='Submit',command=self.submitForm).grid(column=2,row=8,sticky='e')

    def submitForm(self):
        self.conn = sqlite3.connect('overtimeTEST.db')
        self.cursor = self.conn.cursor()
        payNumPlace = str(self.pay.get()).upper()

        idNum = self.cursor.execute("""SELECT id FROM overtime WHERE paynum=?""", (payNumPlace,))
        for row in idNum:
            idNum = row
        self.cursor.execute(""" UPDATE overtime SET nightOne = ?, dayTwo = ?, nightTwo = ?, dayThree = ?, nightThree = ?, dayFour = ? WHERE id=? """,
                            (str(self.variableNightOne.get()),
                            str(self.variableDayTwo.get()),
                            str(self.variableNightTwo.get()),
                            str(self.variableDayThree.get()),
                            str(self.variableNightThree.get()),
                            str(self.variableDayFour.get()),
                            int(idNum[0])))
        self.conn.commit()

class EditUser(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Edit User')
        tk.Label(self,text='Pay No.:').grid(column=0,row=0)
        self.pay = tk.Entry(self)
        self.pay.grid(column=1,row=0,sticky='nw')
        tk.Label(self, text="Rank:").grid(column=0,row=1)
        self.variableRank = tk.StringVar(self)
        self.variableRank.set("Station Officer")
        self.rank = tk.OptionMenu(self,self.variableRank,"Station Officer","Sub Officer","Leading Firefighter","Leading Firefighter(D)","Firefighter","Firefighter(D)")
        self.rank.grid(column=1,row=1,sticky='nw')
        tk.Label(self, text="Act Up:").grid(column=0,row=3)
        self.variableAct = tk.StringVar(self)
        self.variableAct.set("No")
        self.act = tk.OptionMenu(self,self.variableAct,"Yes","No")
        self.act.grid(column=1,row=3,sticky='nw')
        tk.Label(self,text='Name:').grid(column=0,row=4)
        self.name = tk.Entry(self)
        self.name.grid(column=1,row=4,sticky='n')
        tk.Label(self,text="Station:").grid(row=5,column=0)
        self.station = tk.Entry(self)
        self.station.grid(column=1,row=5)
        tk.Label(self,text="Skills:").grid(column=0,row=6)
        self.skills = tk.Entry(self)
        self.skills.grid(column=1,row=6)
        tk.Label(self,text='Watch:').grid(column=0,row=7)
        self.variableWatch = tk.StringVar(self)
        self.variableWatch.set('Blue')
        self.watch = tk.OptionMenu(self,self.variableWatch,'Blue','Green','Red','White','Multi')
        self.watch.grid(column=1,row=7,sticky='nw')
        tk.Label(self,text='Preference:').grid(column=0,row=8)
        self.variablePref = tk.StringVar(self)
        self.variablePref.set('None')
        self.pref = tk.OptionMenu(self,self.variablePref,"None",'Night Shifts','Day Shifts')
        self.pref.grid(column=1,row=8,sticky='nw')
        tk.Label(self,text='Contact:').grid(column=0,row=9)
        self.number = tk.Entry(self)
        self.number.grid(column=1,row=9)
        tk.Button(self, text='Submit', command=self.editDB).grid(column=2, row=9, sticky='s')

    def editDB(self):
        self.conn = sqlite3.connect('overtimeTEST.db')
        self.cursor = self.conn.cursor()
        payNumPlace = str(self.pay.get()).upper()
        idNum = self.cursor.execute("""SELECT id FROM overtime WHERE paynum=?""", (payNumPlace,))
        for row in idNum:
            idNum = row
        self.cursor.execute(""" UPDATE overtime SET rank=?,actup=?,name=?,station=?,skills=?,watch=?,pref=?,number=?
        WHERE id=? """, (str(self.variableRank.get()),
                         str(self.variableAct.get()),
                         str(self.name.get()),
                         str(self.station.get()),
                         str(self.skills.get()),
                         str(self.variableWatch.get()),
                         str(self.variablePref.get()),
                         str(self.number.get()),
                         int(idNum[0])))
        self.conn.commit()

class ViewShifts(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('550x50')
        self.title('Pay Number')
        tk.Label(self,text='Pay Number:').grid(column=0,row=0,sticky='w')
        self.payNo = tk.Entry(self)
        self.payNo.grid(column=1,row=0,sticky='e')
        tk.Button(self,text='Submit',command=self.ShowShifts).grid(column=2,row=0,sticky='e')

    def ShowShifts(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('View Shifts')
        self.conn = sqlite3.connect('overtimeTEST.db')
        self.cursor = self.conn.cursor()
        payNumPlace = str(self.payNo.get()).upper()
        self.shiftsGet = self.cursor.execute(""" SELECT nightOne, dayTwo, nightTwo, dayThree, nightThree, dayFour FROM overtime WHERE paynum=?""", (str(payNumPlace),))
        for i in self.shiftsGet:
            self.shiftsGet = i
        tk.Label(self,text='Shifts:').grid(column=0,row=0,sticky='n')
        tk.Label(self,text='Night One: ').grid(column=0,row=1,sticky='w')
        tk.Label(self,text=str(self.shiftsGet[0]).strip("(,')")).grid(column=1,row=1,sticky='e')
        tk.Label(self,text='Day Two: ').grid(column=0,row=2,sticky='w')
        tk.Label(self,text=str(self.shiftsGet[1]).strip("(,')")).grid(column=1,row=2,sticky='e')
        tk.Label(self,text='Night Two: ').grid(column=0,row=3,sticky='w')
        tk.Label(self,text=str(self.shiftsGet[2]).strip("(',)")).grid(column=1,row=3,sticky='e')
        tk.Label(self,text='Day Three: ').grid(column=0,row=4,sticky='w')
        tk.Label(self,text=str(self.shiftsGet[3]).strip("(,')")).grid(column=1,row=4,sticky='e')
        tk.Label(self,text='Night Three:').grid(column=0,row=5,sticky='w')
        tk.Label(self,text=str(self.shiftsGet[4]).strip("(',)")).grid(column=1,row=5,sticky='e')
        tk.Label(self,text='Day Four: ').grid(column=0,row=6,sticky='w')
        tk.Label(self,text=str(self.shiftsGet[5]).strip("(',)")).grid(column=1,row=6,sticky='e')

class Menu(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Main Menu')
        tk.Button(self,text='New Availability',command=self.openAvailability).grid(column=0,row=0,sticky='w')
        tk.Button(self,text='Edit Availability',command=self.plainFun).grid(column=0,row=1,sticky='w')
        tk.Button(self,text='New User',command=self.openUser).grid(column=0,row=2,sticky='w')
        tk.Button(self,text='Edit User',command=self.openEdit).grid(column=0,row=3,sticky='w')
        tk.Button(self,text='View Shifts',command=self.openShifts).grid(column=0,row=4,sticky='w')

    def openAvailability(self):
        NewAvailability()

    def openUser(self):
        NewUserProfile()

    def openEdit(self):
        EditUser()

    def openShifts(self):
        ViewShifts()

    def plainFun(self):
        print('No Use')

Menu()

