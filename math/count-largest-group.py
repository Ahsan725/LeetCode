class Solution:
    def countLargestGroup(self, n: int) -> int:
        #use a map key:number -> [numbers that add up to that number]
        num_to_list = defaultdict(list)

        for i in range(1, n + 1):
            if i <=9:
                summ = i
            else:
                string_val = str(i)
                summ = 0
                for c in string_val:
                    summ += int(c)
                # print(summ)

            num_to_list[summ].append(i)
        
        #find the largest number of elemnts in a group and then how many groups hve that 
        max_count = float('-inf')
        res = 0
        for lists in num_to_list.values():
            count = 0 
            for num in lists:
                count += 1
            max_count = max(max_count, count)
        
        for lists in num_to_list.values():
            count = 0
            for num in lists:
                count += 1
            if count == max_count:
                res += 1
        return res
            