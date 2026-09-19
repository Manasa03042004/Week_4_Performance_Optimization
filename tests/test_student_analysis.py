import unittest

from original.student_analysis_original import (
    generate_students as generate_original,
    calculate_average as average_original,
    find_top_students as top_original,
    calculate_statistics as statistics_original
)

from optimized.student_analysis_optimized import (
    generate_students as generate_optimized,
    calculate_average as average_optimized,
    find_top_students as top_optimized,
    calculate_statistics as statistics_optimized
)


class TestStudentAnalysis(unittest.TestCase):

    def test_student_generation(self):
        original = generate_original(100)
        optimized = generate_optimized(100)

        self.assertEqual(original, optimized)

    def test_average_calculation(self):
        marks = [80, 90, 70, 85, 95]

        self.assertEqual(
            average_original(marks),
            average_optimized(marks)
        )

    def test_top_students(self):
        students_original = generate_original(100)
        students_optimized = generate_optimized(100)

        result_original = top_original(students_original, 80)
        result_optimized = top_optimized(students_optimized, 80)

        self.assertEqual(result_original, result_optimized)

    def test_statistics(self):
        students_original = generate_original(100)
        students_optimized = generate_optimized(100)

        result_original = statistics_original(students_original)
        result_optimized = statistics_optimized(students_optimized)

        self.assertEqual(result_original, result_optimized)

    def test_large_dataset(self):
        students_original = generate_original(1000)
        students_optimized = generate_optimized(1000)

        self.assertEqual(
            top_original(students_original, 80),
            top_optimized(students_optimized, 80)
        )


if __name__ == "__main__":
    unittest.main()