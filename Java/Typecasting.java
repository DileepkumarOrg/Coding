class Typecasting{
    public static void main(String args[]){
        int a = 5;
        double b = a;
        double c= 10.526;
        int d = (int)c;
        System.out.println(a+"  "+b+" "+c+" "+d);
        //System.out.println(typeOf (a));
        System.out.println(typeOf (b));
        System.out.println(typeOf (c));
        System.out.println(typeOf (d));
        System.out.println("--------------");
        int e=5;
        String f=String.valueOf(e);
        System.out.println(f);
        System.out.println(f+"   "+typeOf (f));
    }
    public static String typeOf(Object object) {
        return object.getClass().getName();



    }
}