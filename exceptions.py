try:
    data = int(input("Son kiriting"))
    result = 100 / data

except ValueError:
    print("Son kiriting")

except ZeroDivisionError:
    print("0 bo'lishi mumkin emas")

else:
    print("Natija:", result)

finally:
    print("Program finished")