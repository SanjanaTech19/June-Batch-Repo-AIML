def analyze_result(name, roll, marks):
    print("Student:", name, "(Roll:", str(roll) + ")")
    
    # Calculate total and average
    total = sum(marks)
    average = total / 5
    print("Total:", total, ", Average:", average)
    
    # Assigning grade based on the average
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"
        
    print("Grade:", grade)
    
    #Checking for subjects below 40
    subject_number = 1
    for mark in marks:
        if mark < 40:
            print("Subjects below 40: Subject", subject_number)
        subject_number = subject_number + 1
        
    print("-" * 40)

# Test with the assignment example
name = "Aarav"
roll = 101
marks = [88.5, 35.0, 76.0, 92.5, 48.0]

analyze_result(name, roll, marks)