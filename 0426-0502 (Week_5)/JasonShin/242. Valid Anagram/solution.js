// https://leetcode.com/problems/valid-anagram/
// Tuesday Submission

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
//First solution.
 var isAnagram = function(s, t) {
    if(s.length !== t.length) return false;
    for(const l of s){
        t = t.replace(l, '')
    }
    
    if(t.length) return false;
    else return true;
};
//Second solution.
const isAnagram = (s,t) => {
   return s.split('').sort().join('') === t.split('').sort().join('')
}