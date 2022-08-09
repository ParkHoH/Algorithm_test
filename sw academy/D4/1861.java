package com.day0809;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA1861 {
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int cnt;
	
	public static void dfs(int x, int y, int N, int[][] graph)	{
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if (nx >= N || ny >= N || nx < 0 || ny < 0) 
				continue;
			
			if (graph[x][y] + 1 == graph[nx][ny]) {
				cnt++;
				dfs(nx, ny, N, graph);
			}
			
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int TC = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= TC; tc++) {
			int N = Integer.parseInt(br.readLine());
			int[][] graph = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) 
					graph[i][j] = Integer.parseInt(st.nextToken());
			}

			int[] result = {0, 0};
			
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					cnt = 1;
					dfs(i, j, N, graph);
					
					if (cnt > result[1]) {
						result[0] = graph[i][j];
						result[1] = cnt;
					} else if (cnt == result[1]) 
						result[0] = Math.min(result[0], graph[i][j]);
				}
			}
			System.out.printf("#%d %d %d%n", tc, result[0], result[1]);
		}
		
	}
}
