name = input("What is your name? ")
favorite_color = input("What is your Favorite color? ")
print(name + " likes " + favorite_color)
birth_year = input("What is Data of your birthday: ")
age = 2020 - int(birth_year)
print(age)
weight_lbs = input("What is your weight (lbs):")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

course = '''
Hi John,

Here is our first meeting

Thank you,
The Support of Team
See you later,
'''
print(course)
########$$$$#######Formating string
first = 'John'
last = 'Smith'
message = first + last + '  [' + last + ' ] is a coder'
msg = f' {first} [{last}] is a coder'
print(msg)
