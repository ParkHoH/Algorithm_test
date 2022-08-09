package com.day0809;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Backjoon2563 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st;
		int[][] graph = new int[101][101];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int startX =  Integer.parseInt(st.nextToken());
			int startY = Integer.parseInt(st.nextToken());
			
			for (int x = startX; x < startX + 10; x++) {
				for (int y = startY; y < startY + 10; y++) 
					graph[x][y] = 1;
			}
		}
		
		int result = 0;
		
		for (int x = 0; x < 101; x++) {
			for (int y = 0; y < 101; y++) {
				if (graph[x][y] == 1)
					result++;
			}
		}
		System.out.println(result);
	}
}
