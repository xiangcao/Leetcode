"""
An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A has size at least 2.

Set S can have elements not consecutive
"""

First sort the intervals, with their starting points from low to high
Then use a stack to eliminate the intervals which fully overlap another interval.
For example, if we have [2,9] and [1,10], we can get rid of [1,10]. Because as long as we pick up two numbers in [2,9], the requirement for [1,10] can be achieved automatically.

Finally we deal with the sorted intervals one by one.
(1) If there is no number in this interval being chosen before, we pick up 2 biggest number in this interval. (the biggest number have the most possibility to be used by next interval)
(2) If there is one number in this interval being chosen before, we pick up the biggest number in this interval.
(3) If there are already two numbers in this interval being chosen before, we can skip this interval since the requirement has been fulfilled.

class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->((a[0]==b[0])?(-a[1]+b[1]):(a[0]-b[0])));
        Stack<int[]> st=new Stack<>();
        for (int[] in:intervals)
        {
            while (!st.isEmpty() && st.peek()[1]>=in[1]) st.pop();
            st.push(in);
        }
        int n=st.size();
        int[][] a=new int[n][2];
        for (int i=n-1;i>=0;i--)
        {
            a[i][0]=st.peek()[0];
            a[i][1]=st.pop()[1];
        }
        int ans=2;
        int p1=a[0][1]-1,p2=a[0][1];
        for (int i=1;i<n;i++)
        {
            boolean bo1=(p1>=a[i][0] && p1<=a[i][1]),bo2=(p2>=a[i][0] && p2<=a[i][1]);
            if (bo1 && bo2) continue;
            if (bo2)
            {
                p1=p2;
                p2=a[i][1];
                ans++;
                continue;
            }
            p1=a[i][1]-1;
            p2=a[i][1];
            ans+=2;
        }
        return ans;
    }
}
