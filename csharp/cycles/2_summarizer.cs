using System;
using System.Globalization;
namespace Summarizer{
    class Summarizer{
        static void Main(){
            Console.WriteLine("Enter numbers to summarize. Enter 0 to print the result.");
            while (true){
                Whatever();
            }
        }
        // I had to make a new function, because Main() can't have arguments
        static void Whatever(double sum = 0){
            Console.Write("number: ");
            string enteredNumber = Console.ReadLine();
            if (enteredNumber == "0"){
                Console.WriteLine("The sum is: " + sum.ToString("R"));
                Environment.Exit(0);
            }
            try{
                double testingIfTheNumberIsANumber = float.Parse(enteredNumber, CultureInfo.InvariantCulture.NumberFormat);
            }
            catch (System.FormatException){
            Console.WriteLine("One of the entered numbers was, in fact, not a number.");
            Console.WriteLine("Please try this again...");
            Whatever(sum);
            }
            double enteredNumberConverted = float.Parse(enteredNumber, CultureInfo.InvariantCulture.NumberFormat);
            sum += enteredNumberConverted;
        }
    }
}
