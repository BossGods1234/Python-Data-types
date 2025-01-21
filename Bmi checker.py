height = float(input("Enter your height here in cm: "))
weight = float(input("Enter your weight here in kg: "))
BMI = weight  / (height/100)**2
print("Your BMI is", BMI)  
if BMI <= 18.4:
    print("You are under weight")
if BMI <= 24.9:
    print("You are normal weight")
if BMI <= 29.9:
    print("You are over weight")
if BMI <= 34.9:
    print("You are severely over weight")
if BMI <= 39.9:
    print("You are Obese")
else:
    print("You are severely obese")
