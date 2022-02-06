#this is the part where we are going to shuffle and generate password 
#python 'random' module is used here to pick random from letters,numbers and punctuations
#then it is re shuffled by string_utilis 
#remember that in order to  use string_utilis you have to install it first.check readme.md.

import random
import string

import string_utils


def main1():
    letter = list(string.ascii_letters)
    punct = list(string.punctuation)
    num = 6,3,2,9,5,1,7,0,8,4

    c1 = random.choice(num)
    c2 = random.choice(num)
    c3 = random.choice(num)
    tmix = letter + punct 



    rnum = c1 - c2
    
    rnum = list(range(999999))
    random.shuffle(rnum)


    final_num = str(random.choice(rnum))

    
    while len(final_num) != 5:
        print()
        if len(final_num) > 5:
            final_num = final_num[:-1]
        

        elif len(final_num) < 5:
            c1 = str(c1)
            final_num = final_num + c1
        elif len(final_num) == 5:
            print()
  

    tmix1 = random.choice(tmix)
    tmix2 = random.choice(tmix)
    tmix3 = random.choice(tmix)
    tmix4 = random.choice(tmix)
    tmix5 = random.choice(tmix)
    tmix6 = random.choice(tmix)
    tmix7 = random.choice(tmix)

    tpw = [tmix1 + tmix2 + tmix3 + tmix4 + tmix5 + tmix6 + tmix7 + final_num]
    random.shuffle(tpw)
    strpw = ' '.join([str(elem) for elem in tpw])
    u2pw = string_utils.shuffle(strpw)
    u1pw = string_utils.shuffle(u2pw)
    global vpw
    vpw = string_utils.shuffle(u1pw)
    
    print(vpw)
    
main1()


    




        
    
    
