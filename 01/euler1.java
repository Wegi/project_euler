public class euler1 {

	public static void main(String[] args) {
		int counter = 0;
		for(int i=0; i<1000; i++) {
			if(isLegit(i))
				counter += i;
		}
		System.out.println("The Number you're searching is: " + counter);
	}
	
	private static boolean isLegit(int argument) {
		if((argument%3 == 0)||(argument % 5 == 0))
			return true;
		return false;
	}
}