'''
Created on 2013-2-28

@author: BXC2011032
'''
hello = 'Hello World'
print hello[:4]
print hello[4:] + hello[:4]

def both_ends(s):
    # +++your code here+++
    if len(s) < 2:
        return s
    return s[:2] + s[-2:]

print both_ends('abcdefg')

def fix_start(s):
    # +++your code here+++
    first = s[0]
    return first + s[1:].replace(first, '*')

print fix_start("bubble")

def mix_up(a, b):
    # +++your code here+++
    temp = a[1]
    a = a[:1] + b[1] + a[2:]
    b = b[:1] + temp + b[2:]
    space = ' '
    return space.join([a, b])

print mix_up('mix', 'pod')
print mix_up('dog', 'dinner')
print mix_up('gnash', 'sport')
print mix_up('pezzy', 'firm')