/*interface Interface1 {
    void display();
}
interface Interface2{
    void printble();
}
class Child  implements Interface1 , Interface2{
    void display(){
        System.out.println("Display");
    }
    void printble(){
        System.out.println("Print");
    }
    public static void main(String []args){
        Child obj = new Child();
        obj.display();
        obj.printble();
    }
}*/


interface Printable
{
void print();
}
interface Showable
{
void show();
}
class A7 implements Printable,Showable
{
public void print()
{
System.out.println("Hello");
}
public void show()
{
System.out.println("Welcome");
}
public static void main(String args[])
{
A7 obj = new A7();
obj.print();
obj.show();
}
}