number = int(input("Write your number: "))

if number % 2 == 0:
    print("Your number is EVEN")
else:
    print("Your numebr is ODD")



print("TICKET STATION:")

height=float(input("Tell me your height in m: "))
age=int(input("Tell me your age: "))
bill=0

if round(height, 2) > 1.20 and age > 5:#AND/OR/NOT
    if(age<=12):
        bill=5
        print(f"Your ticket cost: ${bill}")
    elif(age<=18):
        bill=7
        print(f"Your ticket cost: ${bill}")
    else:
        bill=12
        print(f"Your ticket cost: ${bill}")
    
    photo=input("You want to buy your photo? Y/N: ")
    if(photo=="Y"):
        bill+=3
        print(f"Your bill increase to {bill}")
    else:
        print("Your bill doesn't increase")
else:
     print("You can't get a ticket because your height or age")



print("BMI CALCULATOR:")

weight=float(input("Tell me your weight: "))
bmi=round(weight/(height**2),2)
if(bmi<18.5):
    print("You are UNDERWEIGHT")
elif(bmi<25):
    print("You are NORMAL WEIGHT")
elif(bmi<30):
    print("You are OVERWEIGHT")
elif(bmi<35):
    print("You are OBESE")
else:
    print("You are CLINICALLY OBESE")


print("LEAP YEAR CALCULATOR:")

year=int(input("Tell me the year: "))

if(year%4==0):
    print(f"{year} is a LEAP YEAR")
else:
    print(f"{year} is NOT a LEAP YEAR")