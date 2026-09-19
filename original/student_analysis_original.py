import time


def generate_students(count):
    students = []

    for i in range(count):
        students.append({
            "id": i + 1,
            "name": f"Student_{i + 1}",
            "marks": [
                (i * 7 + 65) % 36 + 60,
                (i * 5 + 72) % 31 + 65,
                (i * 3 + 80) % 21 + 70,
                (i * 9 + 55) % 41 + 55,
                (i * 4 + 90) % 11 + 85
            ]
        })

    return students


def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)


def find_top_students(students, threshold):
    top_students = []

    # Intentionally inefficient nested search
    for student in students:
        average = calculate_average(student["marks"])

        if average >= threshold:
            found = False

            for existing in top_students:
                if existing["id"] == student["id"]:
                    found = True
                    break

            if not found:
                top_students.append({
                    "id": student["id"],
                    "name": student["name"],
                    "average": average
                })

    return top_students


def calculate_statistics(students):
    total_marks = 0
    total_subjects = 0

    for student in students:
        for mark in student["marks"]:
            total_marks += mark
            total_subjects += 1

    average = total_marks / total_subjects

    return {
        "total_students": len(students),
        "total_subjects": total_subjects,
        "overall_average": average
    }


def run_application():
    students = generate_students(10000)

    top_students = find_top_students(students, 80)

    statistics = calculate_statistics(students)

    print("Student Marks Analysis")
    print("-" * 30)
    print(f"Total students: {statistics['total_students']}")
    print(f"Total marks processed: {statistics['total_subjects']}")
    print(f"Overall average: {statistics['overall_average']:.2f}")
    print(f"Students above threshold: {len(top_students)}")


if __name__ == "__main__":
    start = time.perf_counter()

    run_application()

    end = time.perf_counter()

    print(f"Execution time: {end - start:.6f} seconds")