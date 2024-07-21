import java.util.Scanner; 
public class NumberRaisedToPower{
	
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

		
		int a = 0;
		int counter = 0;
		int b =  a;
		int result = 0;
		
	for(counter = 1;counter < 5;counter++){
		
		System.out.print("Enter first integer ");
		int a = input.nextInt();

		System.out.print("Enter second integer ");
		int b = input.nextInt();


		result *= a ;
	

		System.out.println(result);
}
	}

}		
