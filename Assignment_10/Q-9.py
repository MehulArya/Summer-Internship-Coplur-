import matplotlib.pyplot as plt

semesters = ['Sem 1', 'Sem 2', 'Sem 3']
marks = [7.8, 8.9, 8.5]
plt.bar(semesters, marks, color='ORANGE', label='CGPA')
plt.title("Semester-wise CGPA Comparison")
plt.xlabel("Semester")
plt.ylabel("CGPA")
plt.legend()
plt.show()
