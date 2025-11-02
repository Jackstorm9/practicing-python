grade = input("what is your grade?: ")
grade_evaluation = input("did you pass or fail?: ")

if grade_evaluation == "pass":
    print(f"congratulations on passing grade {grade}")
elif grade_evaluation == "fail":
    print(f"Don't worry, you'll do better next time in grade {grade}")
else:
    print("invalid answer")