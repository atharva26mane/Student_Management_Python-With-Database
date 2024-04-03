Project For Engg Students  
This is a  mini project for Python (ostl)

---

# Student Management System

This project is a Student Management System developed in Python using Tkinter for the GUI and SQLite for the database.

## Installation Steps

1. **Install Python**: Make sure you have Python installed on your system.
2. **Install Required Libraries**: Use pip to install the necessary libraries. Run `pip install pillow` to install Pillow.
3. **Create Project**: Set up a project directory for the Student Management System.
4. **Create Python File**: Create a Python file to contain the code for the system.

## Project Structure

The project consists of a single Python file `main.py` containing the code for the Student Management System.

## Code Explanation

- **Import Libraries**: The necessary libraries such as Tkinter, SQLite3, and others are imported.
- **Create Database and Table**: The `Database()` function is defined to create the SQLite database and the STUD_REGISTRATION table if they don't exist.
- **Create GUI Window**: The `DisplayForm()` function is used to create the graphical user interface (GUI) layout for the application.
- **Insert Data into Table**: The `register()` function inserts data entered into the registration form into the database.
- **Reset Form**: The `Reset()` function clears all form fields.
- **Delete Student Record**: The `Delete()` function deletes the selected student record from the database.
- **Search Student Record**: The `SearchRecord()` function searches for student records based on the entered name.
- **Display Student Record**: The `DisplayData()` function fetches and displays all student records in the GUI.
- **Updation is also available.

## Usage

1. Run the `main.py` file to launch the Student Management System.
2. Use the GUI to register new students, view, delete, and search student records.

