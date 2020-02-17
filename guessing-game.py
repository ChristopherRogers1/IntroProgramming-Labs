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
        elif guess.lower() == "quit":
            zero += 1
        else:
            print("Incorrect guess, try again")
    print("done")
main()
