import heapq
class MedianFinder:

    def __init__(self):
        #this will be a min heap that contains the larger numbers
        self.min_heap = []

        #this will be a max heap that contains the smaller numbers
        self.max_heap = []
        

        
    def balance(self):
        return
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)

        #check if max is larger than the min
        if len(self.min_heap)>0 and -self.max_heap[0] > self.min_heap[0]:
            popped = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,popped)

        #check if there is balance


        if len(self.max_heap) > (len(self.min_heap)+1):
            popped = -1*heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,popped)
        
        elif len(self.min_heap) > (len(self.max_heap)+1):
            popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-1*popped)


    def findMedian(self) -> float:
        
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            
            return (self.min_heap[0] - self.max_heap[0]) / 2
        

        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())