

n = int(input("Enter number of students: "))
group_A = set()   # Harmonium
group_B = set()   # Tabla
group_C = set()   # Guitar
all_students = set()

for i in range(n):
    print(f"\nStudent {i+1}:")
    name = input("Enter student name: ").strip()
    all_students.add(name)

    if input("Plays Harmonium? (yes/no): ").lower() == "yes":
        group_A.add(name)
    if input("Plays Tabla? (yes/no): ").lower() == "yes":
        group_B.add(name)
    if input("Plays Guitar? (yes/no): ").lower() == "yes":
        group_C.add(name)

print("\n(a) Both Harmonium & Tabla:", group_A & group_B)

print("(b) Either Harmonium or Tabla but not both:", group_A ^ group_B)


print("(c) Count of students playing neither Harmonium nor Tabla:", len(all_students - (group_A | group_B)))


print("(d) Count of students playing Harmonium & Guitar but not Tabla:", len((group_A & group_C) - group_B))