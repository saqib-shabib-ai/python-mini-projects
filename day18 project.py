# What are CSV Files?
'''
A CSV files is a simple text file used to store
tabular data (like a spredsheet or database table).
Each line represents a row, and valuse are separated
by commas.
'''
# Example

''' 
 Name,Math,Science,English
 Alice,85,80,78
 Bob,90,85,81
 Charlie,84,85,79
 '''

# Reading to CSV Files

import csv

with open('student.csv' , 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Read this data as Dictionary

import csv

with open('student.csv' , 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# Writing to CSV Files
import csv

with open('new_student.csv' , 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Math','Science','English'])
    writer.writerow(['Daisy',88,95,92])

# Write as Dictionay
import csv

with open('new_student.csv' , 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name','Math','Science','English'])
    writer.writeheader()
    writer.writerow({'Name': 'Eve', 'Math':91, 'Science':87, 'English':84})

# Day 18 Project: Student Report Genrator
import csv

# Step 1: Read data and Calculate averages
def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            student_report = []

            for row in reader:
                name = row['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])
                average = round((math + science + english)/ 3 ,2)
                status = "Pass" if average >= 60 else "Fail"

                student_report.append({
                    'Name':name,
                    'Math': math,
                    'Science': science,
                    'English': english,
                    'Average': average,
                    'Status': status
                })

    # Step 2: Write processed data to a new CSV
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['Name', 'Math', 'Science', 'English', 'Average', 'Status']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_report)

            print(f"Student report genrated {output_file} successfully. ")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
    except KeyError:
        print("Error: Invalid column names in the input file")
    except Exception as e:
        print(f"An error occured: {e}")

# Main Program
input_file = 'student.csv'
output_file = 'student_report.csv'

process_student_data(input_file, output_file)
    