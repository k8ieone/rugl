using System;
namespace ClassesTest{
    class MainClass{
        static void Main(){
            Cat cat1 = new Cat("Victoria");
            Cat cat2 = new Cat("Ellie");
            Cat cat3 = new Cat();
            cat1.sayMeow(cat1.catName);
            cat2.sayMeow(cat2.catName);
            cat3.sayMeow(cat3.catName);
            }
        }
    public class Cat{
        public void sayMeow(string name){
            Console.WriteLine(name + ": Meow");
        }
        public Cat(){
            catName = "unnamed";
        }
        public Cat(string name){
            catName = name;
        }
        public string catName { get; }
    }
}