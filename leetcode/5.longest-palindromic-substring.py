"""https://leetcode.com/problems/longest-palindromic-substring/description/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

"""
from line_profiler import LineProfiler

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    n1 = n-1
    lp = 0
    p = ''
    for i in range(1, n):
        if s[i-1] == s[i]:
            k, j = i-1, i
            while k > 0 and j < n1 and s[k-1] == s[j+1]:
                k -= 1
                j += 1
            if j-k+1 > lp:
                lp = j-k+1
                p = s[k:j+1]
        if i < n1 and s[i-1] == s[i+1]:
            k, j = i-1, i+1
            while k > 0 and j < n-1 and s[k-1] == s[j+1]:
                k -= 1
                j += 1
            if j-k+1 > lp:
                lp = j-k+1
                p = s[k:j+1]
    return p


if __name__ == '__main__':
    l = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    # cProfile.run('longestPalindrome(l)')
    # print(longestPalindrome(l))
    lp = LineProfiler()
    lp_wrapper = lp(longestPalindrome)
    lp_wrapper(l)
    lp.print_stats()
