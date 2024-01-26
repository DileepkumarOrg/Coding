class Animal{
    String color=black;
    }
class Dog extends Animal{
    String color=white;

void display(){
    System.out.println(color);
    System.out.println(super.color);
}}
class TestThis
{
public static void main(String args[])
{
Dog s1=new Dog(); 
s1.display();
}}
