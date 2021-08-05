# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your full name? \n")
name2 = input("What is their full name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_1 = name1.lower()
name2_1 = name2.lower()
names = name1_1 + ' ' + name2_1

names_t  = names.count("t")
names_r  = names.count("r")
names_u  = names.count("u")
names_e  = names.count("e")

names_true = str(names_t + names_r + names_u + names_e)

names_l  = names.count("l")
names_o  = names.count("o")
names_v  = names.count("v")
names_e1  = names.count("e")

names_love = str(names_l + names_o + names_v + names_e1)

names_true_love = int(names_true + names_love)

if names_true_love < 10 or names_true_love > 90:
  print(f"Your score is {names_true_love}, you go together like coke and mentos.")
elif names_true_love > 40 and names_true_love < 50:
  print(f"Your score is {names_true_love}, you are alright together.")
else:
  print(f"Your score is {names_true_love}.")
