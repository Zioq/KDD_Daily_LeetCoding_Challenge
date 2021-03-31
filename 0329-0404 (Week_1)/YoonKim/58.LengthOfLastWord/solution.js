// 58.Length of Last Word - https://leetcode.com/problems/length-of-last-word/submissions/

var lengthOfLastWord = function(s) {
    s = s.trim().split(" ");
    return s[s.length-1].length;
};
