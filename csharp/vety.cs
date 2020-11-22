using System;
namespace Sentences{
	class MainClass{
		static void Main(){
			Adjective a = new Adjective();
			Noun n = new Noun();
			Adverb av = new Adverb();
			Verb v = new Verb();
			Adverb2 av2 = new Adverb2();
			for (int i = 0; i < 10; i++) {
				Console.WriteLine(makeSentence(a.pickOne(), n.pickOne(), av.pickOne(), v.pickOne(), av2.pickOne()));
			}
		}
		static string makeSentence(string adjective, string who, string how, string what, string whereA){
			return (adjective + " " + who + " " + how + " " + what + " " + whereA);
		}
	}
	public class Adjective{
		string[] adjectives = { "Starý", "Ostřílený", "Velký", "Hubený", "Automatizovaný", "Nejlepší" };
		public Adjective(){
			
		}
		public string pickOne(){
			Random random = new Random();
			return (this.adjectives[random.Next(0, this.adjectives.Length)]);
		}
	}
	public class Noun{
		string[] nouns = { "programátor", "farmář", "učitel", "filmař", "doktor", "kamarád" };
		public Noun(){
			
		}
		public string pickOne(){
			Random random = new Random();
			return (this.nouns[random.Next(0, this.nouns.Length)]);
		}
	}
	public class Adverb{
		string[] adverbs = { "s oblibou", "znechuceně", "nadšeně", "rychle", "hodně", "málo" };
		public Adverb(){
			
		}
		public string pickOne(){
			Random random = new Random();
			return (this.adverbs[random.Next(0, this.adverbs.Length)]);
		}
	}
	public class Verb{
		string[] verbs = { "spal", "programoval", "umíral", "jedl", "klikal", "kontroloval" };
		public Verb(){
			
		}
		public string pickOne(){
			Random random = new Random();
			return (this.verbs[random.Next(0, this.verbs.Length)]);
		}
	}
	public class Adverb2{
		string[] adverbs = { "na zahradě", "u babičky", "doma", "venku", "v koupelně", "na záchodě" };
		public Adverb2(){
			
		}
		public string pickOne(){
			Random random = new Random();
			return (this.adverbs[random.Next(0, this.adverbs.Length)]);
		}
	}
}
