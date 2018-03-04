package com.google.challenges; 
import java.util.*;
import java.util.ArrayList;
import static java.lang.Math.sqrt;
import static java.lang.Math.floor;

public class Answer {   
    public static int[] answer(int area) { 

        // Your code goes here
        int N, nFloor=0, diff;
		double n=0;
		N=area;
		diff=area;
		ArrayList list = new ArrayList();
		while(diff!=0) {
			n=Math.sqrt(N);
			nFloor = (int)Math.floor(n);
			diff = N - (nFloor*nFloor);
			list.add(nFloor*nFloor);
		
			N=diff;
		}
		int[] ans = new int[list.size()];



	    for (int i = 0; i < list.size() ; i++)
		
			ans[i] = (int)list.get(i);
			
	return ans;
	
   
    } 
}
