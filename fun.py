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

# FOOBAR CHALLENGES

'''-- Python cases --
Input:
solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110

Input:
solution.solution("code")
Output:
    100100101010100110100010

Input:
solution.solution("Braille")
Output:
    000001110000111010100000010100111000111000100010'''


def solution_old(s):
    code_table = {
        'a': '100000',
        'b': '110000',
        'c': '100100',
        'd': '100110',
        'e': '100010',
        'f': '110100',
        'g': '110110',
        'h': '110010',
        'i': '010100',
        'j': '010110',
        'k': '101000',
        'l': '111000',
        'm': '101100',
        'n': '101110',
        'o': '101010',
        'p': '111100',
        'q': '111110',
        'r': '111010',
        's': '011100',
        't': '011110',
        'u': '101001',
        'v': '111001',
        'w': '010111',
        'x': '101101',
        'y': '101111',
        'z': '101011',
        ' ': '000000'
        }
    output = ''
    for char in s:
        if char.isupper():
            output += '000001'
        output += code_table[char.lower()]
    return output

'''input:solution.solution([4, 17, 50])
Output:    -1,-1

Input:solution.solution([4, 30, 50])
Output:    12,1'''


from fractions import Fraction

def solution(pegs):
    """
    need to use min of first gear (2) (as last gear must be >= 1) to find the corresponding value of last gear
    then use max of last gear (gap btwn last and second last peg - 1) to find corresponding value of first gear
    create linear relationship and find when first peg is double of last peg
    """
    
    if len(pegs) == 2:
        radii = Fraction(2*(pegs[1]-pegs[0])/3).limit_denominator()
        return [radii._numerator, radii._denominator]

    prev = 2
    for i in range(1,len(pegs)):
        prev = pegs[i] - pegs[i-1] - prev
    min_first = (2,prev)
    
    max_radii = pegs[-1] - pegs[-2] - 1
    prev = max_radii
    for i in range(-1,-1 * len(pegs),-1):
        prev = pegs[i] - pegs[i-1] - prev
    max_last = (prev, max_radii)

    gradient = (max_last[1] - min_first[1])/(max_last[0] - min_first[0])
    intercept = min_first[1] - gradient * min_first[0]

    first_gear_size = Fraction(intercept/(0.5-gradient)).limit_denominator()

    prev = first_gear_size
    for i in range(1,len(pegs)):
        prev = pegs[i] - pegs[i-1] - prev
        if prev < 1 or prev > pegs[i] - pegs[i-1] -1:
            return [-1,-1]

    if first_gear_size >= 2:
        return [first_gear_size._numerator, first_gear_size._denominator]
    else:
        return [-1,-1]
