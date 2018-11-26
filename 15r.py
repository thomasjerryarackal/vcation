being=int(input("enter the day start for vaction"))
length=int(input("total number of days"))
total=being+length
if (total%7==0):
	print("return on sunday")
elif (total%7==1):
	print("return on monday")
elif (total%7==2):
	print("return on tuesday")
elif (total%7==3):
	print("return on wednesday")
elif (total%7==4):
	print("return on thrusday")
elif (total%7==5):
	print("return on friday")
elif (total%7==6):
	print("return on saturday")
