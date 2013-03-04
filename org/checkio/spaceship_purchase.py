'''
Created on 2013-3-4

@author: congji
'''
#checkio([150, 50, 1000, 100]) == 450
#Sofi: 200
#Oldman: 900
#Sofi: 250
#Oldman: 800
#Sofi: 300
#Oldman: 700
#Sofi: 350
#Oldman: 600
#Sofi: 400
#Oldman: 500
#Sofi: 450
#... old man will be ok with it, because his next proposition will be lower than 450.
 
# a bit shorter example
#checkio([500, 300, 700, 100]) == 700
#Sofi will be ok with 700 because his next proposition will be higher

def purchase(data):
    [sofi, sofi_step, oldman, oldman_step] = data
    print sofi, sofi_step, oldman, oldman_step
    
    deal = False
    while not deal:
        if sofi + sofi_step > oldman:
            deal = oldman
            break;
        sofi = sofi + sofi_step
        if oldman - oldman_step < sofi:
            deal = sofi
            break;
        oldman = oldman - oldman_step    
        continue
    
    
    return deal
    

print purchase([500, 300, 700, 100])