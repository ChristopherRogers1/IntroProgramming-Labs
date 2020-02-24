# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Your Name Here
# Created: YYYY-MM-DD

def getName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    
    return first, last

def buildName(first, last):
    fullName = first + "." + last
    return fullName.lower()

def getPass():
    passwd = input("Create a new password: ")
    realStrength(passwd)
    print("The force is strong in this one…")
    return passwd

def realStrength(passwd):
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    while (passwd.isupper() or passwd.islower()):
        print("Password not strong enough, use both upper and lower case!")
        passwd = input("Create a new password: ")

def main():
    # get user's first and last names
    first, last = getName()
    
    # generate a Marist-style username
    uname = buildName(first,last)
    
    # ask user to create a new password
    getPass()
    
    print("Account configured. Your new email address is",
    uname + "@marist.edu")
main()
