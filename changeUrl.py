import csv
import sys

def editTime(filename):
	r = csv.reader(open(filename)) # Here your csv file
	lines = list(r)
	print("Please Enter The New Interval Time: ")
	newTime = input()
	lines[0][2] = str(newTime)
	writer = csv.writer(open(filename, 'w'))
	writer.writerows(lines)
	print("Interval Change Done")

def addLink(filename):
	print("Please Enter The Link For The Amazon Product: ")
	newRow = input()
	print("Please Enter The Threshold Price For That Product")
	newThreshold = input()
	newRow = "\n%s,%s,%s" % (newRow, newThreshold, '0')
	with open(filename, "a") as f:
	    f.write(newRow)
	print('New Product Added')

def Select(Option):
	if Option == '1':
		#Add Product
		addLink('Urls.csv')
		print("If you want to add another link, Please enter 1")
		print("If you want to change the time interval, Please enter 2")
		print("If you are finished and want to exit, Please enter 3")
		Option = input()
		Select(Option)

	elif Option == '2':
		#Edit Time Interval
		editTime('Urls.csv')
		print("If you want to add another link, Please enter 1")
		print("If you want to change the time interval, Please enter 2")
		print("If you are finished and want to exit, Please enter 3")
		Option = input()
		Select(Option)

	elif Option == '3':
		print("Designed And Built By Harry O'Connor Twitter @Harryoc493")
		print("Goodbye!")
		exit()
	else:
		print("Incorrect Input, Please try Again")
		Option = input()
		Select(Option)
print("Designed And Built By Harry O'Connor Twitter @Harryoc493")
print("Welcome, this program will allow you to: ")
print("Add Amazon Products To Tracks")
print("Edit The Time Interval Between Checking Prices")
print("To Add An Amazon Product, Please Enter 1")
print("To Change The Time Interval, Please Enter 2")
Option = input()
Select(Option)
