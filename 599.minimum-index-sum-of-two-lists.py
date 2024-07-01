"""
Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.

 

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
Example 3:

Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        # check for minimum length list
        f_list = list2
        o_list = list1
        if len(list1) > len(list2):
            f_list = list1
            o_list = list2
        
        for i in range(len(f_list)):
            try:
                index = o_list.index(f_list[i])
            except:
                index = None
            if index is not None:
                if i+index in d.keys():
                    l = d[i+index]
                    l.append(f_list[i])
                    d[i+index] = l
                else:
                    d[i+index] = [f_list[i]]
        
        return d[min(d.keys())]


        

############ Faster and Improved solution ###############

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        list1_d = { string:i for i, string in enumerate(list1) }
        list2_d = { string:i for i, string in enumerate(list2) }
        
        f_list, o_list =  (list1_d, list2_d) if len(list1_d) < len(list2_d) else ( list2_d, list1_d)
        
        for word,index in f_list.items():
            if word in o_list.keys():
                index_o = o_list[word]
                d_key = index_o+index
                if d_key in d:
                    l = d[d_key]
                    l.append(word)
                    d[d_key] = l
                else:
                    d[d_key] = [word]
        
        return d[min(d.keys())]