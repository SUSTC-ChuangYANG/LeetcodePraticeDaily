object Solution {
    def maxProduct(nums: Array[Int]): Int = {
        if (nums.length == 1){
            return nums(0)
        }

        var tmp_min = 1
        var tmp_max = 1
        var res = -Int.MaxValue
        for ( num <- nums ) {
            var a1 = num*tmp_min
            var a2 = num*tmp_max
            if (a1> a2){
                if (a2 > num){
                    tmp_min = num
                }else{
                    tmp_min = a2
                }
                if (a1 >num){
                    tmp_max = a1
                }else{
                    tmp_max = num
                }
            }else{
                if (a1 > num){
                    tmp_min = num
                }else{
                    tmp_min = a1
                }
                if (a2 >num){
                    tmp_max = a2
                }else{
                    tmp_max = num
                }

            }
            if (tmp_max > res){
                res = tmp_max
            }
        }
        return res
    }
}