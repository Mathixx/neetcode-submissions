import bisect

class MedianFinder:

    def __init__(self):
        self.median_left = None
        self.median_right = None
        self.data = []
        

    def addNum(self, num: int) -> None:
        if not self.data:
            self.data.append(num)
            self.median_left = 0
            self.median_right = 0
        else:
            bisect.insort(self.data, num)
            if self.median_left == self.median_right:
                self.median_right += 1
            else:
                self.median_left+=1

    def findMedian(self) -> float:
        if self.median_left == self.median_right:
            return self.data[self.median_left]
        else:
            return float(self.data[self.median_left])/2 + float(self.data[self.median_right])/2
        
        