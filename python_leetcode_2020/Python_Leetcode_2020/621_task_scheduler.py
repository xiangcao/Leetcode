"""
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100]
"""
# Greedy
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = sorted(collections.Counter(tasks).values())
        maxfreq = frequencies.pop()
        idle_time = (maxfreq-1) * n
        for f in reversed(frequencies):
            idle_time -= min(f, maxfreq-1)
            if idle_time <= 0 :
                idle_time = 0
                break
        return idle_time + len(tasks)
 
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = sorted(collections.Counter(tasks).values())
        maxFreq = frequencies[-1]
        maxCount = frequencies.count(maxFreq)
        
        partCount = maxFreq - 1;
        partLength = n - (maxCount - 1)
        emptySlots = partCount * partLength;
        availableTasks = len(tasks) - maxFreq * maxCount
        idles = max(0, emptySlots - availableTasks)
        
        return len(tasks) + idles
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = sorted(collections.Counter(tasks).values())
        maxFreq = frequencies[-1]

        partCount = maxFreq - 1;
        partLength = n 
        emptySlots = partCount * partLength;
        availableTasks = len(tasks) - maxFreq - (maxCount-1)
        idles = max(0, emptySlots - availableTasks)
        
        return len(tasks) + idles

    # round 2
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = sorted(collections.Counter(tasks).values())
        maxfreq = frequencies.pop()
        idle_time = (maxfreq-1) * n
        while frequencies and idle_time > 0:
            idle_time -= min(frequencies.pop(), maxfreq-1)
        idle_time = max(0, idle_time)
        return idle_time + len(tasks)
