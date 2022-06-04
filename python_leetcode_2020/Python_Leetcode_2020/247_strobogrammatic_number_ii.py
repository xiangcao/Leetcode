"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.
"""

Some observation to the sequence:

n == 1: [0, 1, 8]

n == 2: [11, 88, 69, 96]

How about n == 3?
=> it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 2

n == 4?
=> it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 2

n == 5?
=> it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 4

the same, for n == 6, it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 4

def findStrobogrammatic(self, n):
    evenMidCandidate = ["11","69","88","96", "00"]
    oddMidCandidate = ["0", "1", "8"]
    if n == 1:
        return oddMidCandidate
    if n == 2:
        return evenMidCandidate[:-1]
    if n % 2:
        pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
    else: 
        pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate
    premid = (n-1)/2
    return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]


# idea 2
public List<String> findStrobogrammatic(int n) {
    return helper(n, n);
}

List<String> helper(int n, int m) {
    if (n == 0) return new ArrayList<String>(Arrays.asList(""));
    if (n == 1) return new ArrayList<String>(Arrays.asList("0", "1", "8"));
    
    List<String> list = helper(n - 2, m);
    
    List<String> res = new ArrayList<String>();
    
    for (int i = 0; i < list.size(); i++) {
        String s = list.get(i);
        
        if (n != m) res.add("0" + s + "0");
        
        res.add("1" + s + "1");
        res.add("6" + s + "9");
        res.add("8" + s + "8");
        res.add("9" + s + "6");
    }
    
    return res;
}
