print("Шифрование и расшифровка методом Цезаря")
while True:
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    a = int(input("Выберете команду (зашифровать-1, расшифровать-2): "))
    if a == 1:
        word = input("Введите слово на английском языке: ")
        key = int(input("Введите сдвиг (1-25): "))
        word = word.lower()
        wordX = ""
        for i in word:
            position = alphabet.find(i)
            newPosition = position + key
            if i in alphabet:
                wordX = wordX + alphabet[newPosition]
            else:
                wordX = wordX + i
        print("Ваш шифр:", wordX)
    elif a == 2:
        word = input("Введите шифр на английском языке: ")
        key = int(input("Введите сдвиг (1-25): "))
        word = word.lower()
        wordX = ""
        for i in word:
            position = alphabet.find(i)
            newPosition = position - key
            if i in alphabet:
                wordX = wordX + alphabet[newPosition]
            else:
                wordX = wordX + i
        print("Получилось:", wordX)
    else:
        print("Вы ввели не верную комнанду, попробуйте еще раз")