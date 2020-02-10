def main():

    max = input("To what term of pi would you like to calculate?: ")

    total = 0
    
    if int(max) < 1:
        print("Invalid input, must be 1 or greater.")
    elif int(max) == 1:
        print(4)
    elif int(max) > 1:
        for x in range(0, int(max)):
            if (x%2 == 1):
                total = (total - 4/(x*2+1))
            elif (x%2 == 0):
                total = (total + 4/(x*2+1))
        print (total)            
    
main()
