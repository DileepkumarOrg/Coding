public class Variables {
    static int a=5;           //static variable
    int x=50;                 //Instance variable
    void display(){
        int b=7;                //local variable
        System.out.println(b);
    }
    public static void main(String[] args){
        int c=9;                //local varible
        Variables obj1=new Variables();     //Creating object
        obj1.display();                     //Accessing method by using object
        System.out.println(a+" "+obj1.x+" "+c);

        }
    }
