# Variables
varA = 1
varB = 3
varC = 4
varD = 5

# For partner A:
# ret_val = ((a+b) * c)/d
# For partner B:
# ret_val = (a*c +  b*c)/d
def operation(a, b, c, d):
    ret_val = 0
    return ret_val


# Execute main operation
if __name__ == "__main__":
    op_result = operation(varA, varB, varC, varD)
    print("Result value: ", op_result)
