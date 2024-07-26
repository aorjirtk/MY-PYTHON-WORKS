import java.util.Scanner;
public class Question3Java9{

	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

System.out.print("Enter the five digit number ");
	int number = input.nextInt();

	int firstDigit = number / 10000;

	int secondDigit = number / 1000 % 10;

	int thirdDigit = number / 100 % 10;

	int fourthDigit = number / 10 % 10;

	int lastDigit = number % 10;

	int counter = 0;
	for(counter= 1; counter < 2; counter++){
		System.out.println(firstDigit);
		System.out.println(secondDigit);
		System.out.println(thirdDigit);
		System.out.println(fourthDigit);
		System.out.println(lastDigit);

		}
	}

}
