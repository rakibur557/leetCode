class Solution {
  bool canMakeSubsequence(String str1, String str2) {
    int n1 = str1.length;
    int n2 = str2.length;
    int i = 0, j = 0;

    while (i < n1 && j < n2) {
      // Current characters of str1 and str2
      String char1 = str1[i];
      String char2 = str2[j];

      // Check if char1 can match char2 either directly or by incrementing cyclically
      if (char1 == char2 || String.fromCharCode((char1.codeUnitAt(0) - 97 + 1) % 26 + 97) == char2) {
        j++; // Move to the next character in str2 if a match is found
      }
      i++; // Always move to the next character in str1
    }

    // If we've matched all characters of str2, return true
    return j == n2;
  }
}
