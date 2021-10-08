import sys

def arg_reader():
    # What if there wasn't the right number of inputs?
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        col_num = sys.argv[2]
    elif len(sys.argv) < 3:
        raise IndexError(f"User provided too few arguments. Expected: "
                         f"<script> <file> <colnum>. Got: {sys.argv=}")
    else:
        raise ValueError(f"User provided too many arguments. Expected: "
                        f"<script> <file> <colnum>. Not sure what to do with "
                        f"remainder.")
        
    # What if this argument was castable as a int?
    try:
        col_num = int(col_num)
    except ValueError:
        print(f"ValueError: Column number should be numeric literal. Got: {col_num=}", file=sys.stderr)
        sys.exit(1)
        
    return filename, col_num


def col_values(filename, col_num):
    
    # What if we couldn't open the file?
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"FileNotFoundError: File '{filename}' doesn't exist.", file=sys.stderr)
        sys.exit(1)
    
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
    sys.exit(0)

if __name__ == "__main__":
    main()