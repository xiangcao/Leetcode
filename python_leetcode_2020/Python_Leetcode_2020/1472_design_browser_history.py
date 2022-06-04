"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

"""

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history=[homepage]
        self.pos = 0
        self.size = 1

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if self.pos + 1 == len(self.history):
            self.history.append(url)
        else:
            self.history[self.pos+1] = url
        self.pos += 1
        self.size = self.pos + 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.pos = max(0, self.pos-steps)
        return self.history[self.pos]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.pos = min(self.size-1, self.pos + steps)
        return self.history[self.pos]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# round 2
class BrowserHistory2:

    def __init__(self, homepage: str):
        self.backlist=[homepage]
        self.forwardlist = []

    def visit(self, url: str) -> None:
        self.backlist.append(url)
        self.forwardlist = []

    def back(self, steps: int) -> str:
        while steps and len(self.backlist) > 1:
            self.forwardlist.append(self.backlist.pop())
            steps -= 1
        return self.backlist[-1]

    def forward(self, steps: int) -> str:
        while steps and self.forwardlist:
            self.backlist.append(self.forwardlist.pop())
            steps -= 1
        return self.backlist[-1]
