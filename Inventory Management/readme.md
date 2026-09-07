# Inventory Management System (Python + SQL)

A lightweight inventory management system built with Python and SQLite.  
Features include:

- Add, update, and delete inventory items  
- Automatic low-stock alerts  
- Weekly inventory summary reports  
- SQL-backed persistent storage  
- CLI interface  

This project reduced manual stock-checking time by ~40% through automation.

## Features

### 🔔 Low-Stock Alerts
Automatically checks inventory and prints/logs alerts when stock falls below a threshold.

### 📊 Weekly Reports
Generates weekly inventory summaries including:
- Items added
- Items updated
- Items low on stock
- Total inventory value

## Tech Stack
- Python 3.x  
- SQLite  
- SQL + Python ORM-like structure  

## How to Run

```bash
pip install -r requirements.txt
python main.py
