str = "Abdulaziz Maxmudov"
print(len(str))

for s in str:
    print(s)

print(str[1:5])   

text = "Abdulaziz Maxmudov"

# 1. capitalize() - birinchi harfni katta qiladi
print(text.capitalize())  # Abdulaziz maxmudov

# 2. casefold() - barcha harflarni kichik qiladi
print(text.casefold())    # abdulaziz maxmudov

# 3. center() - markazlashtiradi
print(text.center(30, "-"))  # ----Abdulaziz Maxmudov----

# 4. count() - berilgan substring necha marta uchrashini hisoblaydi
print(text.count("a"))    # 2

# 5. encode() - byte formatga o‘zgartiradi
print(text.encode())      # b'Abdulaziz Maxmudov'

# 6. endswith() - oxiri ma'lum substring bilan tugashini tekshiradi
print(text.endswith("ov"))  # True

# 7. expandtabs() - tablarni kengaytiradi (agar bo'lsa)
text_tab = "A\tB\tC"
print(text_tab.expandtabs(4))  # A   B   C

# 8. find() - substringni qidiradi, birinchi indeksni qaytaradi
print(text.find("Max"))   # 9

# 9. format() - formatlash
print("Hello, {}".format(text))  # Hello, Abdulaziz Maxmudov

# 10. format_map() - dictionary bilan formatlash
info = {"name": text}
print("Hello, {name}".format_map(info))  # Hello, Abdulaziz Maxmudov

# 11. index() - find() kabi, lekin topilmasa error beradi
print(text.index("Max"))  # 9

# 12. isalnum() - faqat harf va raqam
print(text.isalnum())     # False (bo‘shliq bor)

# 13. isalpha() - faqat harflar
print(text.isalpha())     # False (bo‘shliq bor)

# 14. isascii() - ASCII belgilar
print(text.isascii())     # True

# 15. isdecimal() - faqat decimal son
print(text.isdecimal())   # False

# 16. isdigit() - faqat raqam
print(text.isdigit())     # False

# 17. isidentifier() - identifikator sifatida ishlay oladimi
print(text.isidentifier())  # False (bo‘shliq bor)

# 18. islower() - hamma kichik harfmi
print(text.islower())     # False

# 19. isnumeric() - faqat raqam
print(text.isnumeric())   # False

# 20. isprintable() - chop etiladigan belgi
print(text.isprintable()) # True

# 21. isspace() - faqat bo‘shliq
print(text.isspace())     # False

# 22. istitle() - sarlavha shaklida
print(text.istitle())     # True

# 23. isupper() - hamma katta harfmi
print(text.isupper())     # False

# 24. join() - iterable elementlarini birlashtiradi
print("-".join(["Abdulaziz", "Maxmudov"]))  # Abdulaziz-Maxmudov

# 25. ljust() - chapga tekislaydi
print(text.ljust(25, "-"))  # Abdulaziz Maxmudov------

# 26. lower() - kichik harfga o‘zgartiradi
print(text.lower())       # abdulaziz maxmudov

# 27. lstrip() - chapdagi bo‘shliqni olib tashlaydi
text_space = "   Abdulaziz"
print(text_space.lstrip())  # Abdulaziz

# 28. maketrans() va translate()
trans = str.maketrans("Abc", "XYZ")
print(text.translate(trans))  # XXdulXZiz Maxmudov

# 29. partition() - substring bo‘yicha bo‘linadi
print(text.partition("Max"))  # ('Abdulaziz ', 'Max', 'mudov')

# 30. replace() - substringni almashtiradi
print(text.replace("Maxmudov", "Tog'a"))  # Abdulaziz Tog'a

# 31. rfind() - oxirgi uchrashuvni topadi
print(text.rfind("a"))      # 6

# 32. rindex() - oxirgi uchrashuv indeksini topadi
print(text.rindex("a"))     # 6

# 33. rjust() - o‘ngga tekislaydi
print(text.rjust(25, "-"))  # ------Abdulaziz Maxmudov

# 34. rpartition() - oxirgi substring bo‘yicha bo‘linadi
print(text.rpartition(" " )) # ('Abdulaziz', ' ', 'Maxmudov')

# 35. rsplit() - oxirdan bo‘linadi
print(text.rsplit(" ", 1))  # ['Abdulaziz', 'Maxmudov']

# 36. rstrip() - o‘ngdagi bo‘shliqni olib tashlaydi
text_space2 = "Abdulaziz   "
print(text_space2.rstrip())  # Abdulaziz

# 37. split() - bo‘linadi
print(text.split())          # ['Abdulaziz', 'Maxmudov']

# 38. splitlines() - qator bo‘yicha bo‘linadi
text_lines = "Abdulaziz\nMaxmudov"
print(text_lines.splitlines())  # ['Abdulaziz', 'Maxmudov']

# 39. startswith() - boshlanishini tekshiradi
print(text.startswith("Abd"))  # True

# 40. strip() - chap va o‘ng bo‘shliqni olib tashlaydi
text_space3 = "   Abdulaziz   "
print(text_space3.strip())      # Abdulaziz

# 41. swapcase() - harflarni o‘zgartiradi
print(text.swapcase())          # aBDULAZIZ mAXMUDOV

# 42. title() - har so‘zning birinchi harfi katta
print(text.title())             # Abdulaziz Maxmudov

# 43. translate() - maketrans bilan birgalikda ishlatiladi
trans2 = str.maketrans("A", "X")
print(text.translate(trans2))   # Xbdulaziz Maxmudov

# 44. upper() - katta harfga o‘zgartiradi
print(text.upper())             # ABDULAZIZ MAXMUDOV

# 45. zfill() - boshiga 0 qo‘shadi
print(text.zfill(25))           # 000000000Abdulaziz Maxmudov