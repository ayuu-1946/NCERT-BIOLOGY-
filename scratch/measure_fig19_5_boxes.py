from PIL import Image
import numpy as np
base='notes/class 11/Ch19_ChemicalCoordinationAndIntegration/assets'
for fid in ['19_5a','19_5b']:
    im=Image.open(f'{base}/fig_{fid}.png').convert('L')
    a=np.array(im)
    # dark-pixel counts by row/column; the box is the long near-black rectangle.
    row=(a<80).sum(axis=1); col=(a<80).sum(axis=0)
    print(fid, 'size', im.size)
    print('rows', sorted(enumerate(row), key=lambda x:x[1], reverse=True)[:12])
    print('cols', sorted(enumerate(col), key=lambda x:x[1], reverse=True)[:12])
