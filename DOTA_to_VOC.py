# Use this script to convert the DOTA dataset to PASCAL VOC format.
import os
from xml.dom.minidom import Document
from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import csv
import cv2
import string

def WriterXMLFiles(imagename, filename, path, box_list, label_list, w, h, d):

    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root)

    nodeFilename = doc.createElement('filename')
    nodeFilename.appendChild(doc.createTextNode(imagename))
    root.appendChild(nodeFilename)

    foldername = doc.createElement("folder")
    foldername.appendChild(doc.createTextNode("JPEGImages"))
    root.appendChild(foldername)

  

    sourcename=doc.createElement("source")

    databasename = doc.createElement("database")
    databasename.appendChild(doc.createTextNode("drones"))
    sourcename.appendChild(databasename)

    annotationname = doc.createElement("annotation")
    annotationname.appendChild(doc.createTextNode("custom"))
    sourcename.appendChild(annotationname)

    imagename = doc.createElement("image")
    imagename.appendChild(doc.createTextNode("custom"))
    sourcename.appendChild(imagename)

    

    root.appendChild(sourcename)

    nodesize = doc.createElement('size')
    nodewidth = doc.createElement('width')
    nodewidth.appendChild(doc.createTextNode(str(w)))
    nodesize.appendChild(nodewidth)
    nodeheight = doc.createElement('height')
    nodeheight.appendChild(doc.createTextNode(str(h)))
    nodesize.appendChild(nodeheight)
    nodedepth = doc.createElement('depth')
    nodedepth.appendChild(doc.createTextNode(str(d)))
    nodesize.appendChild(nodedepth)
    root.appendChild(nodesize)

    segname = doc.createElement("segmented")
    segname.appendChild(doc.createTextNode("0"))
    root.appendChild(segname)

    for (box, label) in zip(box_list, label_list):

        nodeobject = doc.createElement('object')
        nodename = doc.createElement('name')
        nodename.appendChild(doc.createTextNode(str(label)))
        nodeobject.appendChild(nodename)
       
        # The bounding box is in the form of coordinates (xi,yi). We intend to convert that to the format xmin,xmax,ymin,ymax.
        nodebndbox = doc.createElement('bndbox')
        nodexmin = doc.createElement('xmin')
        nodexmin.appendChild(doc.createTextNode(str(min(box[0],box[2]))))
        nodebndbox.appendChild(nodexmin)
        nodeymin = doc.createElement('ymin')
        nodeymin.appendChild(doc.createTextNode(str(min(box[1],box[7]))))
        nodebndbox.appendChild(nodeymin)
        nodexmax = doc.createElement('xmax')
        nodexmax.appendChild(doc.createTextNode(str(max(box[0],box[2]))))
        nodebndbox.appendChild(nodexmax)
        nodeymax = doc.createElement('ymax')
        nodeymax.appendChild(doc.createTextNode(str(max(box[1],box[7]))))
        nodebndbox.appendChild(nodeymax)
        
        nodeobject.appendChild(nodebndbox)
        root.appendChild(nodeobject)
    fp = open(path + filename, 'w')
    doc.writexml(fp, indent='\n')
    fp.close()


def load_annoataion(p):
    '''
    load annotation from the text file
    :param p:
    :return:
    '''
    text_polys = []
    text_tags = []
    if not os.path.exists(p):
        return np.array(text_polys, dtype=np.float32)
    with open(p, 'r') as f:
        for line in f.readlines()[2:]:
            label = 'text'
            
            x1, y1, x2, y2, x3, y3, x4, y4 ,label= line.split(' ')[0:9]
            
            text_polys.append([float(x1), float(y1), float(x2), float(y2), float(x3),float(y3), float(x4), float(y4)])
            text_tags.append(label)

        return np.array(text_polys, dtype=np.int32), np.array(text_tags, dtype=np.str)

if __name__ == "__main__":
    txt_path = './labels/'
    xml_path = './Annotations/'
    img_path = './JPEGImages/'
    print(os.path.exists(txt_path))
    txts = os.listdir(txt_path)
    for count, t in enumerate(txts):
        boxes, labels = load_annoataion(os.path.join(txt_path, t))
        xml_name = t.replace('.txt', '.xml')
        img_name = t.replace('.txt', '.png')
        print(img_name)
        img = cv2.imread(os.path.join(img_path, img_name))
        h, w, d = img.shape
        WriterXMLFiles(img_name, xml_name, xml_path, boxes, labels, w, h, d)

        if count % 1000 == 0:
            print(count)


