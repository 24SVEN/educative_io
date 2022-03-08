class Solution():

    def triplet_with_smaller_sum(self,arr, target):
        count = -1
        triplets = 0
        # TODO: Write your code here
        arr.sort()

        for i in range(2,len(arr)):
            triplets = self.find_triplet(arr,target,triplets,i)


        return triplets

    def find_triplet(self,arr,target,triplets,idx):
        rw = idx - 1
        lw = 0

        
        while lw < rw:
            temp_sum = arr[rw] + arr[lw] + arr[idx]
            if temp_sum < target:
                triplets += 1

            if temp_sum <= target:
                rw -= 1

            else:
                
                lw += 1
        
        return triplets


test = Solution()
print(test.triplet_with_smaller_sum([-1, 0, 2, 3],3)) #2

#print(test.triplet_with_smaller_sum([-1, 4, 2, 1, 3],5)) #4



