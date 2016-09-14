#!/usr/bin/python
import sys
import imghdr
import os
import PIL
#import Image
from PIL import Image
from PIL import ImageFile

file_name_html = sys.argv[1] + '.html' 
f = open(file_name_html,'w')
f.write("""<html>
<head><title>Desplegados Mosaico Empleos</title></head>
<body><h1>Desplegados """+file_name_html+"""</h1>""")

dir_path_images = "/desarrollo/avisox/external/img/"+sys.argv[1]+"/"
dir_www_path_images = sys.argv[1]+"/"
mylist = os.listdir(dir_path_images)
for items in mylist:
        f.write(items+'<br />')
        filename = dir_path_images+items
        ispath = os.path.isdir(filename)
        if ispath:
            #do nothing
             f.write("is a path </br></br>")
        else:    
            result = imghdr.what(filename)
            if result:
                f.write("file format:")
                f.write(result+'<br />\n')
                print(filename)
           
                try:
                    im=Image.open(filename)
                    verify_data = im.verify()
                    f.write('pasando por verify <br />\n')
#                    f.write('en img <img src="http://img.avisooportuno.mx/img/'+dir_www_path_images+items+'" widht="100%" /><br />\n')
#                    f.write('en www <img src="http://www.avisooportuno.mx/img/'+dir_www_path_images+items+'"  widht="100%" /><br />\n')
                    # do stuff
                except IOError:
                    # filename not an image file_exists
                    f.write("<h4>error</h4>"+'<br />\n')
                    print("error en"+filename)
                gif = Image.open(filename)
                try:
                    gif.seek(1)
                except EOFError:
                    isanimated = False
                    f.write('not animated <br /><br />\n')
                else:
                    isanimated = True
                    f.write('is animated TRUE <br /><br />\n')
            else:
                f.write('<h4>Can not identify file: '+filename+' </h4><br />\n')

                f.write('en img <img src="http://img.avisooportuno.mx/img/'+dir_www_path_images+items+'" widht="100%" /><br />\n')
                f.write('en www <img src="http://www.avisooportuno.mx/img/'+dir_www_path_images+items+'"  widht="100%" /><br />\n')


f.write("""</body>
</html>""")
f.close()