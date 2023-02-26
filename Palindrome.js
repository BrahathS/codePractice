/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  // given the string s, return the longest palindromic substring in s
  // "abba" -> "abba"
  // "abb" -> "bb"
  // "cbbd" -> "bb"

  if (s.length <= 1) {
    return s;
  }
  let longest = "";
  let max = 0;
  for (let i = 0; i < s.length; i++) {
    let left = i;
    let right = i;
    while (s[left] === s[right] && right < s.length) {
      right++;
    }
    right--;
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      left--;
      right++;
    }
    left++;
    right--;
    if (right - left + 1 > max) {
      max = right - left + 1;
      longest = s.substring(left, right + 1);
    }
  }
  return longest;
};
