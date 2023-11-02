#print("Hello teacher")
#print("Homework №9 Banul")

#1. Даний текстовий файл.Необхідно створити новийфайл, який потрібно переписати з першого
#всі слова, що складаються не менше ніж з семи літер.

with open("first_text.txt", "r") as input_file:
    with open("second_text.txt", "w") as output_file:
     for line in input_file:
        words = line.split()
        long_words = [word for word in words if len(word) >= 7]
        output_file.write(" ".join(long_words) + "\n")

