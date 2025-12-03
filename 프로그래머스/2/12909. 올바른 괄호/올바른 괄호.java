class Solution {
    boolean solution(String s) {
        
        char[] data = s.toCharArray();
        char[] stack = new char[100000];
        int top = -1;

        for (char d: data) {
            if (d == '(') stack[++top] = d;
            else {
                if (top == -1) return false;
                if (stack[top] != '(') return false;
                top--;
            }
        }

        return top == -1;
    }
}