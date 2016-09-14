#!/usr/bin/python
import imghdr
import os
import PIL
#import Image
from PIL import Image
from PIL import ImageFile
"""result = imghdr.what('/desarrollo/avisox/external/img/desp-me/14291521.gif')
if result:
    print "file format:", result
else:
    print "cannot identify file" """

f = open('desp-me.html','w')
f.write("""<html>
<head><title>Desplegados Mosaico Empleos</title></head>
<body><h1>Desplegados Mosaico Empleos</h1>""")

dir_path_images = "/desarrollo/avisox/external/img/desp-me/"
mylist = os.listdir(dir_path_images)
for items in mylist:
        f.write(items+'<br />')
        filename = dir_path_images+items
        result = imghdr.what(filename)
        if result:
            f.write("file format:")
            f.write(result+'<br />\n')
        else:
            f.write("cannot identify file"+'<br />\n')

        try:
            im=Image.open(filename)
            verify_data = im.verify()
            f.write('pasando por verify <br />\n')
            # do stuff
        except IOError:
            # filename not an image file_exists
            f.write("<h4>error</h4>"+'<br />\n')
        gif = Image.open(filename)
        try:
            gif.seek(1)
        except EOFError:
            isanimated = False
            f.write('not animated <br /><br />\n')
        else:
            isanimated = True
            f.write('is animated TRUE <br /><br />\n')
f.write("""</body>
</html>""")
f.close()