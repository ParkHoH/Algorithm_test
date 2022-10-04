import java.awt.Point;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
	static int[][] board;
	static ArrayList<Point> zero;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		board = new int[9][9];
		zero = new ArrayList<>();
		
		for (int i = 0; i < 9; i++) {
			String s = br.readLine();
			for (int j = 0; j < 9; j++) {
				board[i][j] = s.charAt(j) - '0';
				if (board[i][j] == 0) zero.add(new Point(i, j));
			}
		}
		
		dfs(0);
		
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++)
				System.out.print(board[i][j]);
			System.out.println();
		}
	}

	private static boolean dfs(int cnt) {
		if (cnt == zero.size())	return true;
		Point p = zero.get(cnt);
		
		for (int num = 1; num < 10; num++) {
			if (checkRow(p.x, num) && checkColumn(p.y, num) && checkRect(p.x, p.y, num)) {
				board[p.x][p.y] = num;
				if (dfs(cnt+1)) return true;
				board[p.x][p.y] = 0;
			}
		}
		
		return false;
	}

	private static boolean checkRect(int x, int y, int num) {
		int modX = x / 3;
		int modY = y / 3;
		
		for (int i = 3*modX; i < 3*modX + 3; i++) {
			for (int j = 3*modY; j < 3*modY + 3; j++)
				if (board[i][j] == num) return false;
		}
		
		return true;
	}

	private static boolean checkColumn(int y, int num) {
		for (int i = 0; i < 9; i++)
			if (board[i][y] == num) return false;
		
		return true;
	}

	private static boolean checkRow(int x, int num) {
		for (int i = 0; i < 9; i++)
			if (board[x][i] == num) return false;
		
		return true;
	}
}
