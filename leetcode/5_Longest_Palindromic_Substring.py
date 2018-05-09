class Solution1:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = len(s)
        max = 1
        start = 0
        end = 0
        if x ==1:
            return s
        else:
            for i in range(len(s)):
                for j in range(i+1,len(s)+1):
                    result = s[i:j]
                    reverse = result[::-1]
                    y = len(result)
                    if result == reverse:
                        if y>=max:
                            max = y
                            start = i
                            end = j
            return s[start:end]

class Solution2:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

class Solution3:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        max_length = 0
        palindromic = ''
        for i in range(l):
            x = 1
            while (i - x) >= 0 and (i + x) < l:
                if s[i + x] == s[i - x]:
                    x += 1
                else:
                    break
            x -= 1
            if 2 * x + 1 > max_length:
                max_length = 2 * x + 1
                palindromic = s[i - x:i + x + 1]
            x = 0
            if (i + 1) < l:
                while (i - x) >= 0 and (i + 1 + x) < l:
                    if s[i + 1 + x] == s[i - x]:
                        x += 1
                    else:
                        break
            x -= 1
            if 2 * x + 2 > max_length:
                max_length = 2 * x + 2
                palindromic = s[i - x:i + x + 2]
        if palindromic == '':
            palindromic = s[0]
        return palindromic
        
class Solution4:
    def longestPalindrome(self,s):
        n = len(s)
        maxl = 0
        start = 0
        for i in range(n):
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]
