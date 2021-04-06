// Sbmission for 2021-04-05 

// Initial approach using TreeSet

class Solution {
    public boolean isIdealPermutation(int[] A) {
        TreeSet<Integer> ts = new TreeSet<Integer>();
        int prevVal = -1;
        int localCount = 0;
        int globalCount = 0;
        for(int i = 0 ; i < A.length; i++){
            if(i != 0){
                if(prevVal>A[i])
                    localCount++;
            }
            ts.add(A[i]);
            prevVal = A[i];
            Iterator it = ts.descendingIterator();
            /*if(i == 2)
                return (0 == findIndex(it, A[i]));*/
            globalCount += findIndex(it, A[i]);
        }
        return (localCount == globalCount);
    }
    public int findIndex(Iterator it, int val){
        int tempCount = 0;
        while(it.hasNext()){
            int a = (int)it.next();
            if(val == a)
                return tempCount;
            tempCount++;
        }
        return tempCount;
    }
}

// Optimal solution from discussion.
class Solution {
    public boolean isIdealPermutation(int[] A) {

        for (int i = 0; i < A.length; i++) {
            if (Math.abs(i - A[i]) > 1)
                return false;
        }

        return true;
    }
}
