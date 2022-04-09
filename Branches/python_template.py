# Variables
varA = 1
varB = 3
varC = 4
varD = 5

def operation(a, b, c, d):
    result = a+b+c+d
    return result

# Execute main operation
if __name__ == "__main__":
    op_result = operation(varA, varB, varC, varD)
    print("Result value: ", op_result)
