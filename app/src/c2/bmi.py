# BMI calculation program
weight = float(input("weight(kg)? "))
height = float(input("height(cm)? "))

# BMI calculation
height = height / 100 # convert into meter
bmi = weight / (height * height)

# branch result by BMI value
result = ""

if bmi < 18.5:
    result = "skinny type"
# if (18.5 <= bmi) and (bmi < 25):
if (18.5 <= bmi < 25):
    result = "standard type"
# if (25 <= bmi) and (bmi < 30):
if (25 <= bmi < 30):
    result = "mild obesity"
if bmi >= 30:
    result = "severe obesity"

# display result
print("BMI  :", bmi)
print("result   :", result)