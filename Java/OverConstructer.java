public class OverConstructer {
    int id;
    String name;
    int age;
}
OverConstructer(int i,String n){
    id=i;
    name=n;
    //System.out.println(id+""+name);
}
OverConstructer(int i, String n,int a){
    id=i;
    name=n;
    age=a;}
void display(){
    System.out.println(id+""+name+""+age);
}
public static void main(String []args){
    OverConstructer obj=new OverConstructer(5,"chinnu",51);
    obj.display();
}
}
