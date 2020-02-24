# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Your Name Here
# Created: YYYY-MM-DD

def getName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    
    return first, last

def buildName(first, last):
    return (first + "." + last)

def checkStrength(passwd):
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one…")
    return passwd

def main():
    # get user's first and last names
    first, last = getName()
    
    # generate a Marist-style username
    uname = buildName(first,last)
    
    # ask user to create a new password
    passwd = input("Create a new password: ")
    
    # ensure the password has at least 8 characters
    checkStrength(passwd)
    print("Account configured. Your new email address is",
    uname + "@marist.edu")
main()
