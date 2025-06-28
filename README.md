# String Calculator using TDD Approach

A String Calculator implemented using the Test-Driven Development (TDD) approach with Python and Pytest.

---

## Prerequisites

- Python 3.x installed
- Virtual environment (venv) module available

---

## Installation and Setup

### 1. Clone the repository

    git clone git@github.com:NIKHILP16/StringCalculator.git
    cd StringCalculator

### 2. Setup Environment 

    Create and activate virtual environment

    -On macOS/Linux:
        python3 -m venv venv
        source venv/bin/activate

    -On Windows:
        python -m venv venv
        venv\Scripts\activate

### 3. Install Requirements

    pip install -r requirements.txt

### 4. Run tests normally

    pytest

### 5. Run tests with coverage report

    pytest --cov=calculator --cov-report=term-missing
