from matplotlib import pyplot as plt
import numpy as np
from skimage.transform import rescale, resize, downscale_local_mean
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import scipy.stats as st

import struct

# load dataset

with open('train-labels.idx1-ubyte','rb') as f:
    magic, size = struct.unpack(">II", f.read(8))
    labels = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))

with open('train-images.idx3-ubyte','rb') as f:
    magic, size = struct.unpack(">II", f.read(8))
    nrows, ncols = struct.unpack(">II", f.read(8))
    data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
    data = data.reshape((size, nrows, ncols))


# digits = datasets.load_digits()
n_samples = len(data)
print(n_samples, len(labels))
# flatten
print(data[0].min(), data[0].max())
data = data.reshape((n_samples, -1))
# # create classifier
clf = svm.SVC()
# # train
n = 20000
clf.fit(data[:n], labels[:n])

def gkern(n, std=5):
    """Returns a 2D Gaussian kernel of size nxn"""

    x = np.linspace(-std, std, n + 1)
    kern1d = np.diff(st.norm.cdf(x))
    kern2d = np.outer(kern1d, kern1d)
    return kern2d / kern2d.sum()


def parse(d):
    width, height = d["width"], d["height"]
    M = np.zeros((width, height))
    for line in d["lines"]:
        brushsize = line["brushRadius"] * 2
        kernel = np.ones((brushsize, brushsize))
        for point in line["points"]:
            x, y = int(point["x"]), int(point["y"])

            leftout = brushsize // 2 - y if brushsize // 2 > y else 0
            rightout = brushsize // 2 + y - width if brushsize // 2 + y > width else 0
            topout = brushsize // 2 - x if brushsize // 2 > x else 0
            bottonout = (
                brushsize // 2 + x - height if brushsize // 2 + x > height else 0
            )

            # corner of the window
            l = y - brushsize // 2 + leftout
            r = y + brushsize // 2 - rightout
            t = x - brushsize // 2 + topout
            b = x + brushsize // 2 - bottonout
            # print(f"x {x} y {y} br {brushsize}")
            # print(f"l {l} r {r} t {t} b {b}")
            # print(leftout, brushsize - rightout, topout, brushsize - bottonout)
            cropped_kernel = kernel[
                leftout : brushsize - rightout, topout : brushsize - bottonout
            ]
            M[l:r, t:b] = cropped_kernel
    # plt.imshow(M)
    # plt.show()
    # plt.figure()
    flat = resize(M, (nrows, ncols)).reshape((1, -1))
    # normalize between 0 and 16. same as dataset
    normalized = (flat - flat.min()) / flat.ptp() * 255
    # plt.imshow(normalized.reshape((nrows, ncols)))
    # plt.show()
    prediction, *_ = clf.predict(normalized)

    return prediction


if __name__ == "__main__":
    ex = {
        "lines": [
            {
                "points": [
                    {"x": 219.48639276021905, "y": 65.70224471437163},
                    {"x": 219.48639276021905, "y": 65.70224471437163},
                    {"x": 219.48639276021905, "y": 65.70224471437163},
                    {"x": 216.5969312234745, "y": 66.61381850510344},
                    {"x": 203.0782569961115, "y": 75.39488481666824},
                    {"x": 195.11258932831075, "y": 82.09123854868939},
                    {"x": 178.6344750308965, "y": 97.55300534348818},
                    {"x": 166.95487744600578, "y": 113.0450475297346},
                    {"x": 158.67556425622007, "y": 127.19266532876804},
                    {"x": 149.7455549385734, "y": 145.6971512865506},
                    {"x": 139.12594802520601, "y": 178.04382923180688},
                    {"x": 133.56975436699364, "y": 197.8747011395373},
                    {"x": 129.37026159145114, "y": 213.8204885948844},
                    {"x": 126.07870801903366, "y": 234.54858076681137},
                    {"x": 125.14119835256052, "y": 245.43392124340417},
                    {"x": 125.9909690416141, "y": 256.42451456930297},
                    {"x": 129.02355960988925, "y": 266.0011177788585},
                    {"x": 136.0590946621225, "y": 277.36269752624287},
                    {"x": 143.1878461164008, "y": 283.76513456289354},
                    {"x": 148.609018845465, "y": 286.9300751414358},
                    {"x": 160.41385649103557, "y": 290.6337529319002},
                    {"x": 170.98983694982286, "y": 292.4049494698171},
                    {"x": 184.80882322677826, "y": 292.497158649809},
                    {"x": 190.95777448069694, "y": 291.5645780932126},
                    {"x": 196.05291715280174, "y": 289.1801741169951},
                    {"x": 198.76910971217535, "y": 287.5073340289944},
                    {"x": 204.5770433085137, "y": 281.8203356328775},
                    {"x": 210.1313953482189, "y": 267.85118718650307},
                    {"x": 211.92004002431653, "y": 260.4188336611061},
                    {"x": 212.6918785911788, "y": 252.71940620171958},
                    {"x": 212.5055917393931, "y": 247.77587382307476},
                    {"x": 210.3230341377255, "y": 239.3623271129732},
                    {"x": 208.28391386813325, "y": 234.6852491924822},
                    {"x": 201.68521064437792, "y": 228.56308905515561},
                    {"x": 191.7844966950807, "y": 223.54901024054624},
                    {"x": 180.8119004068521, "y": 220.7967313766086},
                    {"x": 163.1983325883421, "y": 220.10399020628924},
                    {"x": 157.97322965725508, "y": 221.10399364573297},
                    {"x": 156.29591346389492, "y": 221.76235192670202},
                    {"x": 153.23965278278638, "y": 223.64968363329731},
                    {"x": 152.08205394236384, "y": 224.40073369304184},
                    {"x": 152.08205394236384, "y": 224.40073369304184},
                ],
                "brushColor": "#663399",
                "brushRadius": 15,
            }
        ],
        "width": 400,
        "height": 400,
    }
    p = parse(ex)
    print(p)