// Submission for 2021-04-04

class MyCircularQueue {
    int[] ary;
    int front = 0;
    int rear = -1;
    int len = 0;
    int k = 0;
    public MyCircularQueue(int k) {
        ary = new int[k];
        this.k = k;
    }
    
    public boolean enQueue(int value) {
        if(isFull())
            return false;
        rear = (rear + 1) %k ;
        ary[rear] = value;
        len++;
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty())
            return false;
        front = (front + 1) % k;
        len--;
        return true;
    }
    
    public int Front() {
        if(isEmpty())
            return -1;
        return ary[front];
    }
    
    public int Rear() {
        if(isEmpty())
            return -1;
        return ary[rear];
    }
    
    public boolean isEmpty() {
        if(len == 0)
            return true;
        return false;
    }
    
    public boolean isFull() {
        if(len == k)
            return true;
        return false;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
