import java.util.Scanner; 
public class TabularOutput{
	
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		
		int N2 = 0;
		int N3 = 0;
		int N4 = 0;
	for(int N = 1; N<=5; N++){
		System.out.printf("%d%10d%10d%10d%n", N, (N*N), (N*N*N), (N*N*N*N));

		//N2 = N * N;
	//	System.out.println(N2);

		//N3 = N * N * N;
	//	System.out.println(N3);

		//N4 = N * N * N * N;
		

		//System.out.printf("%N\tN2\tN3\tN4%n");
		}
		

	}

}