# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
month_of_change = []  # Store months where changes occurred
net_change_list = []  # Store profit/loss changes between months
greatest_increase = ["", 0]  # [month, amount] for biggest profit increase
greatest_decrease = ["", 9999999999999999999]  # [month, amount] for biggest loss

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    header = next(reader)
    reader = csv.reader(financial_data)
    first_row = next(reader) total_months += 1 
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    # Count first month total_net += int(first_row[1]) # Add first month's profit/loss prev_net = int(first_row[1]) # Store for comparison with next month

    # Skip the header row
 
    # Extract first row to avoid appending to net_change_list
    for row in row_reader
        When 

    # Track the total and net change


    # Process each row of data
    for row in reader:

        # Track the total
    net_change_list = total_net + 1
    month_of_change = total_months + 1 

        # Track the net change


        # Calculate the greatest increase in profits (month and amount)
        if
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest decrease in losses (month and amount)
        if 
        greatest_decrease >prev_net -1
        Then greatest_decrease =prev_net


# Calculate the average net change across the months


# Generate the output summary


# Print the output


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
