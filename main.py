#the calculator file
import calculate_operations as calc_obj
import csv
import os
import json
from collections import Counter

#wrote each operation to a csv
def write_to_csv(val1, val2, result):
    field_names= ["Num 1", "Num 2", "Result"]

    #has the folder containing the script
    file_path = os.path.join(os.path.dirname(__file__), "calc_tracker.csv")
    
    file_exists = os.path.exists(file_path) #check if the file exists
    file_empty = (not file_exists) or os.path.getsize(file_path) == 0

    with open(file_path, "a") as calc_track:
        writer = csv.DictWriter(calc_track, fieldnames=field_names)

        if file_empty:
            writer.writeheader()
        
        data = dict(zip(field_names, [val1, val2, result]))
        writer.writerow(data)

#get the most and least frequent digit
def m_and_l_frequent_digit(filename):
    data = []
    individual_row = []
    with open(filename, 'r') as calc_data:
        reader = csv.DictReader(calc_data)
        for row in reader:
            individual_row = list(row.values())
            data.extend(individual_row)
    
    #conevrt each string to a float
    f_data = [float(s) for s in data]

    digits = []

    for num_str in f_data:
        if num_str == 0:
            digits.append(0)
        else:
            for char in str(num_str):
                #remove all of the minus signs, decimals, and turn 5.0 -> 5
                if char != '0' and char.isdigit():
                    digits.append(int(char))
    
    counter = Counter(digits) #returns an object of the frequency of each number

    #first and last tuple
    return counter.most_common()[0], counter.most_common()[-1]

#get the most and least frequent number
def m_and_l_frequent_num(filename):
    num1_list=[]
    num2_list=[]
    result_list=[]
    total_list=[]

    with open(filename, 'r') as calc_data:
        #print(calc_data.read())
        reader = csv.DictReader(calc_data)
        for row in reader:
            #parse columns into lists
            num1_list.append(float(row['Num 1']))
            num2_list.append(float(row['Num 2']))
            result_list.append(float(row['Result']))

    #append to one big list
    total_list.extend(num1_list)
    total_list.extend(num2_list)
    total_list.extend(result_list)

    counter = Counter(total_list)
    return counter.most_common()[0], counter.most_common()[-1]

def max_and_min(filename):
    num1_list=[]
    num2_list=[]
    result_list=[]
    total_list=[]

    with open(filename, 'r') as calc_data:
        #print(calc_data.read())
        reader = csv.DictReader(calc_data)
        for row in reader:
            num1_list.append(float(row['Num 1']))
            num2_list.append(float(row['Num 2']))
            result_list.append(float(row['Result']))

    total_list.extend(num1_list)
    total_list.extend(num2_list)
    total_list.extend(result_list)
    
    sorted_list = sorted(total_list)
    #first and last element
    return sorted_list[0], sorted_list[-1]

def average(filename):
    num1_list=[]
    num2_list=[]
    result_list=[]
    total_list=[]
    total_rows = 0
    with open(filename, 'r') as calc_data:
        total_rows = row_count(filename)
        #print(calc_data.read())
        reader = csv.DictReader(calc_data)
        for row in reader:
            num1_list.append(float(row['Num 1']))
            num2_list.append(float(row['Num 2']))
            result_list.append(float(row['Result']))

    total_list.extend(num1_list)
    total_list.extend(num2_list)
    total_list.extend(result_list)

    sum_list = sum(total_list)
    
    return sum_list / total_rows

def row_count(filename):
    total_rows = 0
    with open(filename, 'r') as calc_data:
        #print(calc_data.read())
        reader = csv.DictReader(calc_data)
        for row in reader:
            total_rows+=1
        return total_rows

def main():
    while True:
        val1 = float(input("Provide a number: "))
        val2 = float(input("Provide another number: "))
        operation = input("Choose operation (add, sub, mul, div): ").lower()
        result = 0

        # Call methods from calc_obj
        if operation == "add":
            result = calc_obj.add(val1, val2)
            write_to_csv(val1, val2, result)
        elif operation == "sub":
            result = calc_obj.sub(val1, val2)
            write_to_csv(val1, val2, result)
        elif operation == "mul":
            result = calc_obj.mul(val1, val2)
            write_to_csv(val1, val2, result)
        elif operation == "div":
            result = calc_obj.div(val1, val2)
            write_to_csv(val1, val2, result)
        else:
            print("Invalid operation")
            return
        
        print()

        filename = "calc_tracker.csv"

        #Calculations
        row_total = row_count(filename)
        most_common, least_common = m_and_l_frequent_digit(filename)
        most_num, least_num = m_and_l_frequent_num(filename)
        min_num, max_num = max_and_min(filename)
        avg = average(filename)

        data = {
            "Total Rows " : row_total,
            "Most Common Digit (MCD) ": most_common[0], 
            "MCD Frequency " : most_common[1],
            "Least Common Digit (LCD) ": least_common[0], 
            "LCD Frequency " : least_common[1],
            "Most Common Number (MCN) " : most_num[0],
            "MCN Frequency ": most_num[1],
            "Least Common Number (LCN) " : least_num[0],
            "LCN Frequency " : least_num[1],
            "Minimum Number " : min_num,
            "Maximum Number " : max_num,
            "Average " : f"{avg:.3f}"
        }

        output_file = "calculator_summary.json"
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        cont = input("  Press 'q' to quit: ")
        if cont == 'q':
            break

if __name__ == "__main__":
    main()
