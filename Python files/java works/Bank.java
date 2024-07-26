import java.util.Scanner;
public class Bank{

	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		double flagValue = -1;
		double userInput = 0;
		double netAmount = 0;
		
		while(userInput != flagValue){
		if(userInput < -2)System.out.print("invalid input");

		System.out.println("Enter\n 1 to deposit \n 2 to withdraw \n -1 to End: ");
		userInput = input.nextInt();
		if(userInput == 1){
		System.out.print("Enter amount to deposit ");
		double deposit = input.nextInt();
		netAmount= netAmount + deposit;
		if(deposit < 0){
		System.out.println("invalid amount");
		}else
		System.out.println("deposit successful");
		
		}
		if(userInput == 2){
		System.out.print("Enter amount to withdraw ");
		double withdraw = input.nextInt();
		if(withdraw > netAmount || withdraw < 0){
		System.out.println("invalid amount");
		}else
		netAmount= netAmount - withdraw;

		}


		}
		if(netAmount < 0){
		System.out.println("invalid amount");
		}else
	System.out.print("Your account balance is "+netAmount);

	}

}