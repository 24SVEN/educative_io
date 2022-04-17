
class Solution:
    def find_subarrays(self,arr, target):
        result = []
        # TODO: Write your code here

        arr.sort()
        lw,rw = 0,len(arr)-1

        while lw<rw:
            if lw < target:
                result.append([arr[lw]])

            temp_target = target / arr[lw]
            
            temp_list = self.find_pair(arr,lw+1,rw,temp_target)
            if temp_list:
                for li in temp_list:
                    result.append(li.append(arr[lw]))
            lw += 1
        if arr[rw] < target:
            result.append([arr[rw]])

        return result
    
    def find_pair(self,arr,lw,rw,target):
        result = []
        while lw<rw:
            temp_product = arr[lw] * arr[rw]

            if temp_product < target:
                
                for i in range(lw,rw):
                    result.append([i,rw])
                lw += 1
            else:
                rw -= 1

        return result

test = Solution()
print(test.find_subarrays([2, 5, 3, 10],30))