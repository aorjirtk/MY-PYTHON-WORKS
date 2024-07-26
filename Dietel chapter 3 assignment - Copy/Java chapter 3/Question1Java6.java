import java.util.Scanner;
public class Question1Java6{

	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

		System.out.print("What is your problem: ");
		String problem = input.nextLine();

		if(problem == problem){
		System.out.print("have you had this problem before(Yes or No): ");
		String response = input.nextLine();

			if(response.equals ("Yes")){
			System.out.print(" well, you have it again ");
			}
			if(response.equals ("No")){
			System.out.print(" well, you have it now ");
			}
		}
		
	}

}
