import re

def num_extract(line):
# takes a line and extracts the first and last numbers found    
    digits = re.findall(r'\d', line)
    if len(digits) >= 2:
        return int(digits[0] + digits[-1])
    elif len(digits) > 0 and len(digits) < 2: # if only one num found
        return int(digits[0] + digits[0]) # duplicate the single num
    else:
        return 0
    
def calculate_sum(file_path):
# calculates sum of all numbers found in file
    total = 0 # running sum
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip() # remove white space
            total += num_extract(line) 
    return total

if __name__== "__main__":
    ## test function num_extract
    # line = "treb7uchet"
    # num = num_extract(line)
    # print("Extracted the number", num)
    
    input_file = 'input.txt'
    solution_sum = calculate_sum(input_file)
    print("The answer is", solution_sum)