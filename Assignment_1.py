#.............Question-1.............
studentName = input("Enter Students Name: ")
studentsClass = input("Enter Class of the Student: ")
Maths = int(input("Enter marks of Maths: "))
Physics = int(input("Enter marks of Physics: "))
Chemistry = int(input("Enter marks of Chemistry: "))
English = int(input("Enter marks of English: "))
Biology = int(input("Enter marks of Biology: "))
totalMarks = Maths + Physics + Chemistry + English + Biology
percentage = (totalMarks/500) * 100

print(f"{studentName} of {studentsClass} has scored {totalMarks} out of 500.\nPercentage: {percentage}\n"
      f"Maths: {Maths}\nPhysics: {Physics}\nChemistry: {Chemistry}\nEnglish: {English}\nBiology: {Biology}\n")

#.............Question-2.............
str1 = input("Input String 1: ")
str2 = input("Input String 2: ")
res = str1 + str2
print(res)
print(res.count('M'))
res = "\t" + str1 + str2
print(res.expandtabs(40))