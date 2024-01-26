class Overloading
{
    Overloading(int a, int b)
    {
        System.out.println(a+b);
    }
    Overloading(int a,int b,int c)
    {
        System.out.println(a+b+c);
    }
    public static void main(String []args)
    {
        Overloading s= new Overloading(5,4);
        Overloading s1= new Overloading(4,5,6);
    }
}