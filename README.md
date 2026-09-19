# Week 4 - Performance Optimization in Python Applications

## Project Title

Student Marks Analytics & Report Generator

## Objective

The objective of this project is to analyze and optimize the performance of a Python application. The project demonstrates how profiling tools can be used to identify performance bottlenecks and how code optimization can significantly reduce execution time while maintaining the same functionality.

## Application Description

The application generates student records containing marks for five subjects and performs the following operations:

- Generates student records
- Calculates individual student averages
- Identifies students whose average is above a specified threshold
- Calculates overall statistics
- Displays the analysis results

The application processes a dataset of 10,000 students and 50,000 marks.

## Project Structure

```text
Week_4_Performance_Optimization/
│
├── original/
│   └── student_analysis_original.py
│
├── optimized/
│   └── student_analysis_optimized.py
│
├── profiling/
│   ├── baseline_profile.txt
│   ├── optimized_profile.txt
│   └── benchmark_results.txt
│
├── report/
│   └── performance_optimization_report.md
│
├── tests/
│   └── test_student_analysis.py
│
├── README.md
└── requirements.txt