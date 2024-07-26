import java.util.Scanner;
public class Question3Java10{

	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	double principal = 1000;
	double annualRate = 7/100;
	double amountOnDeposit = 0;
	for(int numberOfYears = 1; numberOfYears <= 30; numberOfYears++){

	amountOnDeposit = principal * Math.pow(1.07,numberOfYears);

	System.out.println("At the end of "+numberOfYears+ "years, the amount on deposit is "+amountOnDeposit);

		}

	}

}