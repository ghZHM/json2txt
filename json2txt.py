# read the comments carefully
# remember to check the path
# before you run it, print the value first to make sure the code works properly
import json
import cv2
import os
all_class={'person':0,'car':1,'truck':2,'bus':3}
# class exactly in the json, check the json file,don't trust the description in website
# note: only the class you want the model to recognize should be here
#
savepath="/home/zhl/BDD100K/bddimages/bdd100k_images/bdd100k/images/100k/val/labels/"
# where you want to save the annotation txt
jsonpath="/home/zhl/BDD100K/bdd100k_labels/bdd100k/labels/100k/val/" # original json format annotation
imgpath="/home/zhl/BDD100K/bddimages/bdd100k_images/bdd100k/images/100k/val/images/"
# original image path just to get size of the image,
json_files = os.listdir(jsonpath)
count=0
for i in json_files:
    infile=jsonpath+i
    with open(infile,'r') as load_f:
        load_dict=json.load(load_f)
    count+=1
    outfile = open(savepath+load_dict['name']+'.txt','w')
    # for example if the name of file is 123456.txt ,you only need '123456'
    # if there is no "name" tag in your json, maybe you can get it from substring of image name

    img_path = imgpath+load_dict['name']+".jpg"
    # print(img_path)
    img = cv2.imread(img_path)
    size = img.shape
    h_img =size[0]
    w_img = size[1]
    print(i)
    for item in load_dict['frames'][0]['objects']:
        # print(item)
        if item['category'] not in ("person","car","truck","bus"):
            continue
        # we only need these class ,so you can change the filter according to your need
        label=all_class[item['category']] # "class" tag in json
        # print(infile)
        xmin = item['box2d']['x1']  # check your json file , maybe it is item['xmin']. same in below
        ymin = item['box2d']['y1']
        xmax = item['box2d']['x2']
        ymax = item['box2d']['y2']

        # print(label)
        # print(xmin,ymin,xmax,ymax)
        x_center=(xmin+xmax)/2/w_img
        y_center=(ymin+ymax)/2/h_img
        w=(xmax-xmin)/w_img
        h=(ymax-ymin)/h_img
        outfile.write(str(label)+" "+str(x_center)+" "+str(y_center)+" "+str(w)+" "+str(h)+"\n")
    outfile.close()
    # break
    # you can use this break to test the file,it will only generate one file


