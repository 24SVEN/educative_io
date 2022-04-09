

class Solution:
    def triplet_with_smaller_sum(self,arr, target):

        lw,rw = 0,len(arr)-1
        arr.sort()
        count = 0
        while lw<rw:
            temp_target = target-arr[lw]

            count += self.find_pair(arr,temp_target,lw+1,rw)
            lw += 1
            

        return count


    def find_pair(self,arr,target,lw,rw):

        count = 0
        while lw<rw:
            curr_sum = arr[lw] + arr[rw]

            if curr_sum < target:
                # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between left and right to get a sum less than the target sum
                # For example, using the first test case, if all values in rw-lw are [3,2] and those added up with -1 will always be less than the target of 4
                count += (rw-lw)
                lw += 1
            elif curr_sum >= target:
                rw -= 1

        return count
                

test = Solution()
print(test.triplet_with_smaller_sum([-1, 0, 2, 3],3)) #2

print(test.triplet_with_smaller_sum([-1, 4, 2, 1, 3],5)) #4



