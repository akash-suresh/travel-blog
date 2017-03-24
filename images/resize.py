
# coding: utf-8

# In[4]:

#!/usr/bin/env python

from PIL import Image
import os, sys


# In[11]:

def resizeImage(infile, dir, output_dir="", size=(1500,1000)):
     outfile = os.path.splitext(infile)[0]
     extension = os.path.splitext(infile)[1]

     if extension.lower()!= ".jpg":
        return

     if infile != outfile:
        try :
            im = Image.open(dir+os.sep+infile)
            im = im.resize(size, Image.ANTIALIAS)
            quality_val = 85
            im.save(output_dir+os.sep+outfile+extension,"JPEG", quality=quality_val)
        except IOError:
            print "cannot reduce image for ", infile



# In[12]:

if __name__=="__main__":
    #dir = os.getcwd()
    
    if len(sys.argv[1:]) > 0:
        args = sys.argv[1:]

        if args[0] == "-d":
            if args[1]!="./":
                dir = args[1]
    dir = 'Large'
    output_dir = dir+os.sep+"resized"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for file in os.listdir(dir):
        resizeImage(file,dir,output_dir=output_dir)


# In[ ]:



