def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0
    desired_substring = ''
    ############################ Insert your code here############################
    #如果只要求最大值的，直接if a < b, a =b
    #不要把所有值添加到一个列表里最后再挑
    if len(word)==1:
        desired_length =1
        desired_substring =word
    else:
        try_string = word[0]
        last_value =ord(word[0])
        for i in word[1:]:
    #    for i in range(1,len(word)):
            if ord(i) -last_value == 1:     #如果能直接用就不要再转到list 再转回来
                try_string += i
            else:
                if len(try_string)> desired_length:
                    desired_length = len(try_string)
                    desired_substring = try_string
                try_string = i        #每次停止累加 完，要把 第一个字符改成目前的这个
            last_value = ord(i)
        if len(try_string)> desired_length:
                desired_length = len(try_string)
                desired_substring = try_string
    ############################################################################ 
    

    
    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
