class Demo{
    public static void main(String args[])
    {
        Static void prime(n){
            for (int i=2;i<=n;i++){
            if (n==0||n==1){
            System.out.println("It is not a prime number.");
            }
            else if(n%i==0){
                System.out.println("It is a prime number.");
            }
            else{
                System.out.println("It is a Prime number");
            }
        }
    }
    prime(2);
}
}