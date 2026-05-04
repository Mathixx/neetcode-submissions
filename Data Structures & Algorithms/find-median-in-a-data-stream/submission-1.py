import bisect 
class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)
        self.size += 1
        

    def findMedian(self) -> float:
        if self.size == 1:
            return self.arr[0]
        mid = self.size // 2
        if self.size % 2 == 1:
            return self.arr[mid]
        else:
            return (self.arr[mid-1] + self.arr[mid]) / 2.0
        
        