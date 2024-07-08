# Read height and weight inputs as floats for precision
height = float(input("Enter your height in meters, e.g. 1.83: "))
weight = float(input("Enter your weight in kilograms, e.g. 72.5: "))

# Calculate BMI and round to one decimal place
bmi = round(weight / (height ** 2), 1)

# Print the BMI and the respective category
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 24.9:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 29.9:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 34.9:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
