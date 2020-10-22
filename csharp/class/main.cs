using System;
namespace ClassesTest{
    class MainClass{
        static void Main(){
            Truck car1 = new Truck();
            car1.Load(3000);
            car1.unLoad(500);
            Console.WriteLine(car1.currentLoad);
        }
    }
    public class Truck{
        public int currentLoad;
        public Truck(){
            currentLoad = 0;
        }
        public void Load(int kilograms){
            if (kilograms > 0){
                currentLoad += kilograms;
            }
        }
        public void unLoad(int kilograms){
            if (currentLoad - kilograms >= 0){
                currentLoad -= kilograms;
            }
        }
    }
}