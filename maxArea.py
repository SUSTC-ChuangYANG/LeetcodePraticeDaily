class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # o(n^2)
        # length = len(height)
        # farthest_max_num={}
        # for i in range(length):
        #     farthest_max_num[height[i]]=0
        # print(farthest_max_num)
        #
        # for i in range(length-1):
        #     for j in range(i+1,length):
        #         a,b = height[i],height[j]
        #         if height[i]<height[j]:
        #             farthest_max_num[a]=max(j-i,farthest_max_num[a])
        #         elif height[i]==height[j]:
        #             farthest_max_num[a]=max(j-i,farthest_max_num[a])
        #             farthest_max_num[b]=max(j-i,farthest_max_num[b])
        #         else:
        #             farthest_max_num[b]=max(j-i,farthest_max_num[b])
        # max_area = 0
        # for k,v in farthest_max_num.items():
        #     max_area = max(k*v,max_area)
        # return max_area

        # o(n)
        i,j = 0,len(height)-1
        max_area = 0

        while i < j:
            max_area = max(max_area,(j-i)*min(height[i],height[j]))
            standard_i = height[i]
            standard_j = height[j]
            if height[i] < height[j]:
                i += 1
                while height[i]<standard_i:
                    i += 1
            else:
                j -= 1
                while height[j]<standard_j:
                    j -= 1

        return max_area



def main():
    s = Solution()
    print(s.maxArea([1,5,3,7]))

if __name__ == "__main__":
    main()