# Friendship App...
# Group-18...
# AU-2140043 Bhavya Khakhar...
# AU-2140215 Zenil Sanghvi...
# AU-2140203 Malay Patel...

import pandas as pd
import numpy as np
import openpyxl
from pandas import Series,DataFrame
import xlrd
from openpyxl import Workbook, load_workbook
from matplotlib import pyplot as plt
from datetime import datetime
import os

magenta = '\033[35m'
black = '\033[30m'
white = '\033[37m'
red = '\033[31m'
yellow = '\033[33m'
blue = '\033[34m'
green = '\033[32m'
cyan = '\033[36m'

def mainmenu():
  print(magenta +"            🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
  print("            🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰",yellow + "WELCOME TO FRIENDSHIP APP" ,magenta +"🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
  print(magenta +"           🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
  print(magenta +"           🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰",red+ "Tell Us About Yourself",magenta + "🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
  print(magenta +"           🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
  print()
  print()
  print(green +"*******************************************************************************")
  print(blue +"  \t\t\t\t 1). ADMIN \t\t\t\t")
  print(blue +"  \t\t\t\t 2). CUSTOMER \t\t\t\t")
  print(blue +"  \t\t\t\t 3). EXIT \t\t\t\t" )
  print(blue +"  \t\t\t\t 4). ABOUT APP \t\t\t\t")
  print(green +"*******************************************************************************")
  print(white)
  choice = int(input("\t\t\t\t Enter your choice here: "))
  print(green +" -----------------------------------------------------------------------------------")
  print()
  while (True):
    if choice==1:
      os.system('cls')
      admin()
      print()
      break
    elif choice==2:
      os.system('cls')
      mainmenu2()
      print()
      break
    elif choice==3:
      os.system('cls')
      print(" \t\t\t\t Goodbye \t\t\t\t ")
      print(" \t\t\t\t Please Visit Again \t\t\t\t")
      break
    elif choice==4:
      os.system('cls')
      print('''In these trying times of the pandemic, we have truly grown socially distant, with limited outings and decreasing opportunities to meet new people, attend events and congregations, the average person's social, personal and emotional life has taken a hit. Matchmaking apps can perfectly bridge this gap, by providing a safe and convenient platform for like-minded people to meet and/or get to know each other, helping in returning to the relatively fulfilling life of the pre covid era. In our matchmaking app, our very first step is to check your personality with the 23 questions we have designed to give you a perfect match who is like you. You can find friends who is like you from the filters in our app. Hope it would help you to find some new good friend which would be the part of your life for long time.''')
      print()
      mainmenu()
      break
    else:
      print(" 🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
      print("\t\t\t\t!!WARNING!!\t\t\t\t")
      print("\t\t\t\tEnter a valid choice.\t\t\t\t")
      print(" 🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
      
      mainmenu()
      break

def admin():
  while(True):
    adminname=str(input("\t\t\t\t Enter Username: "))
    print()
    adminpw=str(input("\t\t\t\t Enter Password: "))
    print()
    adminname1= "zenil"
    adminpw1="zenil@123"
    os.system('cls')
    if (adminname==adminname1) and (adminpw==adminpw1):
      print(magenta +"                      🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
      print(yellow +"                       -----------------------------  Welcome Back Admin ! ------------------------------ ")
      print(magenta +"                      🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
      print(red +"                      ---------------------------------  Admin Menu ! ---------------------------------- ")
      print(magenta +"                      🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
      adminmenu()
      break
    else:
      print(red +" 🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
      print(" 🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰!! WARNING !!🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰 ")
      print(" 🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
      print(" 🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰Invalid Username or Password🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
      print(" 🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰")
      print()
      print(white)
      print("\t\t\t\t 1).Main Menu")
      print("\t\t\t\t 2).Admin login")
      print()
      x=int(input("\t\t\t\t Enter your choice here: "))
      print()
      if x==1:
        mainmenu()
        break
      elif x==2:
        admin()
        break
      else:
        print("\t\t\t\t Enter a valid choice")
        break
      print(white)

def adminmenu():
  print(cyan)
  print(" *******************************************************************************")
  print(" \t\t\t 1). View Customer's List. ")
  print(" \t\t\t 2). Questions asked to the customers. ")
  print(" \t\t\t 3). Gender Data. ")
  print(" \t\t\t 4). Return to Main menu. ")
  print(" *******************************************************************************")
  print(green)
  choice1 = int(input("\t\t\t\t Enter your choice here: "))
  print(white)
  while True:
    if choice1==1:
      os.system('cls')
      customerview()
      break
    elif choice1==2:
      os.system('cls')
      print()
      questions()
      break
    elif choice1==3:
      os.system('cls')
      print()
      mfmembers()
      break
    elif choice1==4:
      os.system('cls')
      mainmenu()
      break 
    else:
      print()
      print("\t\t\t\t Enter a valid choice")
      adminmenu()  

def customerview():
  data = pd.read_csv('dating.txt', sep=',')
  print(data)
  print()
  y=input("Enter b or B to go to adminmenu: ")
  if y=='b' or y=='B':
    print()
    os.system("cls")
    adminmenu()

def removecustomer():
  fh_r= open("dating.txt","r")
  fh_w= open("temp.txt","w")

  uname=int(input("Enter the User_ID of the customer that is to be removed...: "))
  while(True):
    s=fh_r.readline(uname)
    L=s.split("~")
    if len(s)>0:
      if L[0]!=uname:
        fh_w.write(s)
  
  fh_w.close()
  fh_w.close()
  old_name='temp.txt'
  new_name='dating.txt'
  os.remove(old_name)
  os.rename(old_name,new_name)

def questions():

  q1=" 1).Do you regularly make new friends "               
  q2=" 2).Do you spend your free time exploring various random topics that pique your interest?"
  q3=" 3).How often you have a backup plan for a backup plan?"        
  q4=" 4).How usually you stay calm under a lot of pressure?"
  q5=" 5).Do you prefer starting another work before completing the previous one?"
  q6=" 6).Are you very sentimental?"          
  q7=" 7).Do you maintain your personal diary. writing, at the end of the day about the events happend during that day?"
  q8=" 8).Do you use organizing tools like schedules and lists?"
  q9=" 9).Even a small mistake can cause you to doubt your overall abilities and knowledge?"
  q10=" 10).Would you like to go on a long walf with a music turned on, when u are upset about something?"
  q11=" 11).How often you start the converstion when you meet someone?"
  q12=" 12).How more inclined you are to follow your heart than your head?"
  q13=" 13).Do you like going to brunch?"
  q14=" 14).Do you worry about whether you made a good impression on people you meet?"
  q15=" 15).Do you avoid leadership roles during group activities?"
  q16=" 16).How often do you get angry?"
  q17=" 17).How often do you go to parties with friends?"
  q18=" 18).Would you like to have a pet?"
  q19=" 19).Which animal would you prefer to have it as a pet?"
  q20=" 20).How often do you keep promises?"
  q21=" 21).How often do you accept hard challenges?"
  q22=" 22).How often do you go on holiday trips?"
  q23=" 23).Do you like to have a healthy argument-good fight?"

  print(cyan)
  print("\t\t\t    1). See all the questions asked to the customers: ")
  print() 
  print("\t\t\t    2). A Specific Question asked to a customer that is to be seen: ")
  print()
  print("\t\t\t    3). Return to main menu: ")
  print()
  
  queans=int(input("\t\t\t Enter a choice: "))
  print()
  
  if queans==1:
    print(blue)
    print('''

  
  1). Do you regularly make new friends
      1.Yes,Very often
      2.Sometimes
      3.Very Rarely

  2). Do you spend your free time exploring various random topics that pique your interest?
      1.Almost all time
      2.Around half of the time
      3.Very rarely

  3). How often you have a backup plan for a backup plan?
      1.Yes,Very often
      2.Sometimes
      3.Very Rarely

  4). How usually you stay calm under a lot of pressure?
      1.Yes,Very often
      2.Sometimes
      3.Very Rarely 

  5). Do you prefer starting another work before completing the previous one?
      1.Yes,Very often
      2.Sometimes
      3.Very Rarely

  6). Are you very sentimental?
      1.Very sentimental
      2.Not much sentimental
      3.Not at all sentimental

  7). Do you maintain your personal diary. writing, at the end of the day about the events happend during that day?
      1.Yes, i write daily
      2.Yes,sometimes
      3.I don't maintain a diary

  8). Do you use organizing tools like schedules and lists?
      1.Yes
      2.No

  9). Even a small mistake can cause you to doubt your overall abilities and knowledge?
      1.Strongly agree
      2.Agree
      3.Disagree
      4.Strongly disagree

  10). Would you like to go on a long walf with a music turned on, when u are upset about something?
       1.Yes, it heals me
       2.It diverts my mind for sometime
       3.It doesn't helps me

  11). How often you start the converstion when you meet someone?
       1.Yes,Very often
       2.Sometimes
       3.Very Rarely

  12). How more inclined you are to follow your heart than your head?
       1.Yes,Very often
       2.Sometimes
       3.Very Rarely

  13). Do you like going to brunch?
       1.Yes,Very often
       2.Sometimes
       3.Very Rarely
    
  14). Do you worry about whether you made a good impression on people you meet?
       1.Yes,Very often
       2.Sometimes
       3.Very Rarely

  15). Do you avoid leadership roles during group activities?
       1.Strongly agree
       2.Agree
       3.Disagree
       4.Strongly disagree
    
  16). How often do you get angry
       1.Even small things make me angry
       2.Some particular things make me angry
       3.I am a cool head type

  17). How often do you go to parties with friends?
       1.Yes,Very often
       2.Sometimes
       3.Very Rarely

  18). Would you like to have a pet?
      1.I already have it
       2.Looking forward to own it
       3.I don't like to have pets

  19). Which animal would you prefer to have it as a pet?
      1.Dog
      2.Cat
      3.Some other animal
      4.I don't like to have pets

  20). How often do you keep promises?
       1.Yes,Very often
       2.Sometimes
       3.Very Rarely 
      
  21). How often do you accept hard challenges?
       1.Yes,Very often
       2.Sometimes
       3.Very Rarely

  22). How often do you go on holiday trips?
       1.Yes,Very often
       2.Sometimes
       3.Very Rarely

  23). Do you like to have a healthy argument-good fight?
       1.Yes i like to argue
       2.I don't argue much
		
        
''')
    print(cyan)
    print("---------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------What to do next ?---------------------------------------------")
    print("---------------------------------------------------------------------------------------------------------")
    print()
    questions()


  elif queans==2:
    print(green)
    x=int(input("\t\t\t Enter the question number which you want to see: "))
    print()
    if x==1:
      print("\t\t\t",q1)
      print()
    elif x==2:
      print("\t\t\t",q2)
      print()
    elif x==3:
      print("\t\t\t",q3)
      print()
    elif x==4:
      print("\t\t\t",q4)
      print()
    elif x==5:
      print("\t\t\t",q5)
      print()
    elif x==6:
      print("\t\t\t",q6)
      print()
    elif x==7:
      print("\t\t\t",q7)
      print()
    elif x==8:
      print("\t\t\t",q8)
      print()
    elif x==9:
      print("\t\t\t",q9)
      print()
    elif x==10:
      print("\t\t\t",q10)
      print()
    elif x==11:
      print("\t\t\t",q11)
      print()
    elif x==12:
      print("\t\t\t",q12)
      print()
    elif x==13:
      print("\t\t\t",q13)
      print()
    elif x==14:
      print("\t\t\t",q14)
      print()
    elif x==15:
      print("\t\t\t",q15)
      print()
    elif x==16:
      print("\t\t\t",q16)
      print()
    elif x==17:
      print("\t\t\t",q17)
      print()
    elif x==18:
      print("\t\t\t",q18)
      print()
    elif x==19:
      print("\t\t\t",q19)
      print()
    elif x==20:
      print("\t\t\t",q20)
      print()
    elif x==21:
      print("\t\t\t",q21)
      print()
    elif x==22:
      print("\t\t\t",q22)
      print()
    elif x==23:
      print("\t\t\t",q23)
      print()
    else:
      print(" Please enter valid question number !! ")
   
    print("---------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------What to do next ?---------------------------------------------")
    print("---------------------------------------------------------------------------------------------------------")
    print()
    questions()
    
    
  elif queans==3:
    adminmenu()
     
  else:
    print("\t\t\t Enter a valid choice..")

import csv


def no_gender(gender):
    import csv
    count = 0
    with open("dating.txt", "r") as f:
        readerm = csv.reader(f)
        for row in readerm:
            for field in row:
                if field == gender:
                    count = count + 1
    return count


def pie_chart():
    import pandas as pd
    from matplotlib import pyplot as plt
    import numpy as np
    import matplotlib.pyplot as plt
    cars = ['Male', 'Female', 'Other']
    data = [no_gender('M'), no_gender('F'), no_gender('O')]
    explode = (0.1, 0.2, 0.3)
    colors = ("orange", "cyan", "brown")
    wp = {'linewidth': 1, 'edgecolor': "green"}
    
    def func(pct, allvalues):
        absolute = int(pct / 100. * np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)
        
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(data,
                                      autopct=lambda pct: func(pct, data),
                                      explode=explode,
                                      labels=cars,
                                      shadow=True,
                                      colors=colors,
                                      startangle=90,
                                      wedgeprops=wp,
                                      textprops=dict(color="magenta"))
    plt.plot(cars)
    plt.show()


def mfmembers():
    print(blue)
    print("\t\t\t 1). No of Male Members ")
    print("\t\t\t 2). No of Female Members ")
    print("\t\t\t 3). No of other gender Members ")
    print("\t\t\t 4). Pie chart ")
    print("\t\t\t 5). Back to Admin Menu ")
    print()
    print(green)
    mfmembers1 = int(input("\t\t\t Please enter your choice here: "))
    os.system('cls')
    print()
    if mfmembers1 == 1:
        count = no_gender('M')
        print(blue)
        print("\t\t\t Number of Male members ", count)
        print()
        mfmembers()
    elif mfmembers1 == 2:
        count = no_gender('F')
        print(blue)
        print("\t\t\t Number of Female members ", count)
        print()
        mfmembers()
    elif mfmembers1 == 3:
        count = no_gender('O')
        print(blue)
        print("\t\t\t Number of other gender members ", count)
        print()
        mfmembers()
    elif mfmembers1 == 4:
        print(pie_chart())
        mfmembers()
    elif mfmembers1 == 5:
        adminmenu()
    else:
        print()
        print()
        print('--------------------------------------------')
        print('--------------------------------------------')
        print("    !!  Enter any of the above option !!    ")
        print('--------------------------------------------')
        print('--------------------------------------------')
        print()
        print(white)

def customerlist():
  data = pd.read_csv('dating.txt', sep=',')
  print(data)
  cho=input("press [B/b] to go back: ")
  if cho=='b' or cho=='B':
    adminmenu() 

import csv
def mainmenu2():
    print()
    while True:
        print(green)
        print("""
           🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰
        \t\t\t Find the Perfect Match !
        \t\t\t 1). Register
        \t\t\t 2). Login
        \t\t\t 3). Exit
          🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰🀰
        """)
        print(white)

        x= int(input("\t\t\t Enter Choice: "))
        os.system('cls')
        if x==1:
          os.system('cls')
          print("")
          register()
            
        
        elif x==2:
          os.system('cls')
          print("")
          login()

        elif x==3:
          os.system('cls')
          print("")
          print("\t\t\t GOODBYE ")
          print("\t\t\tVisit Again")
          break

        else:
          print("\t\t\t Enter a valid choice.")
          print("")
          mainmenu2()  
          break
        print(white)

def register():
    print(red)
    print("--------------------------------------------------------------------------------")
    print("-----------------------------------Register-------------------------------------")
    print("--------------------------------------------------------------------------------")
    print()
    print(green)
    print("\t\t\t Sign up and tell us something about you !")
    print(blue)
    print()
    while True:
      with open ('dating.txt','a') as fo:
          writer=csv.writer(fo)
    
          fname=input("\t\t\t Enter First Name: ")
          print()
          lname=input("\t\t\t Enter Last Name: ")
          print()
          username=fname+lname[0]
          print("\t\t\t Your username is ",username.lower())
          print()
          print(red)
          print("\t\t\t Please Remember It !")
          print()
          pwd=input("\t\t\t Enter Password: ")
          print()
          check=True
          gen=input("\t\t\t Enter Gender [M/F/O]: ")
          print()
          email=input("\t\t\t Your E-Mail id: ")
          print()
          dob=input("\t\t\t Enter your Date of Birth dd/mm/yyyy: ")
          print()
          relegion=input("\t\t\t Enter your Relegion: ")
          print() 
          strengthlist=["Patience","Effeciency","Sensetive","Frank","Leadership","Time Punctual"]
          print(strengthlist)
          strengths=input("\t\t\t Enter Your Strengths [Select from list]: ")
          print()
          print('''
        
              \t\t\t ------ANSWER THE FOLLOWING TO BUILD YOUR PROFILE......-----
        
        ''')
          q1=int(input('''Do you regularly make new friends
	        
            \t1).Yes,Very often
	          2).Sometimes
	          3).Very Rarely
          '''))
          print()
        
          q2=int(input('''Do you spend your free time exploring various random topics that pique your interest?
	        
            \t1).Almost all time
	          2).Around half of the time
	          3.)Very rarely

          '''))
          print()

          q3=int(input('''How often you have a backup plan for a backup plan?
	        
            \t1).Yes,Very often
	          2).Sometimes
	          3).Very Rarely

          '''))
          print()

          q4=int(input('''How usually you stay calm under a lot of pressure?
        	
            \t1).yes,Very often
	          2).Sometimes
	          3).very Rarely
          '''))
          print()

          q5=int(input('''Do you prefer starting another work before completing the previous one?
        	
            1).Yes,Very often
	          2).Sometimes
	          3).Very Rarely
          '''))
          print()

          q6=int(input('''Are you very Sentimental?
	        
            1).Very sentimental
	          2).Not much sentimental
	          3).Not at all sentimental
          '''))
          print()

          q7=int(input('''Do you maintain your personal diary. writing, at the end of the day about the events happend during that day?
        	
            1).Yes, i write daily
            2).Yes,sometimes
            3).I don't maintain a diary

          '''))
          print()

          q8=int(input('''Do you use organizing tools like schedules and lists?
        	
            1).Yes
            2).No

          '''))
          print()

          q9=int(input('''Even a small mistake can cause you to doubt your overall abilities and knowledge?
	        
            1).Strongly agree
            2).Agree
            3).Disagree
            4).Strongly disagree
          '''))
          print()

          q10=int(input('''Would you like to go on a long walf with a music turned on, when u are upset about something?
        	
            1).Yes, it heals me
            2).It diverts my mind for sometime
            3).It doesn't helps me

          '''))
          print()

          q11=int(input('''How often you start the converstion when you meet someone?
	
            1.Yes,Very often
            2.Sometimes
            3.Very Rarely
          '''))
          print()

          q12=int(input('''How more inclined you are to follow your heart than your head?
  
            1.Yes,Very often
            2.Sometimes
            3.Very Rarely
          '''))
          print()

          q13=int(input('''Do you like going to brunch?
	
            1.Yes,Very often
            2.Sometimes
            3.Very Rarely
          '''))
          print()

          q14=int(input('''Do you worry about whether you made a good impression on people you meet?
	
            1.Yes,Very often
            2.Sometimes
            3.Very Rarely
          '''))
          print()


          q15=int(input('''Do you avoid leadership roles during group activities?
	
            1.Strongly agree
            2.Agree
            3.Disagree
            4.Strongly disagree
          '''))
          print()

          q16=int(input('''How often do you get angry
            1.Even small things make me angry
            2.Some particular things make me angry
            3.I am a cool head type
          '''))
          print()

          q17=int(input('''How often do you go to parties with friends?
	
            1.Yes,Very often
            2.Sometimes
            3.Very Rarely
          '''))
          print()


          q18=int(input('''Would you like to have a pet?
          
            1.I already have it
            2.Looking forward to own it
            3.I don't like to have pets
          '''))
          print()

          q19=int(input('''Which animal would you prefer to have it as a pet?
          
            1.Dog
            2.Cat
            3.Some other animal
            4.I don't like to have pets
          '''))
          print()

          q20=int(input('''How often do you keep promises?
          
            1.Yes,Very often
            2.Sometimes
            3.Very Rarely 
          '''))
          print()

  
          q21=int(input('''How often do you accept hard challenges?
          
            1.Yes,Very often
            2.Sometimes
            3.Very Rarely
          '''))
          print()

          q22=int(input('''How often do you go on holiday trips?

            1.Yes,Very often
            2.Sometimes
            3.Very Rarely
          '''))
          print()

          q23=int(input(''' Do you like to have a healthy argument-good fight?
	        
            1.Yes i like to argue
            2.I don't argue much
          '''))
          print()
        
    
          writer.writerow ([username.lower(),pwd, gen.upper(), email.lower(), dob, relegion.lower(), strengths.lower(), q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22 , q23])
          print(green)
          print("Your Registration is sucessful. Kindly login to start your journey")
          print(white)
          print()
          break
          

          

def login():
    print(red)
    print("-----------------------------------------------------------------------------------")
    print("---------------------------------------Login---------------------------------------")
    print("-----------------------------------------------------------------------------------")
    print(cyan)
    print()
    notloggedin=True
    while notloggedin==True:
      with open("dating.txt","r") as f:
        username=input("Enter Username: ")
        print()
        pwd=input("Enter Password: ")
        reader=csv.reader(f)
        for row in reader:
          for field in row:
            if field==username and row[1]==pwd:
              notloggedin=False
            else:
              break
        if notloggedin==True:
          print()
          print("Invalid username or password...")
        else:
          print()
          print("Access Granted ! Let the journey begin !!!")
          os.system("cls")
          profile(username)


def profile(username):
  print(yellow)
  print()
  print()
  print("Welcome ",username)
  print()
  print("------------------------------------------------------------------------------------")
  print("----------------------Welcome to your Profile---------------------------------------")
  print("------------------------------------------------------------------------------------")
  print()
  print("# Enter S/s if you want to search")
  print()
  print("# Enter M/m if you want to find the friends generatted by system")
  print()
  print("# Enter E/e to go to main menu.")
  print()
  choice=input("Enter your choice: ")
  os.system("cls")
  if choice=="S" or choice=="s":
    search(username)
  elif choice=="M" or choice=="m":
    match(username)
  elif choice=='E' or choice=='e':
    mainmenu2()
  else:
    print("Enter a Valid Choice")
    profile(username)
    print(white)

def search(username):
  print(red)
  print("---------------------------------------------------------------------------------")
  print("----------------------------------SEARCH MENU------------------------------------")
  print("---------------------------------------------------------------------------------")
  print()
  print(blue)
  print("""
  1). Search by Gender
  2). Search by Date
  3). Search by Keyword
  4). Return to Main Menu
  """)
  print()
  choice=input("How you want to Search ?: ")
  if int(choice)==1:
    gender()
    m=input("Enter B/b to go to main menu: ")
    os.system("cls")
    if m=='b' or m=='B':
      profile(username)
  elif int(choice)==2:
    date()
    m=input("Enter B/b to go to main menu: ")
    os.system("cls")
    if m=='b' or m=='B':
      profile(username)
    z=input("Enter B/b to go to main menu: ")
    os.system("cls")
    if z=='b' or z=='B':
      profile(username)
  elif int(choice)==3:
    print(blue)
    keyword1=input("Enter the keyword by which you want to search: ")
    print()
    print(white)
    keyword(keyword1)
    print(yellow)
    b=input("Enter B/b to go to main menu: ")
    if b=='B' or b=='b':
      profile(username)
    else:
      print("Enter a valid input...")
  elif int(choice)==4:
      profile(username)
  else:
    print("-------------------------------------------------------------------------------")
    print("--------------------------Enter a valid Search choice--------------------------")
    print("-------------------------------------------------------------------------------")
    search()
    print(white)

def keyword(keyword1):
  print(red)
  print("-------------------------------------------------------------------------------")
  print("---------------------------------MATCH SEARCH--------------------------------")
  print("-------------------------------------------------------------------------------")
  print()
  print(white)
  wordfound=False
  while wordfound==False:
    with open("dating.txt","r") as f:
      reader=csv.reader(f)
      for row in reader:
        for field in row:
          if field==keyword1:
            print(row[0],row[2],row[3])
            wordfound=True

def match(username):
  compatibility_record = {}
  print(cyan)

  print("----------------------------------------------------------------------------------")
  print("-----------------------------------SYSTEM SEARCHED FRIENDS------------------------------------")
  print("----------------------------------------------------------------------------------")
  wordfoundm=False
  while wordfoundm==False:
    with open("dating.txt","r") as f:
      reader=list(csv.reader(f))
      templist1=enumerate(reader)
      for midx, row in templist1:
        for field in row:
          if field==username:
            User_gender=row[2]
            mainuser_index=midx
            wordfoundm=True
   
    if User_gender=='M':
      search_gender='F'
    elif User_gender=='F':
      search_gender='M'
    elif User_gender=='O':
      search_gender='O'

    with open("dating.txt","r") as f:
      readerm=list(csv.reader(f))
      templist=enumerate(readerm)
      for idx, row in templist:
        for field in row:
          if field == search_gender:
            user_index=idx
            name=row[0]
            
            que_no=1
            per_comp=0
            while que_no<=23:
              if (int(readerm[user_index][que_no+6])==int(readerm[mainuser_index][que_no+6])):
                per_comp=per_comp+4.3478260
              que_no=que_no+1
      
            compatibility_record.update({name:per_comp})
  top5 = sorted(compatibility_record.items(), key=lambda x: x[1], reverse=True)[:5]
  sr_no=1
  for i in top5:
    print("%d). %s is %d%s compatible with you" %(sr_no ,i[0] ,i[1],'%'))
    print()

    sr_no=sr_no + 1
  
  x=int(input("To open profile of any of the given user just enter respective number:- "))
  keyword((top5[x-1])[0])
  print(white)
  r=input("Enter b/B to go to main menu: ")
  if r=='B' or r=='b':
    profile(username)
    print()

def gender():
  os.system("cls")
  print(red)
  print("---------------------------------------------------------------------------------")
  print("--------------------------------Search By GENDER---------------------------------")
  print("---------------------------------------------------------------------------------")
  print()
  with open("dating.txt","r") as f:
    print(green)
    gender=input("Enter the Gender under which you are interested in ?: ")
    print()
    y=gender.upper()
    reader=csv.reader(f)
    for row in reader:
      for field in row:
        if field==y:
          print("The username, gender and email id of your selected gender in our list are: ",row[0],row[2],row[3])
          print()

def date():
  os.system("cls")
  print(red)
  print("----------------------------------------------------------------------------------------")
  print("--------------------------------Search By DATE OF BIRTH---------------------------------")
  print("----------------------------------------------------------------------------------------")
  print()
  with open("dating.txt","r") as f:
    print(green)
    dob=input("Enter the Date of Birth of the interested person ?: ")
    reader=csv.reader(f)
    for row in reader:
      for field in row:
        if field==dob:
          
          print(row[0],row[2],row[3])
          print(white)

mainmenu()