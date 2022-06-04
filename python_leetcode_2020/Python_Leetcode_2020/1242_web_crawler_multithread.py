# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

# Python3 Multithreaded BFS with Queue

import threading
from queue import Queue

class Solution1:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def hostname(url):
            start = len("http://")
            i = start
            while i < len(url) and url[i] != "/":
                i += 1
            return url[start:i]

        queue = Queue()
        seen = {startUrl}
        start_hostname = hostname(startUrl)
        seen_lock = threading.Lock()

        def worker():
            while True:
                url = queue.get()
                if url is None:
                    return

                for next_url in htmlParser.getUrls(url):
                    if next_url not in seen and hostname(next_url) == start_hostname:
                        seen_lock.acquire()
                        # Acquire lock to ensure urls are no enqueed multiple times
                        if next_url not in seen:
                            seen.add(next_url)
                            queue.put(next_url)
                        seen_lock.release()
                queue.task_done()
        
        num_workers = 8
        workers = []
        queue.put(startUrl)
        
        for i in range(num_workers):
            t = threading.Thread(target=worker)
            t.start()
            workers.append(t)
        
        # Wait until empty
        queue.join()
        
        for i in range(num_workers):
            queue.put(None)
        for t in workers:
            t.join()
        
        return list(seen)

#Python3 Thread + Lock implementation: 256 ms. ThreadPool: 300 ms.
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
class Solution:
    def __init__(self):
        self.lock = Lock()
        self.queue = collections.deque()
        self.visited = set()
    
    def extractHostName(self, url):
        return '.'.join(url.split('/')[2].split('.')[1:])    
    
    def downloadUrl(self, curr_url):
        next_urls = self.htmlParser.getUrls(curr_url)
        
		# Use Lock to protect shared states.
        with self.lock:
            for url in next_urls:
                if url not in self.visited and self.curr_hostname == self.extractHostName(url):
                    self.queue.append(url)
                    self.visited.add(url)  

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        self.queue.append(startUrl)
        self.curr_hostname = self.extractHostName(startUrl)
        self.visited = {startUrl}
        self.htmlParser = htmlParser
		# Limit to 10 worker threads
        executor = ThreadPoolExecutor(max_workers=10)
        
        while self.queue:
            curr_url = self.queue.popleft()

            url_list = list()
			# Add at least first URL from the queue
            url_list.append(curr_url)

			# If there are still URLs in the queue, add to the list 
            while self.queue:
                curr_url = self.queue.popleft()
                url_list.append(curr_url)
            
            executor_list = list()
			# Execute this batch of threads with threadpool
            for i in range(len(url_list)):
                executor_list.append(executor.submit(self.downloadUrl, (url_list[i])))
                
			# Main thread waiting for the above threads to finish
            for future in executor_list:
                future.result()
        
        # Shutdown ThreadPool executor
        executor.shutdown()
        
        return list(self.visited) 
    

"""Summary
We implement a classic BFS but the entries in our queue are future objects instead of primitve values. A pool of at most max_workers threads is used to execute getUrl calls asynchronously. Calling result() on our futures blocks until the task is completed or rejected.

The great thing about this solution is:

worker thread only calls htmlParser.getUrls, and that's all a worker does;
bookkeeping of the seen urls are centralized in the main thread, therefore eliminates the need for a lock, which is necessary if worker threads also bookkeep seen urls.
Note that DFS will work as well, i.e., stack instead of queue.
"""
from concurrent import futures

class Solution3:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = lambda url: url.split('/')[2]
        seen = {startUrl}
    
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url not in seen and hostname(startUrl) == hostname(url):
                        seen.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))
        
        return list(seen) 

