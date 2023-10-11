def calculate_grade(score):
    if score < 0 or score > 100:
        return "Error: Number is out of range"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = float(input("Enter a number between 0 and 100: "))

grade = calculate_grade(score)

print(f"Grade: {grade}")
