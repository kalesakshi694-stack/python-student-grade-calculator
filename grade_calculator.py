print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks (0-100): "))
python = float(input("Enter Python marks (0-100): "))
science = float(input("Enter Science marks (0-100): "))

if not (0 <= maths <= 100 and 0 <= python <= 100 and 0 <= science <= 100):
    print("Invalid marks! Please enter marks between 0 and 100.")
else:
    total = maths + python + science
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n===== Student Result =====")
    print("Name:", name)
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)
