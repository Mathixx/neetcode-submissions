class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # you wanna add the project to a minHeap of profits of all project you have enough capital to achieve
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort(key=lambda x:x[0])

        affordable_projects = []
        project_count = 0
        curr_capital = w
        i=0

        while i < len(projects) and project_count < k:
            capital, profit = projects[i]
            if capital <= curr_capital:
                heapq.heappush(affordable_projects, -profit)
                i += 1
            else:
                if affordable_projects:
                    curr_capital -= heapq.heappop(affordable_projects)
                    project_count += 1
                else:
                    break
        
        while affordable_projects and project_count < k:
            curr_capital -= heapq.heappop(affordable_projects)
            project_count += 1

        return curr_capital 






        