from numpy import load,dot,where,max
from scipy.misc import imread
from skimage import transform
def distinguish(image):
    place=['万寿山', '东宫门', '佛香阁', '排云殿', '昆明湖']
    img = imread(image)
    img = transform.resize(img, (1024, 680))
    test_x = img.reshape((img.shape[0] * img.shape[1] * img.shape[2], 1))
    w=load('w.npy')
    b=load('b.npy')
    print(w)
    print('-------------------')
    print(b)
    print(w.shape)
    print(b.shape)
    test_y=print(dot(w.T,test_x)+b)
    table = where(test_y == max(test_y))
    return place[table[0][0]]
print(distinguish('z.jpg'))