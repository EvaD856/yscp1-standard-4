'''
Question 3: Nested Loops (Multiplication Table)
Description: Write a program that uses nested loops to print the multiplication table for numbers 1 to 5.
'''
table = 0
for x in range(1,6):
    table += 1 
    num_table = 0
    print(f"---Multiplication Table for {table}---")
    for i in range(12):
        num_table += 1
        product = num_table * table
        print(f"{num_table} * {table} = {product}")
    print("")
















# This program will print the multiplication tables from 1 to 5 

# Use a for loop to iterate through the numbers for each table


    # Use a nested loop to print the table for each number
    