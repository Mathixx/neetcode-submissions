class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort the tasks by begining time at first
        # use min heap to know that among the tasks that can be done which ones are the shortest to do
        ordering = {}
        for i in range(len(tasks)):
            ordering[(tasks[i][0],tasks[i][1])] = i
        
        tasks.sort(key=lambda x : x[0])
        
        curr_time = tasks[0][0]
        heap = []
        res = []

        j = 0
        while j < len(tasks):
            start, time = tasks[j]

            if start <= curr_time:
                heapq.heappush(heap, (time, start))
                j += 1
            else:
                if heap:
                    # achieve shortest task and move up in time accordingly
                    sh_time, sh_start = heapq.heappop(heap)
                    res.append(ordering[(sh_start, sh_time)])
                    curr_time += sh_time
                
                if not heap:
                    curr_time = max(curr_time, start)
        
        while heap:
            sh_time, sh_start = heapq.heappop(heap)
            res.append(ordering[(sh_start, sh_time)])
            curr_time += sh_time
        
        return res
