class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            print("------\n  i = %d" % i)
            print(usedChar)
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roma[s[i]] < roma[s[i + 1]]:
                sum -= roma[s[i]]
            else:
                sum += roma[s[i]]
        return sum
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ''
        ss = sorted(strs)
        print(ss)
        if len(ss) == 0:
            return ''
        if len(ss) == 1:
            return ss[0]
        for i in range(len(ss[0])):
            if ss[0][i] == ss[-1][i]:
                s += ss[0][i]
            else:
                break
        return s

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        p = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in p.values():
                stack.append(i)
            elif i in p.keys():
                if stack == [] or p[i] != stack.pop():
                    return False
            else:
                return False
        return stack == []

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


if __name__ == '__main__':
    solution = Solution()
    q = '()'
    print(solution.isValid(q))