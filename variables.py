name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "Hello, " + full_name.title() + "!"

print(message)

#adding whitespace
print("\tPython")

print("Languages:\n\tJavaScript\n\tC#\n\tPython")

# rstrip() and lstrip() methods to get rid of white space
new_favorite_language = ' python'
new_favorite_language = new_favorite_language.lstrip()
print(new_favorite_language)

# Exercise 2-3 Personal Message
first_name = "Gary"
last_name = "Barry"
full_name = first_name + " " + last_name

personal_message = "Hello " + first_name + ", would you like to learn some Python today?"

print(personal_message)

# Exercise 2-4 Name Cases
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

# Exercise 2-5 and 2-6 Famous Quote
famous_person = "Gary"
famous_quote = '\n\t' + famous_person.title() + ' once spaketh the following, "A person who does not like sandwiches is not a person at all."'

print(famous_quote)

#Exercise 2-7
weird_jerry = " Jerry"
weird_larry = "Larry "

corrected_jerry = weird_jerry.lstrip()
corrected_larry = weird_larry.rstrip()

print(corrected_jerry + " and " + corrected_larry + " are best buds.")
