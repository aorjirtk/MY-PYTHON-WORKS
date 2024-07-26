import java.util.Scanner; 
public class PracticeBook{
	
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		
		int counter = 1;
		double average = 0;
		int grade = 0;
		int sum = 0;


	while(counter <= 10){
		counter = counter +1;
		System.out.print("Enter grade");
		grade = input.nextInt();
		

		sum = sum + grade;

}
		System.out.println("sum is "+sum);

 		average = sum / counter;
		System.out.println("average is "+average);

	}
}