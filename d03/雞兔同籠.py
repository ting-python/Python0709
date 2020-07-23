# 雞兔同籠
# 雞加兔=83隻
# 雞=X 兔=Y
# 雞加兔腳=240
''' x + y = z
    2x + 4y = n
    x = (4*z-n)/2
    y = (n-2*z)/2 '''

def calc(z,n):
    x = (4 * z - n) / 2
    y = (n - 2 * z) / 2
    return x,y

c,r = calc(83,240)
print("雞有%d隻" " 兔有%d隻 " " 總隻數=%d " " 總腳數=%d "\
      %(c,r,c+r,2*c+4*r) )



