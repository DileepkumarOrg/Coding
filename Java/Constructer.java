class Constructer{
	int id;
	String name;
	Constructer(int i,String na){
		id = i;
		name = na;
		//System.out.println("Id is :"+id+"Name: "+na);
		
	}
	void display()
	{
	System.out.println(id+" "+name);
	}

	public static void main(String args[])
	{
		Constructer s1 = new Constructer(56,"Dileep");
		Constructer s2 = new Constructer(52,"dileep");
		s1.display();
		s2.display();
	}
}