# Production-Grade Python Implementations

Welcome to my Python Development Laboratory. This repository contains structured, production-ready Python solutions built to showcase clean code principles, architectural design patterns, robust error handling, and high-performance data processing. 

Each lab is engineered following industry best practices including strict PEP 8 compliance, explicit type hinting, and defensive programming principles.

---

## 🚀 Repository Overview

This repository is organized into distinct laboratories, each focusing on a core area of backend software engineering:

| Laboratory Module | Core Focus | Engineering Concepts Demonstrated |
| :--- | :--- | :--- |
| **01. School Management System** | Architecture & OOP | Factory Principles, Singleton Registries, Static Type Hinting, Dataclasses, Explicit Encapsulation |
| **02. Automated Log Analyzer** | Systems & Data | Stream Processing, Iterator/Generator Patterns (O(1) Memory Usage), Stream-safe File I/O, Regex Tokenization |

---

## 🛠️ Deep Dive: Lab Modules

### 1. School Management System (`/school_management`)
A decoupled backend architecture designed to manage student registration records and performance evaluations. 

* **Key Engineering Patterns:**
    * **Data Validation Optimization:** Implements Python `dataclasses` with post-initialization hooks (`__post_init__`) for rigorous defensive validation at object construction time.
    * **State Control Pattern:** Utilizes a unified `StudentRegistry` tracking instance to ensure structural reliability across data operations.
    * **Type Safety:** Built with absolute strictness utilizing Python’s `typing` module (`List`, `Dict`, `Optional`, `Enum`) to enable seamless static analysis using tools like `mypy`.

### 2. Automated Log & Metrics Analyzer (`/log_analyzer`)
A memory-efficient systems automation tool designed to process enterprise-level infrastructure log files safely.

* **Key Engineering Patterns:**
    * **Constant Memory O(1) Streaming:** Avoids massive file loading errors by using a Python line-by-line streaming `Generator`, ensuring execution stability even on files multi-gigabyte in size.
    * **Deterministic Regular Expressions:** Implements pre-compiled `re` objects to rapidly parse standard log strings into structured runtime tokens.
    * **Custom Exception Hierarchies:** Features clean domain-specific exception handling, creating custom errors (`LogFormatError`) for tracking anomalies without breaking the stream pipeline.

---

## 📈 Quality Standards & Best Practices

All implementations within this repository adhere strictly to the following parameters:

* **Formatting:** Formatted rigorously according to the **PEP 8** standard interface.
* **Documentation:** Fully documented using structured **Sphinx / Google Python Docstring** standards to ensure immediate clarity.
* **Execution Stability:** Configured defensively to gracefully isolate errors and prevent runtime cascade failure.

---

## ⚙️ Local Development Setup

To clone and inspect the code locally, execute the following commands in your terminal environment:

```bash
# Clone the repository
git clone [https://github.com/nirojg/Python-labs.git](https://github.com/nirojg/Python-labs.git)

# Navigate to the repository directory
cd Python-labs

# Verify script execution (Example: Lab 1)
python school_management/main.py
