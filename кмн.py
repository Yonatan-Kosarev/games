from random import randint
t = ["Камень", "Ножницы", "Бумага"]
computer = t[randint(0, 2)]
player = False
while player == False:
    player = input("Камень, Ножницы, Бумага?")
    if player == computer:
        print("Ничья")
    elif player == "Камень":
        if computer == "Бумага":
            print("Проигрыш! Бумага накрыла Камень ")
        else:
            print("Победа! Камень сломал Ножницы ")
    elif player == "Бумага":
       if computer == "Ножницы":
           print("Проигрыш! Ножницы разрезали бумагу")
       else:
           print("Победа! Бумага накрыла Камень")
    elif player == "Ножницы":
        if computer == "Камень":
            print("Проигрыш! Камень сломал Ножницы")
        else:
            print("Победа! Ножницы разрезали Бумагу")
    else:
        print("Ты неправильно играешь! Просто напиши слово на РУССКОМ ЯЗЫКЕ, с Заглавной буквы без п р о б е л о в. ")
    player = False
    computer = t[randint(0, 2)]
