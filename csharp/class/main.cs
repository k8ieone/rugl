using System;
namespace ClassesTest{
    class MainClass{
        static void Main(){
            Cat cat1 = new Cat("Victoria");
            Cat cat2 = new Cat("Ellie");
            Cat cat3 = new Cat();
            cat1.sayMeow();
            cat2.sayMeow();
            cat3.sayMeow();
            }
        }
    public class Cat{
        public void sayMeow(){
            Console.WriteLine(self.catName + ": Meow");
        }
        public Cat(){
            catName = "unnamed";
        }
        public Cat(string name){
            catName = name;
        }
        public string Name { get; }
    }
}