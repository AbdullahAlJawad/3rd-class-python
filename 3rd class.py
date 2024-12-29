'''student_name=input("Enter the student name:")
age=int(input("Enter the age:"))
GPA=float(input("Enter the GPA:"))
Math=float(input("Enter the math number:"))
library=input("Do you have library card? (yes/no):").lower()=="yes"
science_lab=input("Do you have science lab? (yes/no):").lower()=="yes"
print("The Student name is ",+student_name)
print("Student age is",+age)
print("Studetn GPA is",+GPA)
print("Student's math number",+Math)
print("Student library access",+library)
print("Student science_lab access",+science_lab)'''

name = "Glenn Maxwell"
team= "Delhi Capitas"
match_runs= "106 runs in 46 balls"

print(f"The length of the name is {len(name)}")
print(f"The length of the team is {len(team)}")
print(f"The length of the match runs is {len(match_runs)}")

print(f"first letter of the player{name[0]}")
print(f"first letter of the team{team[0]}")
print(f"first letter of the match runs{match_runs[0]}")

str ="String"
print(str[::3])
print(str[0::1])
print(str[::-1])

print(f"last 5 letter of the team{team[-5:]}")
print(f"first 5 letter of the player{name[:5]}")

text = input("Enter the text:")
revtext = text[::-1]
print(revtext)