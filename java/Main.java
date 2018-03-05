
public class Main{
    public static void main(String[] args){
		int i = 13;
		int j = 14;
		int k = sum(i,j);
        System.out.println("i + j = "+k);
		int l = 100;
		int m = loop(l);
		System.out.println(m);
    }
	public static int sum(int a, int b){
		int sum = a+b;
		int c = sum;
		return c;
	}
	public static int loop(int limit){
		for(int i = 0; i < 10000 ; i++){
			if(i>=limit){
				return i;
			}
		}
		return -1;
	}
	public static Object testRef(){
		Object o = new Object();
		System.out.println(o.toString());
		return o;
	}
}
