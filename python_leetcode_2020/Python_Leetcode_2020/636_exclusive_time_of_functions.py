class Solution:
    """
    In a more conventional approach, let's look between adjacent events, with duration time - prev_time. If we started a function, and we have a function in the background, then it was running during this time. Otherwise, we ended the function that is most recent in our stack.
    """
    # top of the stack always has the current running function id; 
    # prev stores the time current running function started running
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)

            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time 
                stack.append(fn)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return ans
