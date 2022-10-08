import numpy as np
import sys
def Sdf2Points(path):
    """
    sdf: x,y,z,v
    points: x,y,z,r,g,b
    """
    out_path = path.split('.')[0]+'.obj'
    fo = open(out_path, 'w')
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            line = line[:-1]
            sp = np.array(line.split(' '), dtype='float')
            d = np.exp(sp[3])
            d = np.clip(d, 0, 1)
            fo.write(sp[0]+' '+sp[1]+' '+sp[2]+' '+str(np.clip(d*255, 0, 255))+' 0 0\n')
    fo.close()

def npz2txt(path):
    """
    npz: deepsdf format: ['pos', 'neg']

    """
    npz = np.load(path)
    sdf1 = npz['pos']
    sdf2 = npz['neg']
    out_path = path.split('.')[0]+'.txt'
    with open(out_path, 'w') as f:
        for i in range(sdf1.shape[0]):
            f.write(str(sdf1[i][0])+' '+str(sdf1[i][1])+' '+\
                    str(sdf1[i][2])+' '+str(sdf1[i][3])+'\n')
        
        for i in range(sdf2.shape[0]):
            f.write(str(sdf2[i][0])+' '+str(sdf2[i][1])+' '+\
                    str(sdf2[i][2])+' '+str(sdf2[i][3])+'\n')

if __name__ == '__main_':
    #sdf = np.load(argv[1])
    npz2txt(sys.argv[1])
