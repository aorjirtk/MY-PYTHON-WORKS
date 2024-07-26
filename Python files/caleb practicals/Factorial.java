import java.util.Scanner; 
public class Factorial{
	
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		int numberFactorial = 0;

		System.out.print("Enter number ");
		int number = input.nextInt();

		while(number > 1){
		number = number - 1;
		numberFactorial = (number + 1) * number - 1;
		
	 	System.out.println(numberFactorial);
		}

	}

}