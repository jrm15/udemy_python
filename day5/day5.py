students_score = [78, 65, 89, 56, 2, 23, 54]
high=0

for score in students_score:
    if score > high:
        high=score

print("Highest score is: " + str(high))

for i in range(11):
    print(i)

total=0
for i in range(0, 11, 2):
    total += i
print(total)

