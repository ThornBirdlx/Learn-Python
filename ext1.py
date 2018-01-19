#!/usr/bin/env python3
#--coding:UTF-8--
from  sys import argv
from os.path import exists

script,from_file,to_file = argv

print ("Copying from %s to %s " % (from_file,to_file))

#we could do these two on one line,how?
in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long " % len(indata))

print ("Does the output file exists? %r"% exists(to_file))




 
#from sys import  argv

#script,file_name = argv


#txt = open(file_name)

#print(txt.read())
#txt.close()

#prompt = 'please enter:'

#print("Hi %s ,I'm the %s script." % (user_name,script))
#print("I'd like to ask you  a  few questions")
#print("Do you like me %s?" % user_name)
#likes = input(prompt)

#print ("Where do you like %s?" %user_name)
#lives = input(prompt)

#print("What kind of computer do you have ")
#computer = input(prompt)

#print ("""
#Alright,so you said %r about liking me .
#You like in  %r ,not sure where that is .
#And you have a %r couputer.Nice.
#"""% (likes,lives,computer))