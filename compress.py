import os
from datetime import datetime
from PIL import Image

for image_file_name in os.listdir('cabbage/'):
    if image_file_name.endswith(".jpg"):
        now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')

        foo = Image.open('cabbage/'+image_file_name)
        foo = foo.resize((100, 100), Image.ANTIALIAS)
        foo.save('resized/cabbage/' + now + '.jpg', optimize=True, quality=100)
