package com.day0809;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA6808 {
	static boolean[] isSelected;
	static int[] guyoung;
	static int[] inyoung;
	static int[] cards;
	static int cntWin;
	static int cntLose;

	public static void permu(int cnt) {
		if (cnt == 9) {
			int scoreGuyoung = 0, scoreInyoung = 0;

			for (int i = 0; i < 9; i++) {
				int score = guyoung[i] + inyoung[i];

				if (guyoung[i] > inyoung[i])
					scoreGuyoung += score;
				else
					scoreInyoung += score;
			}

			if (scoreGuyoung > scoreInyoung)
				cntWin++;
			else if (scoreGuyoung < scoreInyoung)
				cntLose++;

			return;
		}

		for (int i = 0; i < 9; i++) {
			if (isSelected[i])
				continue;
			
			inyoung[cnt] = cards[i];
			isSelected[i] = true;
			permu(cnt + 1);
			isSelected[i] = false;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= TC; tc++) {
			isSelected = new boolean[9];
			guyoung = new int[9];
			inyoung = new int[9];
			cards = new int[9];
			cntWin = cntLose = 0;
			boolean[] used = new boolean[18];
			StringTokenizer st = new StringTokenizer(br.readLine());

			for (int i = 0; i < 9; i++) {
				guyoung[i] = Integer.parseInt(st.nextToken());
				used[guyoung[i] - 1] = true;
			}

			int idx = 0;
			for (int i = 0; i < 18; i++) {
				if (!used[i])
					cards[idx++] = i + 1;
			}

			permu(0);

			System.out.printf("#%d %d %d%n", tc, cntWin, cntLose);
		}

	}

}
