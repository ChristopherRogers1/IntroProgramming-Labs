def main():
    print("PYTHON GUESSING GAME")
    answer = "rat"
    zero = 0;
    while zero==0:
        print("I am thinking of an animal")
        guess = input("Guess what animal I am thinking of: ")
        if guess == "rat":
            zero += 1
        else:
            print("Incorrect guess, try again")
    print("done")
main()