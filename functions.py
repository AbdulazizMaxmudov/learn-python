def sum_numbers(*args):
    total = 0

    for num in args:
        total += num

    print(total)

sum_numbers(1, 2, 3, 4)
sum_numbers(10, 20, 30)

def print_user(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_user(name="Ali", age=25, city="Tashkent")



print(abs(-10))
print(abs(-3.5))


# Example list
numbers = [5, 2, 9, 1, 7, 4]

print("Original list:", numbers)

# len() - list uzunligi
print("Length:", len(numbers))

# max() - eng katta son
print("Max:", max(numbers))

# min() - eng kichik son
print("Min:", min(numbers))

# sum() - yig'indisi
print("Sum:", sum(numbers))

# sorted() - tartiblash
print("Sorted:", sorted(numbers))

# sorted(reverse=True) - teskari tartib
print("Sorted descending:", sorted(numbers, reverse=True))

# reversed() - listni teskari qilish
print("Reversed:", list(reversed(numbers)))

# enumerate() - index bilan chiqarish
print("\nEnumerate:")
for index, value in enumerate(numbers):
    print(index, value)

# zip() - boshqa list bilan birlashtirish
names = ["Ali", "Vali", "Sardor", "Bek", "Olim", "Jasur"]

print("\nZip example:")
for name, number in zip(names, numbers):
    print(name, number)

# map() - har elementga function qo'llash
print("\nMap example (multiply by 2):")
result = map(lambda x: x * 2, numbers)
print(list(result))

# filter() - faqat shartga mos elementlar
print("\nFilter example (even numbers):")
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

# all() - hammasi True bo'lsa
check = [True, True, True]
print("\nAll example:", all(check))

# any() - bittasi True bo'lsa
check2 = [False, False, True]
print("Any example:", any(check2))

# isinstance() - type tekshirish
print("\nIs numbers a list?", isinstance(numbers, list))

# range() bilan loop
print("\nRange example:")
for i in range(5):
    print(i)

# abs() - modul
print("\nAbsolute value:", abs(-10))

# round() - yaxlitlash
print("Round example:", round(3.7))

# pow() - daraja
print("Power example:", pow(2, 3))

# type() - type aniqlash
print("Type of numbers:", type(numbers))

# list() - boshqa collectionni listga aylantirish
text = "Python"
print("\nConvert string to list:", list(text))





