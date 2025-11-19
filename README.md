# Python-Calculator-Analyzer

Python Calculator Tracker

This project tracks calculations made with a simple calculator and generates statistics from them.

## Features

- Takes user input for calculations (add, sub, mul, div)
- Writes each operation to a CSV file
- Parses the CSV data to calculate statistics:
  - Total Rows
  - Most Common Digit (MCD)
  - MCD Frequency
  - Least Common Digit (LCD)
  - LCD Frequency
  - Most Common Number (MCN)
  - MCN Frequency
  - Least Common Number (LCN)
  - LCN Frequency
  - Minimum Number
  - Maximum Number
  - Average
- Exports all statistics to a JSON output file

## How It Works

1. You enter numbers and choose an operation.
2. The result is saved to a CSV file.
3. The program reads the CSV to calculate statistics.
4. Statistics are saved to a JSON file for easy reference.

## Usage

Run the main script and follow the prompts to enter calculations. When finished, type `q` to quit and check the generated CSV and JSON files.
