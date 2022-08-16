package com.day0816;

import java.util.Scanner;

public class Backjoon1074 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int r = sc.nextInt();
		int c = sc.nextInt();
		
		int num = (int) Math.pow(2, N);
		int cnt = 0;
		
		// 1사분면으로 땡겨주는 작업 반복
		while (N != 0) {
			N -= 1;
			num /= 2;
			
			// 2사분면
			if (r < num && c >= num) {
				cnt += num * num;
				c -= num;
			}
			
			// 3사분면
			else if (r >= num && c < num) {
				cnt += num * num * 2;
				r -= num;
			}
			
			// 4사분면
			else if (r >= num && c >= num) {
				cnt += num * num * 3;
				r -= num;
				c -= num;
			}
		}
		System.out.println(cnt);
	}
	
}