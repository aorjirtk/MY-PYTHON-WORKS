import java.util.Scanner;
public class Question3Java13{

	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

System.out.print("Enter the number ");
	int number = input.nextInt();

	int factors=1;
	int counter = 1;

	for(counter = 1; counter <= number; counter++){
		factors=factors*counter;

		}

	System.out.print(factors);
	}

}

