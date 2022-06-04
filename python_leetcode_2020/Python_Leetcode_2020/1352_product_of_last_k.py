"""
Implement the class ProductOfNumbers that supports two methods:

1. add(int num)

Adds the number num to the back of the current list of numbers.
2. getProduct(int k)

Returns the product of the last k numbers in the current list.
You can assume that always the current list has at least k numbers.
At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.
"""

# java solution
class ProductOfNumbers {
    ArrayList<Integer> A = new ArrayList(){{
        add(1);
        }};
    public ProductOfNumbers() {    

    }

    //Prefix Product
    public void add(int a) {
        if (a > 0)
            A.add(A.get(A.size() - 1) * a);
        else {
            A = new ArrayList();
            A.add(1);
        }
    }

    public int getProduct(int k) {
        int n = A.size();
        return k < n ? A.get(n - 1) / A.get(n - k - 1)  : 0;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */
