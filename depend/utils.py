def center_bbox(_bbox):
    bbox = list(_bbox)

    return (round((bbox[0]+bbox[2])/2),round((bbox[1]+bbox[3])/2))