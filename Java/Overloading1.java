class Adder{
	int add(int a,int b)
	{
		return a+b;
	}
	double add(double a,double b)
	{
		return a+b;
	}
}
class Overloading1{
public static void main(String []args){
	Adder obj=new Adder();
	System.out.println(obj.add(2,3));
	System.out.println(obj.add(2.33,5.66));	
	}

}