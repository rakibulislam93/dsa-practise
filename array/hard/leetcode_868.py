
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        index_for_one = -1
        max_distance = 0

        for i in range(len(binary)):
            if binary[i]=='1':
                if index_for_one != -1:
                    distance = i - index_for_one
                    max_distance = max(max_distance,distance)
                
                index_for_one = i
            

        return max_distance