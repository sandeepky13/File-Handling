# File-Handling
Menu-driven CRUD application built with Python File Handling to manage file operations such as Create, Read, Update, and Delete.
# 📂 Python File Handling CRUD Operation

A simple **CRUD (Create, Read, Update, Delete)** project built using **Python File Handling** and **OS Module**.

## 🚀 Features

* Create a file and store data
* Update existing file data
* Delete a file
* Read/View file content
* Menu-driven program using `while loop`

---

## 🛠️ Technologies Used

* Python
* File Handling
* OS Module

---

## 📁 Project Structure

```text
project/
│── main.py
│── data.txt
│── README.md
```

---

## 📌 CRUD Operations

### 1. Create File

Creates a file and writes user input data into it.

### 2. Update File

Updates existing content inside the file.

### 3. Delete File

Deletes the file using Python `os` module.

### 4. Read File

Displays the content stored in the file.

---

## ▶️ How to Run the Project

### Step 1: Clone Repository

```bash
git clone <your_repository_link>
```

### Step 2: Move to Project Folder

```bash
cd project_name
```

### Step 3: Run the Program

```bash
python main.py
```

---

## 💻 Sample Output

```text
========== File CRUD Menu ==========
1. Create
2. Update
3. Delete
4. Read
5. Exit

Enter Your Choice --> 1
Input your data: Hello World

File created successfully
```

---

## 📜 Example Code

```python
import os

file_name = "data.txt"

with open(file_name,"w") as f:
    f.write("Hello Python")
```

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

* Python File Handling
* File Modes (`r`, `w`, `a`)
* CRUD Operations
* While Loop
* Conditional Statements (`if-elif-else`)
* OS Module (`os.remove`, `os.path.exists`)

---

## 👨‍💻 Author

**Sandeep Kumar Yadav**
