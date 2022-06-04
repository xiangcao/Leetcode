from concurrent import futures
"""
Multithread

Summary
We implement a classic BFS but the entries in our queue are future objects instead of primitve values. A pool of at most max_workers threads is used to execute getUrl calls asynchronously. Calling result() on our futures blocks until the task is completed or rejected.
"""
class Solution1:
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

# python bfs
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = {startUrl}
        domain = startUrl.split("http://")[1].split("/")[0]
        ans = [startUrl]
        queue = collections.deque([startUrl])
        while queue:
            for _ in range(len(queue)):
                url = queue.popleft()
                check = htmlParser.getUrls(url)
                for new_url in check:
                    if new_url in visited:
                        continue
                    if new_url.split("http://")[1].split("/")[0] != domain:
                        continue
                    ans.append(new_url)
                    visited.add(new_url)
                    queue.append(new_url)        
        return ans

# java bfs
class Solution {
   public List<String> crawl(String startUrl, HtmlParser htmlParser) {
       Set<String> set = new HashSet<>();
       Queue<String> queue = new LinkedList<>();
       
       String hostname = getHostname(startUrl);
       queue.offer(startUrl);
       set.add(startUrl);
       while (!queue.isEmpty()) {
           String currentUrl = queue.poll();
           for (String url: htmlParser.getUrls(currentUrl)) {
               if (getHostname(url).equals(hostname) && !set.contains(url)) {
                   queue.offer(url);
                   set.add(url);
               }
           }
       }
       
       return new ArrayList<String>(set);
    }
    
    private String getHostname(String Url) {
        return Url.split("/")[2];
    }
}
