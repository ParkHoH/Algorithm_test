class Solution {
    public boolean solution(int x) {
        String[] splited_x = String.valueOf(x).split(""); // Integer.toString(x).split(""); 도 가능함
        int sum = 0;
        for (String s : splited_x) {
            sum += Integer.parseInt(s);
        }
        
        if (x % sum == 0) {
            return true;
        } else {
            return false;
        }
    }
}