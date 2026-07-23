secret_number = 5
for i in range(3):
    a = int(input("guess the secret number between 1 and 10: "))
    if a == secret_number:
        print("you guessed it right!")
        break
    elif a < secret_number:
        print("too low")
    else:
        print("too high")
else:
    print("game over")