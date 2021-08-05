print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print(f"Children tickets are for ${bill}")
  elif age <=18:
    bill = 7
    print(f"Youth tickets are for ${bill}.")
  else:
    bill = 12
    print(f"Adult tickets are for ${bill}.")

  want_photo = input("Do you want a photo to be clicked?It will cost extra $3. Y or N?")

  if want_photo == "Y":
    bill += 3
    print(f"Your total bill is ${bill}.")
else:
  print("Sorry, you have to grow taller before you an ride.")
