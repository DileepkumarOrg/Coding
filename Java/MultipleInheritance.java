class Animal{
    void eat(){
        System.out.println("Eating....");
    }
}
class Dog extends Animal{
    void barking(){
        System.out.println("Barking....");
    }
}
class BabyDog extends Dog{
    void weeping(){
        System.out.println("Weeping....");
    }
}

public class MultipleInheritance {
    public static void main(String []args){
        BabyDog obj=new BabyDog();
        System.out.println(" ");
        obj.weeping();
        System.out.println(" ");
        obj.barking();
        System.out.println(" ");
        obj.eat();
        System.out.println(" ");
    }
}