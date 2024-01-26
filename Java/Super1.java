class Super1{
	void display(){
		System.out.println("Eating.....");
	}
}
class Nature extends Super1{
	void display(){
		System.out.println("Thinking.....");
	}
}
class Test{
public static void main(String []args){
Nature obj=new Nature();
obj.display();
obj.super.display();
	}
}