def longest_palindrome1(s):
    if len(s) <= 1:
        return s
    longest = 0
    longest_str = None
    for i in range(len(s)):
        cur_longest = 1
        l = i-1
        r = i+1
        if l < 0: 
            if s[i] == s[r]:
                longest = 2
                longest_str = s[i:r+1]
            else:
                longest_str = s[i]
            continue
        if r >= len(s):
            continue
        if s[l] == s[i] and s[l] != s[r]:
            l -= 1
            cur_longest += 1
        if s[r] == s[i] and s[l] != s[r]:
            r += 1
            cur_longest += 1
        if s[l] == s[i] and s[l-1] == s[r] and l>0:
            l -= 1
            cur_longest += 1
        while l>=0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            cur_longest += 2
        if cur_longest > longest:
            longest = cur_longest
            longest_str = s[l+1:r]
        
    return longest_str
        
def longest_palindrome(s):
    if len(s) <= 1:
        return s
    longest = 0
    longest_pal = None
    for i in range(len(s)):
        l = i-1
        r = i+1
        cur_length = 1
        center = True
        while True:
            
            if l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cur_length += 2
                if l>=0 and s[l] != s[i]:
                    center = False
                if r<len(s) and s[r] != s[i]:
                    center = False
            elif r < len(s) and s[r] == s[i] and center:
                r += 1
                cur_length += 1
            elif l > 0 and s[l] == s[i] and center:
                l -= 1
                cur_length += 1
            else:
                break
        if cur_length > longest:
            longest = cur_length
            longest_pal = s[l+1:r]
    if longest_pal[0] != longest_pal[-1]:
        longest_pal = longest_pal[0:-1]
    return longest_pal

def convert(s: str, numRows: int) -> str:
    matrix = []
    for _ in range(numRows):
        matrix.append([])
    string = [*s]
    i = 0
    while string:
        if i != numRows:
            matrix[i].append(string.pop(0))
            i += 1
        else:
            counter = numRows - 2
            for j in range(numRows-2):
                for k in range(i):
                    if k != counter:
                        matrix[k].append('')
                    elif string:
                        matrix[k].append(string.pop(0))
                counter -= 1
            i  = 0
    lst = []
    for row in matrix:
        lst += row
    output = ''.join(lst)
    return output

#new

def myAtoi(s: str) -> int:
    if s == "":
        return 0
    i = 0
    output = ''
    while s[i] == ' ':
        i+=1
    if s[i] == "-":
        output += "-"
        i += 1
    elif s[i] == "+":
        i += 1
    elif s[i].isnumeric():
        pass
    else:
        return 0
    while i < len(s):
        if s[i].isnumeric():
            output += s[i]
            i += 1
        else:
            break
    if output == "-" or output == "":
        return 0
    if int(output) < -2**31:
        return -2**31
    if int(output) > 2**31 - 1:
        return 2**31 - 1
    return int(output)


print(myAtoi(" "))