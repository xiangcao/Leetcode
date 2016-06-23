"""
  int[] countingSort(int[] a, int k) {
        int c[] = new int[k];
        for (int i = 0; i < a.length; i++)
            c[a[i]]++;
        for (int i = 1; i < k; i++)
            c[i] += c[i-1];
        int b[] = new int[a.length];
        for (int i = a.length-1; i >= 0; i--)
            b[--c[a[i]]] = a[i];
        return b;
    }
"""


def countingSort(a, k):
    c = [0 for i in range(k)]

    for i in a:
        c[i] += 1
    output = [i for i in range(k) for j in range(c[i])]
           
    return output


def countingSort(a, k):
    c = [0 for i in range(k)]
    output = [0 for i in range(len(a))]
    for i in a:
        c[i] += 1

    for i in range(1,k):
        c[i] += c[i-1]

    for i in range(len(a)-1, -1, -1):
        output[c[a[i]]-1] = a[i] 
        c[a[i]] -= 1

    return output


a = [9,3,8,5,7,2]
k = 10

print countingSort(a,k)
