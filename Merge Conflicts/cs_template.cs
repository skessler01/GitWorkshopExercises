using System;
					
public class Program
{
    
	public static void Main()
	{   
        Int varA = 1;
        Int varB = 2;
        Int varC = 3;
        Int varD = 4;   
		
        Int operationResult = operation(varA, varB, varC, varD);
        Console.WriteLine("Result value: ", op_result);
	}

    // For partner A:
    // ret_val = ((a+b) * c)/d
    // For partner B:
    // ret_val = (a*c +  b*c)/d
    public Int operation(Int a, Int b, Int c, Int d) {
<<<<<<< HEAD (Current Change)
        Int result = (a*c +  b*c)/d;
=======
        Int result = (a*c +  b*c)/d;
>>>>>>> 9d32dca2134c25546c06c9e041549413ae722374 (Incoming Change)  
        return result;
    }
}


