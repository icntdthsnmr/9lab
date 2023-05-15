from PIL import Image, ImageFilter
from pathlib import Path
import os, csv

a = '1.jpg'
b = '2.jpg'
c = '3.jpg'
d = '4.jpg'
e = '5.jpg'

def z1():
    z = [a, b, c, d, e]
    count = 0
    for file in z:
        count += 1
        img = Image.open(file)
        new_img = img.filter(ImageFilter.EMBOSS)
        new_img.show()
        try:
            os.mkdir("D:/Dolmatsyn/helpmeplz")
        except:
            pass
        new_img.save(f"D:/Dolmatsyn/helpmeplz/new_img{count}.jpg")


def z2():
    z = [a, b, c, d, e]
    count = 0
    for file in z:
        if Path(file).suffix == '.jpg' or Path(file).suffix == '.png':
            count += 1
            img = Image.open(file)
            new_img = img.filter(ImageFilter.EMBOSS)
            new_img.show()
            try:
                os.mkdir("D:/Dolmatsyn/helpmeplz")
            except:
                pass
                new_img.save(f"D:/Dolmatsyn/helpmeplz/new_img{count}.jpg")
            else:
                print('Нет файлов типа .jpg или .png')

def z3():
    total_cost = 0

    with open('D:/Dolmatsyn/продукты.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)

        print("Нужно купить:")
        for row in reader:
            product = row[0]
            quan = int(row[1])
            price = int(row[2])
            cost = quan * price
            total_cost += cost

            print(f"{product} - {quan} шт. за {price} руб.")

        print(f"Итоговая сумма: {total_cost} руб.")