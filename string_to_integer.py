class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1  # set positive by default
        stringRepresnt = ""
        flagSignSet = 0  # 1 if sign set already 0 if was not set
        result = 0
        for i in s:
            # whitespace handling
            if ((i == " " or i == "+") and len(stringRepresnt) == 0 and flagSignSet == 0):
                if (i == "+"):
                    flagSignSet = 1
                continue  # ignore and go to the next character
            # sign handling

            elif (i == "-" and len(stringRepresnt) == 0 and flagSignSet == 0):
                flagSignSet = 1
                sign = -1
            # not digit handling -> stop

            elif (ord(i) < 0x30 or ord(i) > 0x39):
                break
            # digit handling
            else:
                if (len(stringRepresnt) > 0 and stringRepresnt[0] == "0"):
                    stringRepresnt = i
                else:
                    stringRepresnt += i

        if(stringRepresnt != ""):
            result = int(stringRepresnt) * sign

            if(result > (pow(2,31)-1)):
                result = pow(2,31)-1
            elif(result < -pow(2,31)):
                result = -pow(2,31)
            
            return result
        else:
            return 0
