# 1. Store the scores (plural)
scores = [85, 72, 91, 64, 78]

# 2. Print initial scores
print("Student Scores:")
for s in scores:
    print(s)

print()

# 3. Track student number and counts
student_num = 1
passed = 0 
failed = 0 

# 4. Check scores
for score in scores:
    if score >= 90:
        print(f"Student {student_num}: {score} - Excellent - Passed")
        passed = passed + 1
    elif score >= 80:
        print(f"Student {student_num}: {score} - Very Good - Passed")
        passed = passed + 1
    elif score >= 75:
        print(f"Student {student_num}: {score} - Good - Passed")
        passed = passed + 1
    else:
        print(f"Student {student_num}: {score} - Failed")
        failed = failed + 1
    
    student_num = student_num + 1

print()

# 5. Calculations and summary
total = sum(scores)
average = total // len(scores)

print("Total Score:", total)
print("Average Score:", average)
print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))
print("Passed:", passed)
print("Failed:", failed)