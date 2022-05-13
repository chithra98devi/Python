# elif statement

days = int(input("Enter the days"))

if days == 0:
    print("Good no fine")
elif days>1 and days<=5:
    print("Fine amount",days* 0.5)
elif days>5 and days<=10:
    print("Fine amount",days*1)
elif days>10 and days<=30:
    print("Fine amount",days*5)
else :
    print("Membership cancel")