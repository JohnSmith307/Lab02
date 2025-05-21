print("What is your name?")
user_name = input()
print("Hi, " + str(user_name) + ".")

print("How old are you, " + str(user_name) + "?")
user_age = input()
print("Hi, " + str(user_name) 
      + ". You're " + str(user_age) 
      + " years old.")

print("How tall are you in inches?")
user_height = input()
user_height_feet = int(user_height) / 12
print(str(user_name) + " is " + str(user_height_feet) + " feet tall.")

print("What is your favorite ice cream flavor " 
      + str(user_name) + "?")
user_icecream = input()
print(str(user_icecream) + ", " "Good choice!")
