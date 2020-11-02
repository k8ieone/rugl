using System;
namespace ClassesTest{
    class MainClass{
        static void Main(){
            Trojuhelnik t1 = new Trojuhelnik(30, 15);
            Console.WriteLine(Trojuhelnik.getStrana().ToString());
        }
    }
    public class Trojuhelnik{
        int strana;
        int vyska;
        public Trojuhelnik(int strana, int vyska){
            this.strana = strana;
            this.vyska = vyska;
        }
        // error CS0120: An object reference is required for the non-static field, method, or property 'Trojuhelnik.getStrana()'
        // Jsem kompletně ztracen
        public int getStrana(){
            return this.strana;
        }
        public int getVyska(){
            return this.vyska;
        }
        public int getObsah(){
            return ((this.strana * this.vyska) / 2);
        }
        public override string ToString(){
            return ("Jsem trojuhelník a toto jsou mé parametry: [ výška: " + this.vyska.ToString() + " strana: " + this.strana.ToString() + " ]");
        }
    }
}