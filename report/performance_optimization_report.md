# Performance Optimization Report

## 1. Introduction

This project focuses on identifying and optimizing performance bottlenecks in a Python application. The application developed for this task is a Student Marks Analytics & Report Generator.

The application generates student records, calculates student averages, identifies students above a specified performance threshold, and calculates overall statistics.

The objective was to establish a baseline performance measurement, identify the main bottleneck using profiling, implement optimizations, and compare the original and optimized implementations.

---

## 2. Project Objective

The main objectives of this project are:

1. Develop a Python application with a measurable computational workload.
2. Establish baseline performance.
3. Use profiling tools to identify performance bottlenecks.
4. Apply suitable optimization techniques.
5. Measure performance after optimization.
6. Verify that optimization does not change application results.
7. Document the performance improvement.

---

## 3. Application Description

The application processes student records containing marks for five subjects.

For each student, the application can:

- Generate student information.
- Calculate the average marks.
- Identify students whose average is at least 80.
- Calculate total marks processed.
- Calculate the overall average.

The performance tests use a dataset containing:

- 10,000 students
- 5 subjects per student
- 50,000 individual marks

---

## 4. Baseline Implementation

The original implementation was created before optimization to provide a realistic performance baseline.

The original program used a nested search inside the `find_top_students()` function.

For every student who met the threshold, the program searched through the existing `top_students` list to determine whether the student had already been added.

This check was unnecessary because each student is processed only once.

---

## 5. Baseline Performance Analysis

The original program was profiled using Python's `cProfile` module.

Command used:

```bash
python -m cProfile -s cumulative original/student_analysis_original.py