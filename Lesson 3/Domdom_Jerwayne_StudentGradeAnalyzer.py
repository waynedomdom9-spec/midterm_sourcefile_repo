raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",

]


PASSING_GRADE = 75

student_scores = {}

print("--- RECORD PROCESSING LOG ---")
for record in raw_records:

    fields = record.split(",")

    if len(fields) != 4:
        print(f"Skipped invalid record (field count error): {record}")
        continue

    name = fields[0].strip()
    raw_scores = fields[1:]
    scores = []

    try:
        for score_str in raw_scores:
            scores.append(int(score_str.strip()))
    except ValueError:
        print(f"Skipped invalid record (numeric conversion error): {record}")
        continue

    student_scores[name] = scores

print("--------------------------------\n")


print("ORGANIZED STUDENT RECORDS")
# Sort the names alphabetically prior to displaying.
for name in sorted(student_scores.keys()):
    print(f"{name}: {student_scores[name]}")


ranking = []

passed_count = 0
failed_count = 0
sum_of_averages = 0


for name, scores in student_scores.items():
    if not scores:
        continue

    total = sum(scores)
    count = len(scores)
    average = total / count
    highest_score = max(scores)
    lowest_score = min(scores)

    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1

    sum_of_averages += average

    ranking.append((average, name, highest_score, lowest_score, remark))



ranking.sort(key=lambda item: item[0], reverse=True)

print("\nSTUDENT GRADE REPORT")
print(f"{'Rank':<6}{'Name':<7}{'Average':<9}{'Highest':<9}{'Lowest':<8}{'Remark'}")

# Use enumerate for rank index and tuple unpacking for fields.
for rank, (avg, name, hi, lo, remark) in enumerate(ranking, start=1):
    print(f"{rank:<6}{name:<7}{avg:<9.2f}{hi:<9}{lo:<8}{remark}")


total_students = len(ranking)

class_average = (sum_of_averages / total_students) if total_students > 0 else 0.0

print("\nCLASS SUMMARY")
print(f"Number of Students: {total_students}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")


if ranking:
    highest_student = ranking[0]
    lowest_student = ranking[-1]

    print(f"Highest: {highest_student[1]} - {highest_student[0]:.2f}")
    print(f"Lowest: {lowest_student[1]} - {lowest_student[0]:.2f}")