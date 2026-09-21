# Student Management and Results Analysis System

A simple **Student Management and Results Analysis System** developed using **Python built-in libraries**.

This project allows users to manage student details, store marks, calculate total and average marks, assign grades, determine pass/fail status, and perform basic class result analysis.

## Features

* Add student details
* Store subject marks
* Calculate total marks
* Calculate average marks
* Calculate grades
* Check pass/fail status
* Display student results
* Calculate class average
* Find highest and lowest average
* Calculate pass percentage
* Menu-driven console application

## Technologies Used

* Python
* Python built-in functions
* `statistics` module
* Lists
* Dictionaries
* Functions
* Conditional statements
* Loops

## Python Library Used

### Statistics

The built-in `statistics` module is used to calculate the average of student marks.

```python
import statistics

average = statistics.mean(marks)
```

No external Python packages are required.

## Grading System

| Average Mark | Grade |
| ------------ | ----- |
| 90 - 100     | A+    |
| 80 - 89      | A     |
| 70 - 79      | B     |
| 60 - 69      | C     |
| 50 - 59      | D     |
| Below 50     | F     |

A student is considered **PASS** when the student scores at least 40 marks in every subject.

## Example Result

```text
===== STUDENT RESULT =====

ID: 101
Name: Anu
Marks: [85, 78, 90]

Total: 253
Average: 84.33
Grade: A
Result: PASS
```

## Class Analysis

The system can display:

```text
===== CLASS ANALYSIS =====

Number of Students: 10
Class Average: 76.5
Highest Average: 94.0
Lowest Average: 42.0
Passed: 8
Failed: 2
Pass Percentage: 80.0%
```

## How to Run

1. Download or clone this repository.

2. Open the project folder in VS Code or CMD.

3. Run the Python file:

```bash
python student_management.py
```

4. Select an option from the menu.

## Project Structure

```text
student-management/
│
├── student_management.py
└── README.md
```

## Future Improvements

The project can be extended with:

* Search student
* Update student details
* Delete student
* Save records using JSON
* CSV file support
* Subject-wise analysis
* Attendance management
* Graphical user interface using Tkinter
* Result report generation

## Author

**Teena Benny**

## License

This project is created for learning and educational purposes.
