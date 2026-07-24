# Lab 1: Grade Evaluator & Archiver

## Project Overview

This project was developed as part of the **Introduction to Python Programming and Databases** course at the **African Leadership University (ALU)**.

The project consists of:

1. A **Python application** (`grade-evaluator.py`) that reads student grades from a CSV file, validates the data, calculates the final grade and GPA, determines whether the student has passed or failed, and identifies formative assignments eligible for resubmission.

2. A **Bash shell script** (`organizer.sh`) that archives the current `grades.csv` file by renaming it with a timestamp, moving it to an `archive` directory, creating a new empty `grades.csv`, and recording the operation in `organizer.log`.

---

## Project Structure

```
Lab1/

├── grade-evaluator.py
├── organizer.sh
├── grades.csv
├── README.md
├── organizer.log          (created after running organizer.sh)
└── archive/               (created after running organizer.sh)
```

---

## Features

### Python Application (`grade-evaluator.py`)

- Reads grade records from a CSV file.
- Validates that all scores are between 0 and 100.
- Validates that:
  - Total assignment weight equals 100.
  - Formative assignments total 60%.
  - Summative assignments total 40%.
- Calculates the final grade.
- Calculates the GPA using:

```
GPA = (Final Grade / 100) × 5.0
```

- Determines whether the student has PASSED or FAILED.
- Identifies the highest-weight failed formative assignment(s) eligible for resubmission.

---

### Bash Script (`organizer.sh`)

- Creates an `archive` directory if it does not already exist.
- Generates a timestamp.
- Renames `grades.csv` using the timestamp.
- Moves the renamed file into the archive folder.
- Creates a new empty `grades.csv`.
- Records every archive operation in `organizer.log`.

---

## Requirements

- Python 3
- Bash Shell (Linux, macOS, or WSL on Windows)

---

## How to Run the Python Program

Open a terminal in the project directory and run:

```bash
python3 grade-evaluator.py
```

or

```bash
python grade-evaluator.py
```

When prompted, enter the CSV filename:

```
grades.csv
```

The program will:

- Validate the data
- Calculate the final grade
- Calculate the GPA
- Display the student's status
- Show any eligible formative resubmissions

---

## How to Run the Shell Script

Give the script execute permission:

```bash
chmod +x organizer.sh
```

Run the script:

```bash
./organizer.sh
```

The script will:

- Archive the current `grades.csv`
- Create a new empty `grades.csv`
- Update `organizer.log`

---

## Example Output

```
--- Processing Grades ---

Weight validation passed.

Formative Marks: 35.00
Summative Marks: 25.00

Final Grade: 60.00%
GPA: 3.00

Status: PASSED
```

---

## Author

Name: Kelvin Bruce MUPENZI

GitHub: kelvinbruce110

Course: Introduction to Python Programming and Databases

Institution: African Leadership University
