#include<stdio.h>
int main() {
	int num;
	printf("Enter a Number : ");
	scanf("%d",&num);
	fact(num);
	int fact(num){
		for (int i=1; i >= num; i++){
			num = num*i;
		}
		printf("%d",num);
	}
	
}