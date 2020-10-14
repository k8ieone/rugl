using System;
using System.Globalization;
namespace Divider{
    class Divider{
        static void Main(){
            // Here we get the input
            Console.Write("Enter the number to test: ");
            string numberOne = Console.ReadLine();
            try{
            double numberOneConverted = float.Parse(numberOne, CultureInfo.InvariantCulture.NumberFormat);
            double numberOneWritable = float.Parse(numberOne, CultureInfo.InvariantCulture.NumberFormat);
            Console.WriteLine(numberOne + " can be divided by these numbers:");
            while (numberOneWritable > 0){
                if (numberOneConverted % numberOneWritable == 0){
                    Console.WriteLine(numberOneWritable.ToString("R") + " ");
                    }
                numberOneWritable -= 1;
                }
            }
            catch (System.FormatException){
                Console.WriteLine("One of the entered numbers was, in fact, not a number.");
                Console.WriteLine("Please try this again...");
                Environment.Exit(1);
            }
        }
    }
}