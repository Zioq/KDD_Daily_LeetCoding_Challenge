// 242. Valid Anagram - https://leetcode.com/problems/valid-anagram/
var isAnagram = function(s,t) {
    s = s.split("")
    t = t.split("")
    const sortedS = s.sort();
    const sortedT = t.sort();

    if (sortedS.length !== sortedT.length){
        return false;
    } else {
        let result = false;
        // compare each element of array
        for (let i = 0; i < sortedS.length; i++) {
            if(sortedS[i] !== sortedT[i]) {
                return false
            } else {
                result = true;
            }
        }

        return result;
    }
}

console.log(isAnagram("anagram","nagaram"))
console.log(isAnagram("rat","car"))
console.log(isAnagram("abc","def"));
console.log(isAnagram("rat","cari"))