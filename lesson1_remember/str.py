s = "cat"
s = s.upper()
print(s)

s1 = 'Hello'
s2 = ("Hel"
      "lo") # печатает просто Hello
s3 = """Line one
                        Line two"""
# тройные кавычки позволяют форматировать произвольно

print(s1)
print(s2)
print(s3)

s = "Hello everybody!"
print(len(s))
print(s[0])
print(s[4])
print(s[-1]) # отрицательная индексация - с конца

# s = "P y t h o n"
#ind   0 1 2 3 4 5
# index of last element = len()-1 or -1

# print(s[100]) - index error: string index out of range

# slicing -> my_string[start:end:step]
text = "automation"
       #0123456789

print(text[2:6])
print(text[:4]) # from start to ind 4 exclusive
print(text[4:]) # from ind 4 to the end
print(text[:]) # prints all
print(text[::2]) #evetu 2 symbol
print(text[::-1]) #reverse all
print(text[5:100]) #no error
print()

name = "Mariia"
last_name = "Ivanova"
age = 25
print(name+" "+last_name+ " - " + str(age))
print(f"Hi my name is {name} and my last name is {last_name} and I'm {age}")

#upper()/lower()
raw = "    Automation QA    "
print(raw.upper())
print(raw.lower())
#strip() убирает пробелы
print(raw.strip())
print(raw.strip().upper())

#split()/join()
csv_line = "Login/Registration ,Cart,Checkout"
parts = csv_line.split(",") #makes list ['obj1', '2']
print(parts)
print(" - ".join(parts)) # объединяет элементы списка в строку, можно указать объединитель
print()

#replace()
msg = "Test failed: element not found"
print(msg.replace("failed", "passed"))

#find() and index()
#find() -->-1 if substring is not found
#index()-->ValueError if substring is not found
s = "banana"
print(s.find("na"))
print(s.index("na"))

print(s.find("xyz"))
# print(s.index("xyz"))

#count()
print(s.count("na"))