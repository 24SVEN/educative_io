class Solution():
    def triplet_sum_close_to_target(self,arr, target_sum):
        # TODO: Write your code here
        ln = len(arr) - 1
        
        
        arr.sort()
        triplets= [[arr[ln],arr[ln-1],arr[ln-2]]]
        for i in range(len(arr)-1,0,-1):
            # if i == len(arr) - 1:
            #     triplets = self.find_triplet(arr,target_sum,i-1,arr[i],triplets)
            # elif arr[i] != arr[i+1]:
            triplets = self.find_triplet(arr,target_sum,i-1,arr[i],triplets)

        
        return sum(triplets[0])

    def find_triplet(self,arr,target_sum,rw,idx_val,triplets):
        lw = 0

        
        while lw<rw:
            #DONT NEED TO APPEND TO TRIPLETS SINCE WE ONLY NEED TO RETURN ONE SUM
            temp_sum = sum(triplets[0])
            existing_triplet_difference = target_sum - temp_sum

            difference = target_sum - (arr[lw] + arr[rw] + idx_val)

            if difference == 0:
                #we are just setting to one triplet since we only need one to return the SUM of the triplet
                return [[arr[lw] , arr[rw] ,idx_val]]
            
            elif abs(difference) == abs(existing_triplet_difference):
                if temp_sum > (arr[lw] + arr[rw] + idx_val):
                    triplets = [[arr[lw] , arr[rw] ,idx_val]]
                #rw -= 1

            elif abs(difference) < abs(existing_triplet_difference):
                triplets = [[arr[lw],arr[rw],idx_val]]

                #rw -= 1
                
            if difference < 0:
                rw -= 1
            else:
                lw += 1
                
        
        return triplets

#test cases
test = Solution()
print(test.triplet_sum_close_to_target([-2, 0, 1, 2],2)) #1
print(test.triplet_sum_close_to_target([-3, -1, 1, 2],1)) #0
print(test.triplet_sum_close_to_target([1, 0, 1, 1],100)) #3
# # print(test.triplet_sum_close_to_target([1, 1, 1, 0],-100))
# # print(test.triplet_sum_close_to_target([1,1,-1,-1,3],-1))
print(test.triplet_sum_close_to_target([1,1,-1,-1,3],3)) #3
print(test.triplet_sum_close_to_target([-1,0,1,2,-1,-4],0)) #0
print(test.triplet_sum_close_to_target([1,2,4,8,16,32,64,128],82))
