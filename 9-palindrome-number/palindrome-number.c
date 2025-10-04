bool isPalindrome(int x) {
    if (x < 0) return false;

    char numStr[12];
    sprintf(numStr, "%d", x);

    int len = strlen(numStr);
    
    for (int i = 0; i < len / 2; i++) {
        if (numStr[i] != numStr[len - i - 1]) {
            return false;
        }
    }

    return true;
}