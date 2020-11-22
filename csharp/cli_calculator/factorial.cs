using System;
using System.Globalization;
namespace idk{
	class MainClass{
		static void Main(){
			Console.Write("Zadejte první číslo (n): ");
			string n = Console.ReadLine();
			Console.Write("Zadejte druhé číslo (k): ");
			string k = Console.ReadLine();
			try{
				float nConverted = float.Parse(n, CultureInfo.InvariantCulture.NumberFormat);
				float kConverted = float.Parse(k, CultureInfo.InvariantCulture.NumberFormat);
				KombinacniCislo a = new KombinacniCislo(nConverted, kConverted);
				Console.WriteLine(a.getResult());
			}
			catch (System.FormatException){
				Console.WriteLine("Something fucked up and the conversion to a float is impossible.");
			}
		}
	}
	public class KombinacniCislo{
		// This is entirely useless
		float result;
		public KombinacniCislo(float n, float k){
			Faktorial fN = new Faktorial(n);
			Faktorial fK = new Faktorial(k);
			Faktorial fNK = new Faktorial(n - k);
			this.result = (fN.Calculate() / (fK.Calculate() * fNK.Calculate()));
			// this.result = 1;
		}
		public string getResult(){
			return this.result.ToString("R");
		}
	}
	public class Faktorial{
		// This class only has one function and calculates factorial of a given number in it
		float n;
		public Faktorial(float n){
			this.n = n;
		}
		public float Calculate(){
			float result = 1;
			while (this.n > 1){
				result = result * n;
				n -= 1;
			}
			return result;
		}
	}
}
