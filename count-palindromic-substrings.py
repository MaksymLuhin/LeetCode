def countSubstrings(s: str) -> int:
    palindromicStrings = []
    numberOfPalindromes = 0
    for i in range(0, len(s)):

        for j in range(2):
            left, right = i, i+j

            while left >= 0 and right <= (len(s)-1) and s[left] == s[right]:
                palindromicStrings.append(s[left:right+1])
                numberOfPalindromes += 1
                #increment/dicrement pointers
                left -= 1
                right += 1
    
    return palindromicStrings


print(countSubstrings("aaa"))