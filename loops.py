for i in range(1, 6):
    print("Son:", i)


fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print("Men yaxshi ko'raman:", fruit)


for i in range(1, 11):
    if i % 2 == 0:
        print(i)


while True:
    text = input("Biror narsa yozing (exit yozsangiz chiqadi): ")

    if text == "exit":
        print("Dastur tugadi")
        break

    print("Siz yozdingiz:", text)



for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i*j)

