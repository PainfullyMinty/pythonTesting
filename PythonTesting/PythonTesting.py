name = input("What is your name? \n")
print("Hello " + name + "!")

strAge = input("How old are you? \n")
age = int(float(strAge))
if age < 10:
    print("Wow, " + str(age) + " is pretty young...")
elif age >= 10 and age < 13:
    print("You're pretty much a twelvie at " + str(age))
elif age >= 13 and age < 20:
    print("TEENAGER ALERT. THE AGE OF " + str(age) + " SUGGESTS HIGH LEVELS OF TEEN.")
else:
    print(str(age) + ". That's old.")