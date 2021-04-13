// submission for 2021-04-13
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {
    ListIterator<Integer> flattenedIterator;
    ArrayList<Integer> ary;
    public NestedIterator(List<NestedInteger> nestedList) {
        Iterator it = nestedList.iterator();
        ary = new ArrayList<Integer>();
        while(it.hasNext()){
            NestedInteger ni = (NestedInteger) it.next();
            if(ni.isInteger()){
                ary.add(ni.getInteger());   
            }
            else {
                addListElements(ni.getList());   
            }
        }
        flattenedIterator = ary.listIterator();
    }
    
    public void addListElements(List<NestedInteger> list){
        Iterator it = list.iterator();
        while(it.hasNext()){
            NestedInteger ni = (NestedInteger) it.next();
            if(ni.isInteger()){
                ary.add(ni.getInteger());   
            }
            else {
                addListElements(ni.getList());   
            }
        }
    }

    @Override
    public Integer next() {
        flattenedIterator.add(4747); 
        return flattenedIterator.next();
    }

    @Override
    public boolean hasNext() {
        return flattenedIterator.hasNext();
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
