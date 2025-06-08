#include <stdio.h>

int main(){
    int n1=0,n2=1,n3,n;
    printf("Enter number of fibanocci: ");
    scanf("%d",&n);
    if (n<=2){
        printf("%d,%d,",n1,n2);
    }
    else{
        printf("%d,%d,",n1,n2);
        for (int i=0;i<(n-2);i++){
            n3=n1+n2;
            n1=n2;
            n2=n3;
            printf("%d, ",n3);
        }
    }
}
// Output: Enter number of fibanocci: 5