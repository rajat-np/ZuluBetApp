import fileinput
from datetime import date, timedelta
from back import dscrape, opendata
from tkinter import *
from tkinter import ttk
from tkinter.tix import *
import os
import csv
root = Tk()
v  = IntVar()
r1 = ttk.Radiobutton(root, text="Offline", variable=v, value=0)
r1.grid(row = 0 , column = 0)

r2 = ttk.Radiobutton(root, text="Online", variable=v, value=1)
r2.grid(row = 0 , column = 1)

dtF = Label(root, text = "From Date:", padx = 10, pady= 10)
dtF.grid(row = 1, column = 0,sticky="E")
entdF = Entry(root, bg="white",highlightthickness=2)
entdF.grid(row = 1 , column = 1)


dtT = Label(root, text = "To Date:",padx = 10, pady= 10)
dtT.grid(row = 2 , column = 0,sticky="E")
entdT = Entry(root,highlightthickness=2)
entdT.grid(row = 2 , column = 1)


de = Label(root, text = "Edge:", padx = 10, pady= 10)
de.grid(row = 3 , column = 0,sticky="E")
ente = Entry(root,highlightthickness=2)
ente.grid(row = 3 , column = 1)


df = Label(root, text = "HOME/DRAW/AWAY/\nALL/1X/X2/12:", padx = 10, pady= 10)
df.grid(row = 4 , column = 0,sticky="E")
entw = Entry(root,highlightthickness=2)
entw.grid(row = 4 , column = 1)

dfU = Label(root, text = "FAV/NA/DOG:", padx = 10, pady= 10)
dfU.grid(row = 5 , column = 0,sticky="E")
entFU = Entry(root,highlightthickness=2)
entFU.grid(row = 5 , column = 1)


dfLOW = Label(root, text = "LOW:", padx = 10, pady= 10)
dfLOW.grid(row = 6 , column = 0,sticky="E")
entLOW = Entry(root,highlightthickness=2)
entLOW.grid(row = 6 , column = 1)

dfHIGH = Label(root, text = "HIGH:", padx = 10, pady= 10)
dfHIGH.grid(row = 7 , column = 0,sticky="E")
entHIGH = Entry(root,highlightthickness=2)
entHIGH.grid(row = 7 , column = 1)


bt2 = ttk.Button(root, text = "Exit",command = lambda : sys.exit())
bt2.grid(row = 8 , column = 1)

bt1 = ttk.Button(root, text = "Proceed", command = lambda : trans())
bt1.grid(row = 8 , column = 0)

#---------------------------------------------------------------------------------------------------------------=======


def backend():
	fm  = open("mini.txt", "w")
	of=v.get()
	date1=str(entdF.get()).strip().split("-")
	date2=str(entdT.get()).strip().split("-")
	edg=float(ente.get())
	h=str(entw.get())
	fod=str(entFU.get())
	od1 = float(entLOW.get())
	od2  = float(entHIGH.get())

	d1 = date(int(date1[2]), int(date1[1]), int(date1[0]))  # start date
	d2 = date(int(date2[2]), int(date2[1]), int(date2[0]))
	f1=open("temp.csv",'w')
	f1.close()
	with open('temp2.csv', 'w') as csvfile:
	        sw = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
	        sw.writerow([
	            'ID',
	            'Match_name',
	            'Date_Time',
	            'Prediction_1',
	            'Prediction_X',
	            'Prediction_2',
	            'Average_1',
	            'Average_X',
	            'Average_2',
	            'Final_Result',
	            'Value_1',
	            'Value_X',
	            'Value_2',
	            'Probability_1',
	            'Probability_X',
	            'Probability_2',
	            'Edge_1',
	            'Edge_X',
	            'Edge_2',
	            ])
	delta = d2 - d1         # timedelta
	sum1=[0,0]
	if (v.get()==1):
		print("online")
		for i in range(delta.days + 1):
			j=str(d1 + timedelta(days=i))
			dat=j.split("-")
			date1=str(dat[2]+'-'+dat[1]+'-'+dat[0])
			dscrape(date1)
			su=opendata(date1, edg, h, fod, od1, od2)
			sum1[0]=sum1[0]+su[0]
			sum1[1]=sum1[1]+su[1]
	else:
		print("offline")
		for i in range(delta.days + 1):
			j=str(d1 + timedelta(days=i))
			dat=j.split("-")
			date1=str(dat[2]+'-'+dat[1]+'-'+dat[0])
			try:
				su=opendata(date1, edg, h, fod, od1, od2)
				sum1[0]=sum1[0]+su[0]
				sum1[1]=sum1[1]+su[1]
			except:
				print(date1, " not in Database")
			
	f=open("temp.csv",'r')
	read = csv.reader(f,delimiter = ",")
	total=0
	for i in read:
		total=total+1
	print("total winnings = ", str(sum1[1])[0:5], file = fm)
	print("total bets = ", sum1[0], file = fm)
	print("net winnings = ", str(sum1[1]-sum1[0])[0:5], file = fm)

