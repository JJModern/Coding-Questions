class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # a pred of b (insert one char) -> B
        # length of longest word chain

        # first sort them in terms of shortest length
        words = sorted(words, key=lambda x: len(x))
        print(words)
        adj_lst_of_dict = [{} for _ in words]
        max_gain_lst = [None for _ in words]
        # make list of dictionary (adj list). for all words
        for i, item in enumerate(words):
            input_dict = {}
            for j, other_item in enumerate(words):
                if item in other_item and i != j and len(item) > len(other_item):
                    input_dict[other_item] = j
            adj_lst_of_dict[i] = input_dict

        max_num = 0
        for dct in adj_lst_of_dict:
            max_num = max(
                max_num, self.recursive_max_len(dct, adj_lst_of_dict, max_gain_lst)
            )
        return max_num

    def recursive_max_len(self, input_dict, adj_lst_of_dict, max_gain_lst):
        # recursive max gain function
        if input_dict == {}:
            return 1

        max_num = 0
        for key, index in input_dict.items():
            if not max_gain_lst[index]:
                result = recursive_max_len(
                    adj_lst_of_dict[index], adj_lst_of_dict, max_gain_lst
                )
                max_gain_lst[index] = result
                max_num = max(max_num, result)
            else:
                max_num = max(max_num, max_gain_lst[index])

        return 1 + max_num


new_instance = Solution()
print(new_instance.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
