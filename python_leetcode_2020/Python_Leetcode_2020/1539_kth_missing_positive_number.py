# solution 1 O(N)
int findKthPositive(vector<int>& arr, int k) {
    for (int n = 1, i = 0; n <= 1000; ++n) {
        if (i < arr.size() && arr[i] == n)
            ++i;
        else if (--k == 0)
            return n;
    }
    return 1000 + k;
}

# soltuion 2 binary search O(LogN)
Explanation on why l + k:

We use binary search to find the smallest index, l, such that there are more than k missing numbers in [0, A[l]]. The actual number of missing numbers in [0, A[l-1]] is A[l-1] - (l - 1) - 1 = A[l-1] - l. Counting from A[l-1], The k-th missing number is therefore (A[l-1] + k - (A[l-1] - l) = l + k

we know it starts from 1, so

arr[mid] - (mid + 1)
will be the count of number that missed.

Thanks to @caohuicn for explaining this for us:
" Here is my understanding of why l + k is the answer. ( a bit long, please comment if there's a more concise explanation):

We are maintaining such invariant throughout the loop: l + k <= ans <= r + k. Obviously when the array is missing k or more elements in the beginning, ans == k; when there is no missing elements, ans is arr.length + k;
When we update l = mid + 1, there are already mid + 1 non-missed elements on the left, and we still need k missed elements, so l + k <= ans still holds true;
When we update r = mid, we know ans is less than arr[mid], and on the left of mid, there are mid non-missed elements, plus k or more missed elements, so ans is at most mid + k;
Finally when l == r, we get l + k == ans == r + k "
    public int findKthPositive(int[] arr, int k) {
        int l = 0, r = arr.length;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] - (mid + 1) >= k) r = mid;  //missed more or equal than k numbers, left side;
            else l = mid + 1;   // missed less than k numbers, must be in the right side;
        }
        return l + k;
    }
