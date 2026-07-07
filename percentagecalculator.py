print("Enter Marks Obtained in 4 Subjects:")
math = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = math + science + hindi
print("sum of math,english,science,hindi is:", sum)

perc = (sum/400)*100

print (end="Percentage Mark = ")
print(perc)