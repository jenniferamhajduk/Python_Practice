#Convert Fahrenheit to Celsius and vice versa

temp = input("Enter a temperature for conversion. E.G. 32F or 12C: ")
assert 'C' in temp or 'F' in temp
temp_int = int(temp[:-1])

print(temp_int)

if 'C' in temp:
    conv = (temp_int * 1.8) + 32
    print("{0}F".format(conv))
if 'F' in temp:
    conv = (temp_int - 32) * 5/9
    print("{0}C".format(conv))


#Exercise: Think of another conversion you can do, height in feet to inches, for example
