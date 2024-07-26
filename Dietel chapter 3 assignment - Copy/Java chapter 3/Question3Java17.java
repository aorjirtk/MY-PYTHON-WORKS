
public class Question3Java17{

	public static void main(String[] args){
	int row = 0;
	int column = 0;
	
	for(row =1; row < 10; row++){
		for(column =10;column > row; column--){
	
		System.out.print("*"+"");
		}
	System.out.println();


		}

	for(row =1; row > 10; row++){
		for(column =10;row < 10; column--){
	
		System.out.print(""+"*");
		}
	System.out.println();

		}
	}

}
