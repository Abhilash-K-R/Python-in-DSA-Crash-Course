'''Assignment 4:
Given two strings s and p, the task is to find the smallest substring in s that contains all characters of p, including duplicates. If no such substring exists, return "". If multiple substrings of the same length are found, return the one with the smallest starting index.

Examples: 

Input: s = "timetopractice", p = "toc"
Output: toprac
Explanation: "toprac" is the smallest substring in which "toc" can be found.

Input: s = "zoomlazapzo", p = "oza"
Output: apzo
Explanation: "apzo" is the smallest substring in which "oza" can be found.
'''
# leetcode 76. Minimum Window Substring


from collections import Counter

def minWindow(s, p):
    if not s or not p:
        return ""
    
    need = Counter(p)
    missing = len(p)
    
    left = 0
    start = 0
    min_len = float('inf')
    
    for right in range(len(s)):
        if need[s[right]] > 0:
            missing -= 1
        
        need[s[right]] -= 1
        
        while missing == 0:
            if right - left + 1 < min_len:
                start = left
                min_len = right - left + 1
            
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            
            left += 1
    
    return s[start:start + min_len] if min_len != float('inf') else ""