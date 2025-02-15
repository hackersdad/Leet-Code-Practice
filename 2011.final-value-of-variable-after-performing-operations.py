# There is a programming language with only four operations and one variable X:

# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        op_val = {'++X':1,'X++':1,'X--':-1,'--X':-1}
        for o in operations:
            x += op_val[o]
        return x


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if "++" in op else -1 for op in operations)
