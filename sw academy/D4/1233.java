package com.day0809;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class SWEA1233 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int tc = 1; tc <= 10; tc++) {
			int N = Integer.parseInt(br.readLine());
			int result = 1;

			for (int i = 0; i < N; i++) {
				String[] s = br.readLine().split(" ");
				if (result == 0) continue;

				if (s.length == 4) { // 4개인 경우
					if (s[1].equals("+") || s[1].equals("-") || s[1].equals("*") || s[1].equals("/"))
						continue;
					result = 0;
				}

				else if (s[1].equals("+") || s[1].equals("-") || s[1].equals("*") || s[1].equals("/")) {
					result = 0;
				}
			}
			System.out.printf("#%d %d%n", tc, result);
		}

	}

}

//package com.day0809;
//
//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.util.StringTokenizer;
//
//public class SWEA1233 {
//
//	public static void main(String[] args) throws Exception {
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st;
//		
//		for (int tc = 1; tc <= 10; tc++) {
//			int N = Integer.parseInt(br.readLine());
//			int result = 1;
//			
//			for (int i = 0; i < N; i++) {
//				st = new StringTokenizer(br.readLine());
//				st.nextToken();
//				char c = st.nextToken().charAt(0);
//				
//				if(st.hasMoreTokens()) { // 4개인 경우
//    				if(c >= '0' && c <= '9')  // 숫자인 경우
//    					result = 0;
//    			}
//    			else { // 2개인 경우
//    				if(c < '0' || c > '9')  // 문자인 경우
//    					result = 0;
//    			}
//			}
//			System.out.printf("#%d %d%n", tc, result);
//			
//		}
//		
//	}
//
//}
