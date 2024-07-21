import java.util.Scanner; 
public class Practice{
	
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.print("Enter constant number ");
		int constantNumber = input.nextInt();

		int number = 0;
		int sum = 0;
		
		
	while(sum <= constantNumber){
		System.out.print("Enter Integer ");
		number = input.nextInt();
		
		sum = sum + number;
		}

		System.out.print("Sum of integers is "+sum);
	}
	

}