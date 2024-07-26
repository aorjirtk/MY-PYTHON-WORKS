
import java.util.Scanner;
public class Question3Java12{

	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	System.out.print("Enter the five digit integer: ");
	int number = input.nextInt();

	int lastDigit = number % 10;

	int firstDigit = number / 10000;

	int fourthDigit = (number / 10) % 10;

	int secondDigit = (number / 1000) % 10;

	int thirdDigit = (number / 100) % 10;
 

	if(firstDigit == lastDigit && secondDigit == fourthDigit){
	System.out.print(number+ " is a palindrome");

	}else
		System.out.print(number+ " is Not a palindrome");

	}

}