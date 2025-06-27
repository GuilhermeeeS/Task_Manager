# Task Manager 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height=50/>
          

# ✅ Simple Task Manager | Python Project

This repository contains a simple task management system built with Python.  
It allows you to create, list, complete, remove and filter tasks.  
Tasks are stored in a JSON file, ensuring persistence between runs.

<br>

## ⚙️ Features

• Add tasks with description, deadline and priority <br>  
• List pending or completed tasks <br>  
• Mark tasks as completed <br>  
• Remove tasks <br>  
• Filter pending tasks by priority <br>  
• Store tasks in a local JSON file (`tasks.json`) <br>

<br>

## 📁 Project Structure

The project is divided into two files:

- `main.py`: Handles the user interface, displays the menu and captures input  
- `tasks.py`: Contains the `TaskManager` class that handles all task logic

<br>

## 🛠️ Customization

To change the name or path of the storage file (`tasks.json`),  
edit the `file_name` parameter in the `TaskManager` class in `tasks.py`.

```python
task_manager = TaskManager(file_name="your_file.json")
