/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

 int factorial(int number){
        
        int result = 1;
        
        if (number < 1){
            
        }
        
        for (int i = number; i > 1; --i){
            result *= i;
        }
        
        return result;
    }

int factorial_rec(int number){
    
    if (number >= 1){
        return number * factorial_rec(number - 1);
    }else{
        return 1;
    }
    
}

int main(){
    
    int number;
    try{
        scanf("%d", &number);
        
    }catch{
        printf("You didn't enter a number, moron")
    }
    
    
    

    printf("%d\n", factorial());
    printf("%d\n", factorial_rec();
    
}

