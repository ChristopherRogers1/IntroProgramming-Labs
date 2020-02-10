
def main():
    num1 = 0
    num2 = 1
    temp = 0

    target = input("What number of the fibonacci sequence would you like to find?: ")

    if (int(target)==0):
        print (num1)
    
    for x in range(0, int(target)):
        temp = num1
        num1 = num1 + num2
        num2 = temp
        print (num1)
main()
