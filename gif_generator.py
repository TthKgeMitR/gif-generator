import os
from PIL import Image

save_path = '/Users/admin/Documents/M1/林業/result/pine2/trashed.gif'
jpg_dir_path = '/Users/admin/Documents/M1/林業/result/pine2/trashed/'

images = []

jpg_list = os.listdir(jpg_dir_path)
jpg_list = sorted(jpg_list)

for i in jpg_list:
    name = i.split('.')
    if name[1] == 'jpg' or  name[1] == 'JPG':
        tmp = Image.open(jpg_dir_path + i)
        images.append(tmp)
        print(i)

images[0].save(save_path, save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)
print('saved as: {}'.format(save_path))