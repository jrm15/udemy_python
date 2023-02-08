print("Welcome to the tip calculator.")

total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
perc = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

result = round((total + ((total*perc)/100))/people, 2)

print("Each person should pay: $", result)

#ERROR:print("Each person should pay: $ + result")
print (f"Each person should pay: ${result}")

#result=1

#ES IGUAL:
#result=result+1
#result+=1

