"""
Frequency: Amazon 341; 
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]: 
        def get_key(log):
            _id, content = log.split(" ", maxsplit=1)
            return (0, content, _id) if content[0].isalpha() else (1, )

        return sorted(logs, key=get_key)


Overview
First of all, let us put aside the debate whether this problem is an easy or medium one. The problem is a good exercise to practice the technique of custom sort in different languages.

The idea of custom sort is that we don't have to rewrite a sorting algorithm every time we have a different sorting criteria among the elements.

Each language provides certain interface that allows us to customize the sorting criteria of the sorting functions, so that we can reuse the implementation of sorting in different scenarios.

In this article, we will present two ways to specify the sorting order, namely by comparator and by sorting key.

Approach 1: Comparator
Intuition

Algorithm

The above pairwise "less than" relationship is also known as comparator in Java, which is a function object that helps the sorting functions to determine the orders among a collection of elements.

We show the definition of the comparator interface as follows:

int compare(T o1, T o2) {
    if (o1 < o2)
        return -1;
    else if (o1 == o2)
        return 0;
    else // o1 > o2
        return 1;
}
As we discussed before, once we define the pairwise relationship among the elements in a collection, the total order of the collection is then fixed.

Now, what we need to do is to define our own proper comparator according to the description of the problem. We can translate the problem into the following rules:

1). The letter-logs should be prioritized above all digit-logs.

2). Among the letter-logs, we should further sort them firstly based on their contents, and then on their identifiers if the contents are identical.

3). Among the digit-logs, they should remain in the same order as they are in the collection.

One can then go ahead and implement the comparator based on the above rules. Here is an example.


Stable Sort

One might notice that in the above implementation one can find the logic that corresponds each of the rules, except the Rule (3).

Indeed, we did not do anything explicitly to ensure the order imposed by the Rule (3).

The short answer is that the Rule (3) is ensured implicitly by an important property of sorting algorithms, called stability.

It is stated as "stable sorting algorithms sort equal elements in the same order that they appear in the input."

Not all sort algorithms are stable, e.g. merge sort is stable.

The Arrays.sort() interface that we used is stable, as one can find in the specification.

Therefore, the Rule (3) is implicitly respected thanks to the stability of the sorting algorithm that we used.

Complexity Analysis

Let NN be the number of logs in the list and MM be the maximum length of a single log.

Time Complexity: \mathcal{O}(M \cdot N \cdot \log N)O(M⋅N⋅logN)

First of all, the time complexity of the Arrays.sort() is \mathcal{O}(N \cdot \log N)O(N⋅logN), as stated in the API specification, which is to say that the compare() function would be invoked \mathcal{O}(N \cdot \log N)O(N⋅logN) times.

For each invocation of the compare() function, it could take up to \mathcal{O}(M)O(M) time, since we compare the contents of the logs.

Therefore, the overall time complexity of the algorithm is \mathcal{O}(M \cdot N \cdot \log N)O(M⋅N⋅logN).

Space Complexity: \mathcal{O}(M \cdot \log N)O(M⋅logN)

For each invocation of the compare() function, we would need up to \mathcal{O}(M)O(M) space to hold the parsed logs.

In addition, since the implementation of Arrays.sort() is based on quicksort algorithm whose space complexity is \mathcal{O}(\log n)O(logn), assuming that the space for each element is \mathcal{O}(1)O(1)). Since each log could be of \mathcal{O}(M)O(M) space, we would need \mathcal{O}(M \cdot \log N)O(M⋅logN) space to hold the intermediate values for sorting.

In total, the overall space complexity of the algorithm is \mathcal{O}(M + M \cdot \log N) = \mathcal{O}(M \cdot \log N)O(M+M⋅logN)=O(M⋅logN).

Approach 2: Sorting by Keys
Intuition

Rather than defining pairwise relationships among all elements in a collection, the order of the elements can also be defined with sorting keys.

To illustrate the idea, let us first define a Student object as follows, which has three properties: name, grade, age.

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
Now, if we are asked to sort the list of students by age in ascending order, we could simply use the age property of each student as the sorting key, as follows:

>>> sorted(student_objects, key=lambda student: student.age)
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
Furthermore, the key could be a tuple of multiple keys, i.e. tuple(key_1, key_2, ... key_n).

If two elements have the same value on key_1, the comparison will carry on for the following keys, i.e. key_2 ... key_n.

As a result, if we are asked to sort the students first by the grade, then by the age, we can simply return the compound key (stduent.grade, student.age), as follows:

>>> sorted(student_objects, key=lambda student: (student.grade, student.age))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
Algorithm

Given the above intuition, it should be clear that all we need is to translate the rules we defined before into a tuple of keys.

As a reminder, here are a list of the rules that we defined before, concerning the order of logs:

1). The letter-logs should be prioritized above all digit-logs.

2). Among the letter-logs, we should further sort them based on firstly on their contents, and then on their identifiers if the contents are identical.

3). Among the digit-logs, they should remain in the same order as they are in the collection.

To ensure the above order, we could define a tuple of 3 keys, (key_1, key_2, key_3), as follows:

key_1: this key serves as a indicator for the type of logs. For the letter-logs, we could assign its key_1 with 0, and for the digit-logs, we assign its key_1 with 1. As we can see, thanks to the assigned values, the letter-logs would take the priority above the digit-logs.

key_2: for this key, we use the content of the letter-logs as its value, so that among the letter-logs, they would be further ordered based on their content, as required in the Rule (2).

key_3: similarly with the key_2, this key serves to further order the letter-logs. We will use the identifier of the letter-logs as its value, so that for the letter-logs with the same content, we could further sort the logs based on its identifier, as required in the Rule (2).

Note: for the digit-logs, we don't need the key_2 and key_3. We can simply assign the None value to these two keys. As a result, the key value for all the digit-logs would be (1, None, None).

Finally, thanks to the stability of sorting algorithms, the elements with the same key value would remain the same order as in the original input. Therefore, the Rule (3) is ensured.


Complexity Analysis

Let NN be the number of logs in the list and MM be the maximum length of a single log.

Time Complexity: O(M⋅N⋅logN)

The sorted() in Python is implemented with the Timsort algorithm whose time complexity is O(N⋅logN).

Since the keys of the elements are basically the logs itself, the comparison between two keys can take up to O(M) time.

Therefore, the overall time complexity of the algorithm is O(M⋅N⋅logN).

Space Complexity: O(M⋅N)

First, we need \mathcal{O}(M \cdot N)O(M⋅N) space to keep the keys for the log.

In addition, the worst space complexity of the Timsort algorithm is O(N), assuming that the space for each element is O(1). Hence we would need O(M⋅N) space to hold the intermediate values for sorting.

In total, the overall space complexity of the algorithm is O(M⋅N+M⋅N)=O(M⋅N).