def trans():
	root1 = Tk()
	ll2 = Label(root1, text = "Choose Option")
	ll2.pack()
	b1 = ttk.Button(root1, text = "DataBase(CSV)", width = 20, command = lambda : openCSV())
	b1.pack()
	b1 = ttk.Button(root1, text = "Result",  width = 20, command = lambda : openResult())
	b1.pack()
	b2 = ttk.Button(root1, text = "MiniResult",  width = 20, command = lambda: openminiResult())
	b2.pack()
	b6 = ttk.Button(root1, text = "Close",  width = 10, command = lambda :root1.destroy())
	b6.pack(side  = "bottom")
	root1.geometry("250x180+805+230")
	root1.title("ZuluBet")
	print(v.get())
	backend()
	root1.mainloop()
def openCSV():
	rootn = Tk()
	swin = ScrolledWindow(rootn)
	swin.pack()
	win = swin.window

	with open("temp2.csv", newline = "") as file:
		reader = csv.reader(file)
		r = 0
		for col in reader:
			c = 0
			for row in col:
				if c == 1:
					label = tkinter.Label(win, width = 40, height = 1, text = row)
					label.grid(row = r, column = c)
				else:
					label = tkinter.Label(win, width = 14, height = 1, text = row)
					label.grid(row = r, column = c)

				c += 1
			r += 1

	rootn.geometry("800x600+20+20")
	rootn.title("ZuluBet")
	rootn.mainloop()
def openResult():
	t=0
	
	rootn = Tk()
	swin = ScrolledWindow(rootn)
	swin.pack()
	win = swin.window

	with open("temp.csv", newline = "") as file:
		reader = csv.reader(file)
		r = 0
		for col in reader:
			c = 0
			for row in col:
				if c == 0:
					label = tkinter.Label(win, width = 40, height = 1, text = row)
					label.grid(row = r, column = c)
				else:
					label = tkinter.Label(win, width = 14, height = 1, text = row)
					label.grid(row = r, column = c)
				
				c += 1
			r += 1
	#rootn.geometry("800x600+20+20")
	rootn.title("ZuluBet")
	rootn.mainloop()
def openminiResult():
	i = 0
	rootn = Tk()
	fm = open("mini.txt", "r")
	lines = fm.readlines()
	for line in lines:
		label = tkinter.Label(rootn , text = line.strip() ,padx = 80, pady  = 15)
		label.grid(row = i, column = 0)
		i+=1
	#rootn.geometry("275x150+500+230")
	rootn.title("ZuluBet")
	bw6 = ttk.Button(rootn, text = "Close",  width = 10, command = lambda :rootn.destroy())
	bw6.grid(row = i+1 )
	rootn.mainloop()



root.geometry("320x350+500+230")
root.title("ZuluBet")
root.mainloop()


