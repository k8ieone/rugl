namespace Test{
    class MyApp{
        static void Main(){
            int stranaA, stranaB;
            stranaA = 5;
            stranaB = 10;
            if (stranaA == 0){
                System.Console.WriteLine("Strana A je 0!");
                System.Environment.Exit(1);
            }
            else if (stranaB == 0){
                System.Console.WriteLine("Strana B je 0!");
                System.Environment.Exit(2);
            }
            System.Console.WriteLine("Obvod je " + MyApp.calculateEdgesLength(stranaA, stranaB));
            System.Console.WriteLine("Obsah je " + MyApp.calculateSurfaceArea(stranaA, stranaB));
        }
        static int calculateSurfaceArea(int stranaA, int stranaB){
            return stranaA * stranaB;
        }
        static int calculateEdgesLength(int stranaA, int stranaB){
            return 2 * (stranaA + stranaB);
        }
    }
}