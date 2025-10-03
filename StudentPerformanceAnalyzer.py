import numpy as np
# Generate random marks for 30 students and 5 subjects
num = np.random.default_rng(seed=1)
marks = num.integers(low=0, high=101, size=(30, 5))
# Calculate class average
class_average = np.mean(marks)
# Average marks
avg_per_student = np.mean(marks, axis=1)
avg_per_subject = np.mean(marks, axis=0)
# Max and min scores per student
max_per_student = np.max(marks, axis=1)
min_per_student = np.min(marks, axis=1)
# Max and min scores per subject
max_per_subject = np.max(marks, axis=0)
min_per_subject = np.min(marks, axis=0)
# Pass/Fail detection
pass_mask = np.all(marks >= 40, axis=1)
pass_students = np.sum(pass_mask)
fail_students = marks.shape[0] - pass_students
# Grouping students (6 groups, 5 students each)
groups = marks.reshape(6, 5, 5)
avg_per_group = np.mean(groups, axis=(1, 2))
top_group = np.argmax(avg_per_group)
# Assign letter grades
grades = np.empty(marks.shape, dtype='<U1')
grades[marks >= 90] = 'A'
grades[(marks >= 80) & (marks < 90)] = 'B'
grades[(marks >= 70) & (marks < 80)] = 'C'
grades[(marks >= 60) & (marks < 70)] = 'D'
grades[marks < 60] = 'F'
#Outputs:-
print("\n===== STUDENT PERFORMANCE SUMMARY =====\n")
print(f"🎯 Class Average: {class_average:.2f}\n")
print("👩‍🎓 Average Marks Per Student:")
for i, avg in enumerate(avg_per_student, 1):
    print(f"  Student {i:02d}: {avg:.2f}")
print()
print("📘 Average Marks Per Subject:")
for i, avg in enumerate(avg_per_subject, 1):
    print(f"  Subject {i}: {avg:.2f}")
print()
print("🔼 Max & 🔽 Min Marks Per Subject:")
for i in range(5):
    print(f"  Subject {i+1}: Max = {max_per_subject[i]}, Min = {min_per_subject[i]}")
print()
print("✅ Pass/Fail Summary:")
print(f"  Passed All Subjects: {pass_students}")
print(f"  Failed in At Least One Subject: {fail_students}\n")
print("👥 Average Marks Per Group:")
for i, avg in enumerate(avg_per_group, 1):
    print(f"  Group {i}: {avg:.2f}")
print(f"\n🏆 Top Scoring Group: Group {top_group + 1}\n")
print("🎓 Grade Distribution Per Subject:")
grade_labels = ['A', 'B', 'C', 'D', 'F']
for subj in range(marks.shape[1]):
    print(f"  Subject {subj + 1}: ", end='')
    counts = [np.sum(grades[:, subj] == g) for g in grade_labels]
    print(", ".join(f"{g}:{c}" for g, c in zip(grade_labels, counts)))
print()
print("📋 Grades Table (Students × Subjects):")
print(grades)