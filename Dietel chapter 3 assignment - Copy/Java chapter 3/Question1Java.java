import java.util.Scanner;
public class Question1Java{

	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

	int userInput = 0;
	int counter = 0;
	int flagValue = 0;
	while(flagValue != 1 && flagValue != 2){
		System.out.print("Enter the number: ");
		userInput = input.nextInt();
		if (userInput == 1 || userInput ==2)
			break;
		counter += 1; 
				
		}
	System.out.print("The number of failed attempts is "+counter);
	

	}

}