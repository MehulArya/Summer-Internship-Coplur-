studentName = input("Enter Students Name: ")
studentsClass = input("Enter Class of the Student: ")
Maths = int(input("Enter marks of Maths: "))
Physics = int(input("Enter marks of Physics: "))
Chemistry = int(input("Enter marks of Chemistry: "))
English = int(input("Enter marks of English: "))
Biology = int(input("Enter marks of Biology: "))
totalMarks = Maths + Physics + Chemistry + English + Biology
percentage = int((totalMarks/500) * 100)

print(f"\nResult: {studentName} of class {studentsClass} has scored {totalMarks} out of 500.\n\nPercentage: {percentage}%,\n"
      f"\nMaths: {Maths}\nPhysics: {Physics}\nChemistry: {Chemistry}\nEnglish: {English}\nBiology: {Biology}\n")

if  percentage >= 60:
    print("Grade: A")
elif percentage < 60 and percentage > 50:
    print("Grade B")
elif percentage < 50 and percentage > 40:
    print("Grade C")
elif percentage < 40 and percentage > 30:
    print("Grade D")
elif percentage < 30 and percentage > 20:
    print("Grade E")
else:
    print("Grade: Fail")