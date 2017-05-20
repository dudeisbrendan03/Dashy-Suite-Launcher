#Simple library call
import fileinput
#import os

#Open the file
#file = open('Configuration\config.json','w')
#message = file.read()
#print("Going to print the contents of the config")
#print(message)
#file.close()

#Start editing method 1
hostingurl = int(input("What is the hosting url for your bot (this is where the bot will say the address is. Include an address and port): "))
for line in fileinput.input("Configuration\config.json", inplace=True):
    print "hostingurl" % (fileinput.filelineno(), 4),

