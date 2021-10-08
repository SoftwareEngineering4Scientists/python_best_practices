my_var = '-5.0'

if isinstance(my_var, (int, float)):
    if my_var >= 0:
        pass
    else:
        raise ValueError(f"Variable `my_var` is {my_var}. It should be greater than or equal to 0.")
else:
    raise TypeError(f"Variable `my_var` is a {type(my_var)}, when it should have been int or float.")

print("My variable: ", my_var)