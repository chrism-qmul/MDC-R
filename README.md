## MC corpus with revised ids and bounding boxes

### [UPDATE Feb 6 2025]
There is a folder now with all the data built into the xmls.
- no extra downloads required everything is self-contained in this repo
- images are updated ("basedata/images" contain regular images, "basedata/images-blank" contain images with ids ommitted)
- phrase.xml files in the "markables" folder contain an updated "object" field which is a string that can be evaluated in python (unless it's a special markable like "architect") and will contain a list of blocks of the markable, each is a tuple:
   (block_id, (bbox_top, bbox_bottom, bbox_left, bbox_right), (r_coord, g_coord, b_coord), color, img_path) 
- in the markables folder there are also subfolders with different versions of the object field
    - phrases-full contain xmls with tuples as described above
    - phrases-idonly contain xmls where only the block id's are listed (e.g., object = "[('a1'), ('b2')]")
    - phrases-bbonly contain xmls where only bounding boxes are listed (e.g., object = "[((50, 150, 200, 250)), ((75, 100, 50, 200))]")
      when you decide which one you want to use just copy those phrase.xml files over those already present in the "markables" folder (for example, "cp markables/phrases-idonly/*.xml markables/"), the default variant in markables is the "phrases-full"


### [Old instructions below]

This repository contains:

1) README.md - this file with instructions
2) a link to download the file with regenerated images with new ids -- [link here](https://takelab.fer.hr/data/sodestreamtmp/new-images.tar.gz)
3) remapping.json - a file mapping old ids to new ids for those markables that referred to blocks (also contains bounding box info and other metadata)
4) bbdraw.py - a script to draw/check bounding boxes

### Instructions:

- Download the image archive from the above link (2), extract it to some folder.
- Download remapping.json and bbdraw.py, put them into the same folder as the images.
- You now have access to the regenerated image files, you also have access to remapping.json which when you load it is a list of objects each representing one markable. The fields are:
  - "IMG": e.g.,"B31-A41-C25-1523029167770_31-new-ids.png" --> the corresponding image
  - "EXPERIMENT_ID": e.g., "B31-A41-C25-1523029167770"
  - "MARKABLE_ID": e.g., "markable_75"
  - "BLOCK_LIST": either a string for special entities like "architect" or a list of block objects, each of those is itself another dictionary with these fields:
    - "OLD_ID_PARSED": e.g., "a" or "(red, a)" this is the old block id as it was parsed (by the final tweaked version of the parsing code) after all normalizations and fixes by both annotators and me
    - "COLOR": e.g., "blue"
    - "COORDS": e.g., [-1, 0, -2] (these are the red green and blue directions, respectively)
    - "BBOX": e.g., "(76, 453, 550, 942)" (these are the vertical_min, vertical_max, horizontal_min, horizontal_max, respectively)
    - "ID": e.g., "b6", this is the newly generated id
      
- If necessary you can also draw the bounding boxes for testing purposes, to do that position yourself into the folder with images and call:
  
  python bbdraw.py [image_name] [block_id]

  e.g.,

  python bbdraw.py B31-A41-C25-1523029167770_31-new-ids.png b6

### Notes:
  - any markable that is a reference in the "...*phrase.xml" files should have an entry in remapping.json (EXPERIMENT_ID and MARKABLE_ID should uniquely identify its entry)
  - special markables like "architect" will have a BLOCK_LIST be a string
  - some markables can have an empty BLOCK_LIST (e.g., if all blocks are either unresolvable or invisible)
  - blocks that are ambiguous in the coordinate mapping (letter mapping heuristic failed) are simpliy omitted - about 25 markables have this issue (UPDATE: this has been fixed)
  - invisibility is encoded either explicitly as a special markable with BLOCK_LIST = "to_be_remove:invisible" or implicitly by omitting those blocks of the markable that are out of view (but those that are in view are included normally)
  - BBOX is a string, you need to "eval" it to get the tuple back
  - a bounding box for the entire markable can be generated from individual bounding boxes of it's constituent blocks
  - (not very important) COORDS count the positive direction as 0,1,2 ... and the negative direction -1, -2 ... (so, for example a block that is at +2 is 2 empty spaces away from the corresponding axis, the block at -2 is 1 empty space away)

### TLDR:
- for any markable in the phrase.xml files you can look it up in remapping.json (using experiment_id and markable_id) to get its corresponding (1) new id, (2) corresponding png image with the new id drawn, (3) the spatial coordinates and bounding box (in that new image) for each of its blocks

   
