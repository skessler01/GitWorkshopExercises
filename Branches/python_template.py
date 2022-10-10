# Variables
varA = 1
varB = 3
varC = 4
varD = 5

def operation(a, b, c, d):
    result = a+b+c+d
    return result

def operation2(a,b):
    return a-b
    
def operation3(a,b):
    return a*b

# Execute main operation
if __name__ == "__main__":
    op_result = operation(varA, varB, varC, varD)
    op2_result = operation2(varA,varB)
    op3_result = operation3(varA,varB)
    print("Result value: ", op_result)
    print("Result value2: ", op2_result)
    print("Result value3: ", op3_result)
