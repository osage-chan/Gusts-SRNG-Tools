import depend.screenshotter as screenshotter
import _config as cf

def is_black():
    ss = screenshotter.screenshot().resize((100,100))
    w,h = ss.size

    c,m = 0,0

    sens = cf.aura_check_sensitivity
    for x in range(w):
        for y in range(h):
            r,g,b = ss.getpixel((x,y))
            m += 1
            if r<sens and g<sens and b<sens:
                c += 1

    return ((c/m)*100)
