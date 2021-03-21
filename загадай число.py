guessesTaken = 0

print("Желаешь разбогатеть друг? Как тебя зовут?")
myName = input()

print("Ну тогда приступим!", myName, ",ты загадываешь число от 1 до 100. Ну а я пытаюсь одгодать")

while guessesTaken < 7:
    print("начнЁм?")
    guess = int(input())

    guessesTaken += 1

    if guess < number:
        print("Моё число больше твоего!")
    elif guess > number:
        print("Моё число меньше твоего!")
    elif guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Превосходно!", myName, ", ты угадал число с", guessesTaken, "попытки. Твой выигрыш - 10 очков!")

if guess != number:
        number = str(number)
        print("Жаль, но у тебя не осталось попыток. Я загадал число", number, ",но ты проиграл. \nЭй, вы двое сн