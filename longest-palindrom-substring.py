def longestPalindrome(s: str) -> str:
    #solution one - O(N^3)
    #------------------------------------------------------------------------
    # length = len(s)
    # maxLength = 0
    # longestPalindromeString = "" 
    # #we are building string with i - where i is nth character
    # #we constantly add character b to
    # #for example for babad
    # #iteration 1
    # #i = b, b = a, newString = ba
    # #iteration 2
    # #i = b, b = b, newString = bab
    # #and so on
    # for i in range(0, length):
    #     newString = s[i]
    #     #indexes shifted by one
    #     for b in range(i, length):
    #         #
    #         if(b != i):
    #             newString += s[b]
            
    #         newStringLength = len(newString)
    #         if(isPalindrome(newString) and newStringLength>maxLength):
    #             maxLength = newStringLength
    #             longestPalindromeString = newString
    #         else:
    #             #ignore and go to the next loop iteration
    #             continue


    # return longestPalindromeString

    
    #solution 2
    #use two pointers that expand from the center
    maxLength = 0
    start = 0

    for i in range(0, len(s)):
        #for odd
        left, right = i,i
        newLength = 0

        while left >=0 and right <len(s) and s[left] == s[right]:
            newLength += right-left+1
            if(newLength > maxLength):
                maxLength = newLength
                start = left
            left-= 1
            right+= 1
        
        #for even
        left, right = i,i+1
        newLength = 0

        while left >=0 and right <len(s) and s[left] == s[right]:
            newLength += right-left+1
            if(newLength > maxLength):
                maxLength = newLength
                start = left
            left-= 1
            right+= 1

        

    return s[start:start+maxLength]


def isPalindrome(s: str) -> bool:
    length = len(s)
    # to reverse string i use slicing
    # s[length:None:-1]
    # stringName[start:end:step]
    # can also be rewritten as [::], but i think writing this way is more readable
    reversedString = s[length:None:-1]
    if(s == reversedString):
        return True
    else:
        return False

print(longestPalindrome("cbbd"))