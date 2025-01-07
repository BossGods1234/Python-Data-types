print("Enter marks obtained in 4 subjects: ")
math = int(input("maths:"))
science = int(input("science:"))
english = int(input("english:"))
hindi = int(input("hindi:"))
sum = math+science+english+hindi
print("Sum of all subjects", sum)
per = (sum/400)*100
print(end="Percentage Marks =")
print(per)
