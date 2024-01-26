class BreakContinueExample{
    public static void main(String args[]){
        for (int i=0;i<=7;i++){
            if (i==5)
            continue;     //for continue  we use continue; in place of break;
            System.out.println(i);
        }
    }
}