#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    # Register a CSV dialect for parsing the CSV file
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    # Open the CSV file and read it using DictReader
    with open(csv_file_location, mode='r') as file:
        employee_file = csv.DictReader(file, dialect='empDialect')
        employee_list = []
        for data in employee_file:
            employee_list.append(dict(data))
    return employee_list

def process_data(employee_list):
    # Collect all department names
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data.get('Department', 'Unknown'))
    
    # Count occurrences of each department
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    
    return department_data

# Set the correct path to your CSV file
csv_file_path = '/home/student/data/employee.csv'

# Read the employee data from the CSV file
employee_list = read_employees(csv_file_path)

# Process the employee data to get department counts
dictionary = process_data(employee_list)

# Print the report
print(dictionary)
