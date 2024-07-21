import java.util.Scanner; 
public class SumOfTenNumbers{
	
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

		int number = 0;
		int sum = 0;
		
	for(number =1;number <= 10;number++){
		System.out.println("Enter number ");
		number = input.nextInt();

		sum = sum + number;
		}

		
	}

}		
