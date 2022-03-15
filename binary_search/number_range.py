class Solution():
    def findRange(self,arr,key):
        result = [-1,-1]

        return self.binarySearch()
    def binarySearch(self,arr,key,isLeft):
        lw,rw = 0,len(arr)-1

        while lw <= rw:
            mid = (rw+lw)//2


            if arr[mid] > key:
                rw = mid - 1
            elif arr[mid] < key:
                lw = mid + 1
            else:
                if isLeft:
                    rw = mid - 1
                else:
                    lw = mid + 1
        
        if isLeft:
            return lw
        else:
            return rw


def main():
    test = Solution()
    print(test.find_range([4, 6, 6, 6, 9], 6))
    print(test.find_range([1, 3, 8, 10, 15], 10))
    print(test.find_range([1, 3, 8, 10, 15], 12))