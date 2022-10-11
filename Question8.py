def isAnagram(s: str, t: str) -> bool:

        x = [s[idx] for idx in range(0,len(s))]
        x.sort()
        y = [t[idx] for idx in range(0,len(t))]
        y.sort()
 
        if (x == y):print("TRUE")
        else: print("FALSE")

s1 ="paint"
s2 ="iantpi"
isAnagram(s1, s2)

# The time complexity for the code is O(nlogn).
