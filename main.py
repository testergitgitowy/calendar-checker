import datetime
import calendar

def name(decision):
  print("Type period of time (in years): ", end = "")
  while True:
    try:
      period = abs(int(input()))
    except:
      print("Must be an integer (number). Try again:  ", end = "")
    else:
      break
  period *= 12
  print("Type the day you want to check for (1-Monday, 7-Sunday")
  while True:
    try:
      choosed_day = int(input())
      if 1 <= choosed_day <= 7:
        break
      else:
        print("Wrong number. Pass an integer in range (1-7): ", end = "")
    except:
      print("Must be an integer in range (1-7). Type again: ", end = "")
  day = datetime.date.today().day
  month = datetime.date.today().month
  year = datetime.date.today().year
  startdate=datetime.datetime(year, month, day)
  d = startdate
  match_amount = 0
  month_amount = 0
  control = 0
  while(period > 0):
    period -= 1
    if d.weekday() == choosed_day - 1:
      if control == 0 and decision == 1:
        print("Month's found: ")
        control = 1
      if control == 0 and decision == 0:
        control = 1
      match_amount += 1
      if decision == 1:
        print(calendar.month(d.year,d.month))
      if d.month != 1:
        month1 = d.month - 1
        d = d.replace (month = month1)
        month_amount += 1
      else:
        year1 = d.year - 1
        d = d.replace (month = 12, year = year1)
        month_amount += 1
      diff = abs(d - startdate)
    elif d.month != 1:
      month1 = d.month - 1
      d = d.replace (month = month1)
      month_amount += 1
    else:
      year1 = d.year - 1
      month1 = 12
      d = d.replace (month = month1, year = year1)
      month_amount += 1
  if control == 0:
    print("No matching were found.\nProbability: 0\nProbability expected: ", 1/7)
  else:
    print("Number of months found: ", match_amount)
    print("Number of months checked: ", month_amount)
    print("Number of days: ", diff.days)
    print("Probability found: ", match_amount/month_amount)
    print("Probability expected: ", 1/7)
    if decision == 1:
      print("Range of research:\nStarting month:")
      print(calendar.month(startdate.year, startdate.month))
      print("Final month:",)
      print(calendar.month(d.year, d.month))
print("Do you want to print out all of founded months?: [1/y][n/0]", end = " ")
true = ['1','y','Y','yes','YES','YEs','YeS','Yes','ye','Ye','YE']
false = ['0','no','NO','nO','No','n','N']
while True:
  decision = input()
  if decision in true:
    decision = 1
    break
  elif decision in false:
    decision = 0
    break
  else:
    print("Wrong inpsut. Try again: ")
name(decision)