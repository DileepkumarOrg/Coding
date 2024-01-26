//Auto boxing
class Auto_Boxing_Un_Boxing{
    public static void main(String args[]){
        int a=25;   
        Integer b=Integer.valueOf(a);
        System.out.println(a+" "+b);
        System.out.println(typeOf (b));
        Double c=Double.valueOf(a);
        System.out.println(a+" "+c);
        System.out.println(typeOf (c));
        short x= 546;
        String y= String.valueOf(x);
        System.out.println(x+" "+y);
        System.out.println(typeOf(c));
        System.out.println("Staring of Unboxing:");




        Integer p=56;
        int q= p.intValue();
        int r= p;
        System.out.println(p+" "+q+" "+r );
    }
    private static String typeOf(Object object) {
        return object.getClass().getName();
    }
}