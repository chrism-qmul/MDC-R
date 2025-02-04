import sys
import cv2
import numpy as np
import json


# ASSUMPTION: remapping.json and the png images are in the current folder

image_name = sys.argv[1] 
block_id = sys.argv[2] 

# for testing
#image_name = "B31-A41-C25-1523029167770_31-new-ids.png"
#block_id = "b6"

# load bounding box coords
json_data = json.load(open("remapping.json","r"))
img_markables = [x for x in json_data if x["IMG"] == image_name]
for markable in img_markables:
    blocks = [block for block in markable["BLOCK_LIST"] if block["ID"]==block_id]
    if len(blocks) >= 1:
        bbcoords = blocks[0]["BBOX"]
        break
top, bottom, left, right = eval(bbcoords)
print(bbcoords)

# load the image

image_data = cv2.imread(image_name)

# add bbox on it
cv2.rectangle(image_data, (left, top), (right, bottom), (0,0,0), 10)

# display 
cv2.imshow("Image with bounding box:", image_data)
cv2.waitKey(0)
cv2.destroyAllWindows()


