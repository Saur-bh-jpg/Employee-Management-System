# Employee Management System

## Project Overview
The **Employee Management System (EMS)** is a Python-based Command Line Interface (CLI) application designed to streamline the process of managing workforce data. It replaces manual record-keeping with an automated system that stores Employee IDs, Names, and Salaries in a persistent CSV database. This project demonstrates the practical application of File Handling, Data Persistence, and CRUD (Create, Read, Update, Delete) operations.

## Features
* **Add Employee:** create new records with unique IDs.
* **Display All:** View a tabular list of all employees currently in the database.
* **Search:** Quickly locate specific employee details using their ID.
* **Update Record:** Modify an existing employee's name or salary securely.
* **Delete Record:** Permanently remove an employee's data from the system.
* **Data Persistence:** All data is saved automatically to `emp.csv`, ensuring it is not lost when the program closes.

## Technologies Used
* **Language:** Python 3.x
* **Libraries:**
    * `csv` (for database operations)
    * `os` (for file management)
* **Tools:** Visual Studio Code (VS Code)

## Steps to Install & Run
1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    ```
2.  **Navigate to the Project Directory:**
    ```bash
    cd Employee-Management-System
    ```
3.  **Run the Application:**
    Execute the Python script using your terminal:
    ```bash
    python src/main.py
    ```
    *(Note: If you have a single file, run `python "Employee management system.py"`)*

## Instructions for Testing
1.  **Start the App:** Run the script to see the Main Menu.
2.  **Add Data:** Select Option `1` and enter `ID: 101`, `Name: TestUser`, `Salary: 5000`.
3.  **Verify:** Select Option `2` to confirm the user appears in the list.
4.  **Update:** Select Option `3`, enter `ID: 101`, and change the salary to `6000`.
5.  **Search:** Select Option `5` and search for `101` to see the updated details.
6.  **Delete:** Select Option `4` and delete `ID: 101`.
7.  **Exit:** Select Option `6` to close the program.


