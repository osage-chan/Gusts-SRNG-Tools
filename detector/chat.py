from depend.screenshotter import screenshot

chat_button_bbox = (66,10,86,29)

def is_open():
    r,g,b = screenshot().crop(chat_button_bbox).resize((1,1),3).getpixel((0,0))
    return r>200 and g>200 and b>200