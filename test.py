import imghdr

result = imghdr.what('14288757.gif')

if result:
    print "file format:", result
else:
    print "cannot identify file"