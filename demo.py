print("hello world from demo")
text = " Engineering".lstrip()
print(text)
test = "#ABC#".strip("#")
print(test)
text = "python PROGRAMMING".lower()
print(text)

text = "968-Maria, ( D@t@ Engineer );; 27y      "
text = text.replace("968-", "name:")
text = text.replace("27y", "age: 27").replace("D@t@", "Data").replace(";;", ",").replace("(", "").replace(")", "").replace(",", "|") 
text = text.strip().lower()  
print(text)

country = "USA"
print(country.isalpha())

phone = "123-456-7890"
print(phone.isdigit())

price = 35.6777
print(round(price,2))
price = 35.6777
print(f"{price:.2f}")

import random 
print(random.random())
print(random.randint(1,100))
print(random.choice(["apple", "banana", "cherry"]))


x = 7.0
print(type(x))
print(x.is_integer())
print(isinstance(x, float))

print(random.randint(1, 100))   
