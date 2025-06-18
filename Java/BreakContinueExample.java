class BreakContinueExample{
    public static void main(String args[]){
        for (int i=0;i<=7;i++){
            if (i==5){
                continue;     //for continue  we use continue; in place of break; 
            }
            System.out.println(i);
        }
    }
}

/*
    for continue output : 0 1 2 3 4 6 7,
    for break output : 0 1 2 3 4,
*/


