import java.util.Scanner;
public class Question3Java8{

	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		int product = 1;
		double total = 0;
		int largestNumber = 0;
		int smallestNumber = 0;
		double average = 0;
		int counter = 0;

		for(counter = 1; counter <= 4; counter++){

		System.out.print("Enter the three integers: ");
		int userInput = input.nextInt();
			if(largestNumber < userInput){
			largestNumber = userInput;
				}

			if(smallestNumber == 0 || userInput < smallestNumber){
			smallestNumber = userInput;
				}
			
			total= total + userInput;
			product= product * userInput;
			average = total/counter;
		}
		//average = total/counter;
		System.out.println("the sum of integers is "+ total);

		System.out.println("the product of the integers is "+product);

		System.out.println("the smallest integers is "+smallestNumber);
		
		System.out.println("the largest integers is "+ largestNumber);

		System.out.println("the average of  the integers is "+ average);
	}


}

		