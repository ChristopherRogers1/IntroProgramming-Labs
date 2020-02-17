def main():
    print("PYTHON GUESSING GAME")
    answer = "rat"
    zero = 0
    while zero==0:
        print("I am thinking of an animal")
        guess = input("Guess what animal I am thinking of ('quit' to cancel): ")
        if guess.lower() == answer:
            zero += 1
            print("Correct guess, congratulations!")
            ratCheck = 0
            while ratCheck == 0:
                response = input("Do you like this animal? Y/N: ")
                if response[0].lower() == "y":
                    print("I also like this animal")
                    ratCheck+=1
                elif response[0].lower() == "n":
                    print("It's a shame you don't like this animal.")
                    ratCheck+=1
                else:
                    print("Invalid answer, try again:")
        elif guess[0].lower() == "q":
            zero += 1
        else:
            print("Incorrect guess, try again")
    print("done")
main()
