name = input("Enter student name: ")
student_id = input("Enter student ID: ")
cgpa = float(input("Enter CGPA: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter monthly family income: "))
student = {
    "Name": name,
    "Student ID": student_id,
    "CGPA": cgpa,
    "Attendance": attendance,
    "Family Income": income
}
scholarships = [
    "Merit Scholarship",
    "Need-Based Scholarship",
    "Academic Support Scholarship"
]
print("\nStudent Information:")
print(f"Name: {student['Name']}")
print(f"Student ID: {student['Student ID']}")
print(f"CGPA: {student['CGPA']}")
print(f"Attendance: {student['Attendance']}%")
print(f"Family Income: {student['Family Income']}")
print("\nAvailable Scholarships:")
for s in scholarships:
    print(s)
eligible = False   # Boolean variable

if cgpa >= 3.50 and attendance >= 85 and income <= 100000:
    decision = "Congratulations! You are eligible for Merit + Need-Based Scholarship."
    eligible = True

elif cgpa >= 3.50 and attendance >= 85:
    decision = "Congratulations! You are eligible for Merit Scholarship."
    eligible = True

elif cgpa >= 3.00 and attendance >= 75 and income <= 60000:
    decision = "Congratulations! You are eligible for Need-Based Scholarship."
    eligible = True

elif cgpa >= 2.50 and attendance >= 70:
    decision = "Congratulations! You are eligible for Academic Support Scholarship."
    eligible = True

else:
    decision = "Sorry! You are not eligible for any scholarship."
    eligible = False
print("\nScholarship Decision:")
print(decision)
print(f"\nEligible: {eligible}")