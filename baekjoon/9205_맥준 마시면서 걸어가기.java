package com.day1006;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Backjoon9205 {
	static int N;
	
	static Point home, festival;
	static Point[] conv;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int TC = Integer.parseInt(br.readLine());
		
		while (TC-- > 0) {
			N = Integer.parseInt(br.readLine());
			conv = new Point[N];
			
			st = new StringTokenizer(br.readLine());
			home = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				conv[i] = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
			}
				
			st = new StringTokenizer(br.readLine());
			festival = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
			
			System.out.println(bfs());
		}
		
	}

	private static String bfs() {
		boolean[] visited = new boolean[N];
		Queue<Point> queue = new ArrayDeque<>();
		
		queue.add(home);
		
		while (!queue.isEmpty()) {
			Point cur = queue.poll();
			
			if (Math.abs(cur.x - festival.x) + Math.abs(cur.y - festival.y) <= 1000)
				return "happy";
			
			for (int i = 0; i < N; i++) {
				if (!visited[i] && (Math.abs(cur.x - conv[i].x) + Math.abs(cur.y - conv[i].y) <= 1000)) {
					visited[i] = true;
					queue.add(conv[i]);
				}
			}
		}
		
		return "sad";
	}
}
