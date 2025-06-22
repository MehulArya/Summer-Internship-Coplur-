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