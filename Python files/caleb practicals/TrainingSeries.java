import java.util.Scanner;

public class LargestAndSmallest{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		
		int smallest = 0;
		int largest = 0;
		CharAt stopper = 'n' 

	while(stopper != 'n'){
		System.out.println("Enter number");
		int number = input.nextInt();
		largest = number > largest;

		}
		System.out.println(largest);



}

}