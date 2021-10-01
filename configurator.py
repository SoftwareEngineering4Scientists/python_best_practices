import configparser

my_config = configparser.ConfigParser()
my_config.read("./config.ini")

print("Sections: ", my_config.sections())

# FILES
input_file = my_config['FILES']['input']
output_file = my_config['FILES']['output']
print("input type: ", type(input_file), input_file)

# PARAMETERS
var = float(my_config['PARAMETERS']['var'])
print("var type: ", type(var), var + 3)

# OTHERS
pet_list = my_config['OTHERS']['petlist'].strip().split(',')
print(pet_list)