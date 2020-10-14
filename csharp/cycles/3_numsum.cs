using System;
using System.Globalization;
namespace NumSum{
    class NumSum{
        static void Main(){
            Console.Write("Enter a number (ints only): ");
            string enteredNumber = Console.ReadLine();
            try{
                int testingIfThisIsANumber = int.Parse(enteredNumber, CultureInfo.InvariantCulture.NumberFormat);
            }
            catch (System.FormatException){
                Console.WriteLine("One of the entered numbers was, in fact, not an integer.");
                Console.WriteLine("Please try this again...");
                Environment.Exit(1);
            }
            double sum = 0;
            foreach (char digit in enteredNumber){
                sum += char.GetNumericValue(digit);
            }
            Console.WriteLine("Sum of all entered digits is: " + sum.ToString("R"));
        }
    }
}