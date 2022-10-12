import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Solution {
	static int N, M, answer;
	static HashMap<Integer, ArrayList<Integer>> lowHeight, highHeight;
	static boolean[] lowChecked, highChecked;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int TC = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= TC; tc++) {
			N = Integer.parseInt(br.readLine());
			M = Integer.parseInt(br.readLine());
			
			lowHeight = new HashMap<>();
			highHeight = new HashMap<>();
			
			for (int i = 1; i < N+1; i++) {
				lowHeight.put(i, new ArrayList<>());
				highHeight.put(i, new ArrayList<>());
			}
			
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				lowHeight.get(b).add(a);
				highHeight.get(a).add(b);
			}
			
			answer = 0;
			
			for (int i = 1; i < N+1; i++) {
				lowChecked = new boolean[N+1];
				highChecked = new boolean[N+1];
				
				lowChecked[i] = true;
				highChecked[i] = true;
				
				answer += ((findLower(i) + findHigher(i)) == N-1) ? 1 : 0;
			}
			
			System.out.println("#" + tc + " " + answer);
		}
		
		
	}

	private static int findLower(int idx) {
		int cnt = 0;
		
		for (int newIdx : lowHeight.get(idx)) {
			if (!lowChecked[newIdx]) {
				lowChecked[newIdx] = true;
				cnt += 1 + findLower(newIdx);
			}
		}
		
		return cnt;
	}


	private static int findHigher(int idx) {
		int cnt = 0;
		
		for (int newIdx : highHeight.get(idx)) {
			if (!highChecked[newIdx]) {
				highChecked[newIdx] = true;
				cnt += 1 + findHigher(newIdx);
			}
		}
		
		return cnt;
	}
}
