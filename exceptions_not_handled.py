import sys

def arg_reader():
    # What if there wasn't the right number of inputs?
    filename = sys.argv[1]
    col_num = sys.argv[2]
    
    # What if this argument was castable as a int?
    col_num = int(col_num)
    return filename, col_num


def col_values(filename, col_num):
    
    # What if we couldn't open the file?
    file = open(filename, 'r')
    
    values = []
    for line in file:
        line_list = line.strip().split(',')
        # What if the line length after splitting was not col_num long?
        col_val = line_list[col_num]
        values.append(col_val)
        
    file.close()
    return values


def main():
    filename, col_num = arg_reader()
    values = col_values(filename, col_num)
    print(f"Column values: {values}")


if __name__ == "__main__":
    main()