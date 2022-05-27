# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

last_age = 90
reamining_age = last_age - int(age)
days = 365 * reamining_age
weeks = 52 * reamining_age
months = 12 * reamining_age

print(f"YOu have {days} days, {weeks} weeks, {months} months left.")