text = str(input("inserte una palabra: "))

for char in text:
    if not char.isalpha():
        print('Non-alphabetic char found!')
        break
else:
    print('All chars are alphabetic')