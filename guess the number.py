n = 18
guesses = 1
while(guesses<=10):
    i = int(input("enter value:"))
    if i == 18:
        print("congratulations! you won")
        print("you took", guesses, "guesses")


    elif i > 18:
        print("decrease the value")

    else:
        print("increase the value")

    guesses = guesses + 1
if guesses > 10:
    print("game over!")