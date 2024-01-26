public class PrimitiveDataTypesExample {
    public static void main(String[] args) {
        int a=3;
        Integer b= Integer.valueOf(a);
        System.out.println(a+" "+b);
        Integer c=9;
        int d=c.intValue();
        System.out.println(c+" "+d);
 
 
 
 
        /*Integer a=5;    
        int i=a.intValue();                                     //converting Integer to int explicitly  
        int j=a;                                                //unboxing, now compiler will write a.intValue() internally    
    
        System.out.println(a+" "+i+" "+j);*/ 

    }
}
