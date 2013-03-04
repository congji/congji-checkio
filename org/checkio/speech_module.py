'''
Created on 2013-3-4

@author: BXC2011032
'''
#checkio(4)=='four'
#checkio(143)=='one hundred forty three'
#checkio(12)=='twelve'
#checkio(101)=='one hundred one'
#checkio(212)=='two hundred twelve'
#checkio(40)=='forty'
single = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tenplus = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    
def get_single(num):
    return num % 10

def get_tens(num):
    return num // 10 

def get_hundreds(num):
    return num // 100

def checkio(num):
    num_str = str(num)
    if len(num_str) == 1:
        return single[int(num_str)]
    elif len(num_str) == 2:
        if num < 20:
            return tenplus[get_single(num)]
        else:
            ten = tens[get_tens(num) - 2]
            if get_single(num) == 0:
                return ten
            else:
                return ten + ' ' + checkio(get_single(num))
    elif len(num_str) == 3:
        hundreds = single[get_hundreds(num)] + ' hundred'
        if num % 100 == 0:
            return hundreds
        else:
            return  ' ' + checkio(num % 100)
    
for x in range(0, 120):
    print checkio(x)
    
print checkio(100)