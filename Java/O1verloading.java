class Overloading {
    /*int add(int a,int b){
        return a+b;
    }
    int add(int a,int b,int c){
        return a+b+c;
    }

    public static void main(String []args)
    {
        Overloading s=new Overloading();
        System.out.println(s.add(2,5));
        System.out.println(s.add(2,5,8));
    }
}*/


    Overloading(int a, int b) {
     return a+b;
         
    }

    Overloading(int a, int b, int c) {
        return a+b+c;
    }

    public static void main(String[] args) {
        Overloading s = new Overloading();
        System.out.println(s.Overloading(2, 5));
        System.out.println(s.Overloading(2, 5, 8));
    }
}






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