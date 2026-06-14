# 📚 Python Stack Workflow Implementation

A lightweight, clean console demonstration of a **Stack** data structure implemented using pure Python. This project highlights foundational data handling built around the **LIFO (Last In, First Out)** structural principle.

---

## ⚙️ Core Operations Implemented
* **`push(element)`**: Appends a new data item to the top of the stack and provides a real-time console confirmation tracker.
* **`pop()`**: Extracts and returns the top-most item from the stack. Includes safety validation to handle structural **Underflow** conditions.
* **`is_empty()`**: A modular helper function that returns a boolean state evaluating whether the stack contains elements.
* **`peek()`**: Inspects the current top element of the stack (`Stack[-1]`) without removing it from the sequence, backed by defensive validation checks.
* **`size()`**: Dynamically calculates and displays the exact integer count of the items currently residing in the stack.

---

## 🧠 CS Concepts & Logic Applied
* **LIFO Architecture**: Ensures that the last element added is always the first one to be extracted—the core logic driving undo/redo operations and navigation history tracking.
* **Defensive Error Guarding**: Utilizes modular state checks to capture edge cases (like popping or peeking from a blank list), preventing runtime tracebacks and managing memory boundaries gracefully.

---

## 🚀 How to Run

1. Make sure you have Python installed, then clone or copy this script.
2. Open your terminal, navigate to the project directory, and start an interactive Python shell:
   ```bash
   python -i Stack.py
