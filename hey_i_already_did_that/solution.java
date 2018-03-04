import java.awt.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class answer{
 
	    public static int answer(String n, int b) { 

	        // Your code goes here.
	        
			ArrayList<String> listFinal = new ArrayList();
			int l = listFinal.size();
			listFinal.add(n);
			int i, count = 0;
			int diff=0;
			int k = n.length();
			String z = "";
			while (count ==0) {
				
				ArrayList<String> digits = getDigits(n);
				ArrayList<String> listAsc = sortAsc(digits); // Sort in ascending order
		
				int yVal = Integer.parseInt(arraylist2String(digits), b); // Convert list to Int wrt base
		
				ArrayList<String> list = getDigits(n);
				ArrayList<String> listDes = sortDes(list); // Sort in descending order
			
				int xVal = Integer.parseInt(arraylist2String(listDes), b); // Convert list to Int wrt base
			
				String zVal = Integer.toString(xVal - yVal, b); // diff between x and y
				int zvalue = Integer.parseInt(zVal, b);
				z = Integer.toString(zvalue, b);

				if (z.length() < k) {
					z = String.format("%0" + k + "d", zvalue);
				
				}
				n = z;
			

				for (int j = 0; j < listFinal.size(); j++) {
					
					if (z.equals(listFinal.get(j))) {
						System.out.println(listFinal.size() - j);
						diff=listFinal.size() - j;
						count=1;	

					}
				
				}
				listFinal.add(z);

			}
			
		
			return diff;
	}
	
		public static ArrayList<String> getDigits(String num) {
			ArrayList<String> digits = new ArrayList<String>();
			collectDigits(num, digits);
			return digits;
			
		}

		private static void collectDigits(String num, ArrayList<String> digits) {
			int i;
			for (i = 0; i < num.length(); i++) {
				digits.add(Character.toString(num.charAt(i)));
			}

		}

		public static ArrayList<String> sortAsc(ArrayList<String> m) {
			Collections.sort(m);

			return (m);

		}

		public static ArrayList<String> sortDes(ArrayList<String> list) {
			Collections.sort(list);
			Collections.reverse(list);

			return (list);

		}


		public static String arraylist2String(ArrayList<String> list) {

			StringBuilder numString = new StringBuilder();
			int i;
			for (i = 0; i < list.size(); i++) {
				numString.append(list.get(i));

			}
			String result = numString.toString();
			return (result);
		}


	}
