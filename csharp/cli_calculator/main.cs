using System;
using System.Globalization;
namespace Calculator{
    class Calculator{
        static void Main(){
            // Here we get the input
            Console.Write("Enter the first number: ");
            string numberOne = Console.ReadLine();
            Console.WriteLine("Available operations: +, -, *, /");
            Console.Write("Enter the operation: ");
            string operation = Console.ReadLine();
            Console.Write("Enter the second number: ");
            string numberTwo = Console.ReadLine();

            // Here we determine what operation to perform
            switch(operation){
                case "+":
                    Console.WriteLine(Add(numberOne, numberTwo));
                    break;
                case "-":
                    Console.WriteLine(Subtract(numberOne, numberTwo));
                    break;
                case "*":
                    Console.WriteLine(Multiply(numberOne, numberTwo));
                    break;
                case "/":
                    Console.WriteLine(Divide(numberOne, numberTwo));
                    break;
                default:
                    Console.WriteLine("Invalid operation!");
                    Environment.Exit(1);
                    break;
            }
        }
        static string Add(string numberOne, string numberTwo){
            try{
                // Variables from the "try" block are not available outside?????
                double numberOneConverted = float.Parse(numberOne, CultureInfo.InvariantCulture.NumberFormat);
                double numberTwoConverted = float.Parse(numberTwo, CultureInfo.InvariantCulture.NumberFormat);
                // That's why everything is done in the "try" block... stoopid!!!
                double result = (numberOneConverted + numberTwoConverted);
                return result.ToString("R");
            }
            catch (System.FormatException){
                Console.WriteLine("One of the entered numbers was, in fact, not a number.");
                Console.WriteLine("Please try this again...");
                Environment.Exit(1);
            }
            // This needs to be here for the thing to compile, even tho it never gets executed...
            return "error";
        }
        // The following 2 functions are just copy-pastes of the Add function...
        static string Subtract(string numberOne, string numberTwo){
            try{
                double numberOneConverted = float.Parse(numberOne, CultureInfo.InvariantCulture.NumberFormat);
                double numberTwoConverted = float.Parse(numberTwo, CultureInfo.InvariantCulture.NumberFormat);
                double result = (numberOneConverted - numberTwoConverted);
                return result.ToString("R");
            }
            catch (System.FormatException){
                Console.WriteLine("One of the entered numbers was, in fact, not a number.");
                Console.WriteLine("Please try this again...");
                Environment.Exit(1);
            }
            return "error";
        }
        static string Multiply(string numberOne, string numberTwo){
            try{
                double numberOneConverted = float.Parse(numberOne, CultureInfo.InvariantCulture.NumberFormat);
                double numberTwoConverted = float.Parse(numberTwo, CultureInfo.InvariantCulture.NumberFormat);
                double result = (numberOneConverted * numberTwoConverted);
                return result.ToString("R");
            }
            catch (System.FormatException){
                Console.WriteLine("One of the entered numbers was, in fact, not a number.");
                Console.WriteLine("Please try this again...");
                Environment.Exit(1);
            }
            return "error";
        }
        static string Divide(string numberOne, string numberTwo){
            try{
                double numberOneConverted = float.Parse(numberOne, CultureInfo.InvariantCulture.NumberFormat);
                double numberTwoConverted = float.Parse(numberTwo, CultureInfo.InvariantCulture.NumberFormat);
                double result = (numberOneConverted / numberTwoConverted);
                return ("Result: " + result.ToString("R"));
            }
            catch (System.FormatException){
                Console.WriteLine("One of the entered numbers was, in fact, not a number.");
                Console.WriteLine("Please try this again...");
                Environment.Exit(1);
            }
            return "error";
        }
    }
}