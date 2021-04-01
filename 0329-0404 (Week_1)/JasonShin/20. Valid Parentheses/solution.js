// https://leetcode.com/problems/valid-parentheses/

/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    //Using Stack.
    let stackArr = new Array();
    let sLength = s.length;
    //Check the string length is even. Otherwise, it cannot be valid.
    if(sLength % 2 !== 0){
        return false;
    }
    
    for(let i = 0; i < sLength; i++){
        switch(s[i]) {
            case '(':
                stackArr.push(')');
                break;
            case '[':
                stackArr.push(']');
                break;
            case '{':
                stackArr.push('}');
                break;
            //From here we check the following LIFO as a stack.
            case ')':
               if(stackArr.pop() === ')') {
                   break;
               } else return false;
            case ']':
                if(stackArr.pop() === ']') {
                   break;
               } else return false;
            case '}':
                if(stackArr.pop() === '}') {
                   break;
               } else return false;
        }
    }
    if(stackArr.length === 0) return true;
    else return false;
};