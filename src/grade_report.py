"""
grade_report.py
Combine functions from earlier scripts into one small program:
takes a list of student marks and prints a short grade report.
This mirrors the shape of real EDA/report code used later.
"""

def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    return "Fail"

def build_report(students):
    """students: dict of {name: marks}. Returns a list of report lines."""
    lines = []
    for name, marks in students.items():
        lines.append(f"{name}: {marks} marks -> Grade {grade(marks)}")
    return lines

def pass_rate(students):
    passed = sum(1 for m in students.values() if m >= 40)
    return round(passed / len(students) * 100, 1)


if __name__ == "__main__":
    students = {
        "Asha": 92,
        "Ravi": 68,
        "Meera": 55,
        "Karan": 35,
        "Neha": 81,
    }

    print("--- Grade Report ---")
    for line in build_report(students):
        print(line)

    print(f"\nPass rate: {pass_rate(students)}%")