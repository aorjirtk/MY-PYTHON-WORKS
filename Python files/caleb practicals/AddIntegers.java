import java.util.Scanner; 
public class AddIntegers{
	
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

		int number = 0;
		int numberPositive = 0;
		int numberZero = 0;
		int numberNegative = 0;

		
	while(number != 101){
		
		System.out.print("Enter Integers or 101 to stop: ");
		number = input.nextInt();

		if(number < 0 ){
		numberNegative++;

		}else if(number > 0 ){
		numberPositive++;

		} else{
		numberZero++;

		}
			
		}

		System.out.println("zero are "+ numberZero);
		System.out.println("negative numbers are "+ numberNegative);
		System.out.println("positive numbers are "+ numberPositive);

	}
}