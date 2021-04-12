from matplotlib import pyplot as plt
import numpy as np
from skimage.transform import rescale, resize, downscale_local_mean
from sklearn import datasets, svm, metrics
from sklearn.preprocessing import StandardScaler, scale
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import scipy.stats as st
import pickle
import sys, os

import struct

# load dataset

def create_classifier(use_old, n=60_000):
    # use old classifier

    with open("train-labels.idx1-ubyte", "rb") as f:
        magic, size = struct.unpack(">II", f.read(8))
        labels = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder(">"))

    with open("train-images.idx3-ubyte", "rb") as f:
        magic, size = struct.unpack(">II", f.read(8))
        nrows, ncols = struct.unpack(">II", f.read(8))
        data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder(">"))
        data = data.reshape((size, nrows, ncols))

    if use_old:
        with open("clf.pickle", "rb") as f:
            clf = pickle.load(f)
            return clf, nrows, ncols

    # digits = datasets.load_digits()
    n_samples = len(data)
    # flatten
    data = data.reshape((n_samples, -1))
    # plt.imshow(scale(data[2]).reshape((28, 28)))
    # plt.colorbar()
    # plt.show()


    # create classifier
    clf = make_pipeline(StandardScaler(), svm.SVC())
    # train
    print(f"Started training with {n} images")
    clf.fit(data[:n], labels[:n])
    with open("clf.pickle", "wb") as f:
        pickle.dump(clf, f)

    print(f"Finished training")
    return clf, nrows, ncols


def gkern(n, std=5):
    """Returns a 2D Gaussian kernel of size nxn"""

    x = np.linspace(-std, std, n + 1)
    kern1d = np.diff(st.norm.cdf(x))
    kern2d = np.outer(kern1d, kern1d)
    return kern2d / kern2d.sum()


def parse(d, clf, nrows, ncols):
    # print(d)
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
    
    flat = resize(M, (nrows, ncols)).reshape((1, -1)) * 255
    # mean of 0 and std of 1. same as dataset
    # scaled = (flat[0]).reshape((1, -1))
    # print(scaled)
    # plt.imshow((flat.reshape((nrows, ncols))))
    # plt.colorbar()
    # plt.show()
    prediction, *_ = clf.predict(flat)

    return prediction


if __name__ == "__main__":
    ex = {
        "lines": [
            {
                "points": [
                    {"x": 115.6583325145006, "y": 76.43813850353384},
                    {"x": 115.6583325145006, "y": 76.43813850353384},
                    {"x": 115.6583325145006, "y": 76.43813850353384},
                    {"x": 115.6583325145006, "y": 76.43813850353384},
                    {"x": 115.6583325145006, "y": 76.43813850353384},
                    {"x": 115.6583325145006, "y": 76.43813850353384},
                    {"x": 115.6583325145006, "y": 76.43813850353384},
                    {"x": 115.6583325145006, "y": 76.43813850353384},
                    {"x": 115.6583325145006, "y": 76.43813850353384},
                    {"x": 115.6583325145006, "y": 76.43813850353384},
                    {"x": 132.00530618449102, "y": 76.9244303365973},
                    {"x": 149.03944766471463, "y": 78.30904228819172},
                    {"x": 166.062702026294, "y": 80.05613078663563},
                    {"x": 183.12590303822535, "y": 82.54751953006696},
                    {"x": 189.25354359314346, "y": 83.82752591571116},
                    {"x": 201.12494093708858, "y": 85.55412167460963},
                    {"x": 217.24552913997138, "y": 88.86621070410068},
                    {"x": 222.58156354479468, "y": 90.59081521281864},
                    {"x": 227.66168998124957, "y": 92.35152661040836},
                    {"x": 231.1956768245137, "y": 94.05950692707408},
                    {"x": 233.5478362748785, "y": 95.3861441092416},
                    {"x": 235.12026211108395, "y": 96.47017231388331},
                    {"x": 236.25210832781977, "y": 97.28277817056187},
                    {"x": 238.213935690569, "y": 99.10781290471733},
                    {"x": 239.156605483604, "y": 100.19933596934715},
                    {"x": 240.06749716403706, "y": 101.48633272473086},
                    {"x": 241.28337646940983, "y": 103.73041044053826},
                    {"x": 242.29976631956683, "y": 106.86598518878392},
                    {"x": 242.2191007108065, "y": 111.28325038012485},
                    {"x": 241.87889472450496, "y": 113.42925630213517},
                    {"x": 240.17263146213625, "y": 118.03006576538759},
                    {"x": 236.36702565875555, "y": 124.10967272502694},
                    {"x": 229.8214654893983, "y": 130.14603355424055},
                    {"x": 222.6712530920848, "y": 136.98610866226443},
                    {"x": 214.850314754223, "y": 142.42768893711187},
                    {"x": 207.50565950486168, "y": 146.48201570848278},
                    {"x": 204.71835483684475, "y": 147.88524503414916},
                    {"x": 198.7236607321116, "y": 150.8957973261231},
                    {"x": 196.72514969450188, "y": 151.89876321130035},
                    {"x": 192.11904204350836, "y": 153.76827935587946},
                    {"x": 188.0209109896842, "y": 155.53366946277288},
                    {"x": 187.1610747878977, "y": 155.87325617299044},
                    {"x": 184.78910847663107, "y": 157.0281425120946},
                    {"x": 184.38228461625002, "y": 157.26392782587817},
                    {"x": 183.9420613494669, "y": 157.56147201829285},
                    {"x": 183.47820017306552, "y": 157.92164936686095},
                    {"x": 182.53853401892272, "y": 158.84955759528674},
                    {"x": 181.6062096791458, "y": 160.26336630756475},
                    {"x": 181.2947072033361, "y": 161.0760953809145},
                    {"x": 181.21728751372714, "y": 161.48787745091678},
                    {"x": 181.6268985039093, "y": 163.51824063635277},
                    {"x": 184.3706601740188, "y": 168.6835836000975},
                    {"x": 189.44866138121887, "y": 174.9550886747545},
                    {"x": 195.15034467163468, "y": 180.17670802841795},
                    {"x": 206.70899389764827, "y": 187.10911962213538},
                    {"x": 214.51265981094647, "y": 191.4489523602132},
                    {"x": 223.5114833562931, "y": 196.45106830345884},
                    {"x": 227.14565789608776, "y": 198.16429216440687},
                    {"x": 233.7112572963937, "y": 202.10534734702787},
                    {"x": 239.82273963100778, "y": 205.9233123326632},
                    {"x": 245.69456295420545, "y": 210.70438776113392},
                    {"x": 249.6077784593743, "y": 214.70391838620205},
                    {"x": 253.91036003833784, "y": 219.417970398708},
                    {"x": 256.42024048303176, "y": 223.24597398491872},
                    {"x": 257.9678939273568, "y": 225.90754784848338},
                    {"x": 260.00845938130743, "y": 230.36866450196413},
                    {"x": 261.99284391899363, "y": 235.9700741043447},
                    {"x": 264.066003988735, "y": 241.94442172294865},
                    {"x": 265.7209456885238, "y": 250.4996579409724},
                    {"x": 266.7512315507962, "y": 260.3464028137025},
                    {"x": 265.42925607293967, "y": 271.36666955929775},
                    {"x": 264.8107473534586, "y": 275.4186535716483},
                    {"x": 261.56912276646915, "y": 285.82431486542447},
                    {"x": 257.21495895818276, "y": 293.01605223531453},
                    {"x": 249.20486648341432, "y": 303.6849017905938},
                    {"x": 242.37675734519053, "y": 310.6888151658103},
                    {"x": 233.15010111012288, "y": 318.5175105868996},
                    {"x": 225.3214716629971, "y": 323.16020248262623},
                    {"x": 222.58286606552858, "y": 324.6241353786507},
                    {"x": 213.76249169227327, "y": 328.97382382776277},
                    {"x": 203.21094485321487, "y": 333.00168045410226},
                    {"x": 196.34448856745823, "y": 335.3693988853984},
                    {"x": 185.72016670135983, "y": 337.70487803688286},
                    {"x": 172.93535349283013, "y": 339.0373299860169},
                    {"x": 160.9838274752677, "y": 339.65845063983716},
                    {"x": 157.9896476306587, "y": 339.7829030399007},
                    {"x": 146.99718163506614, "y": 340.02118690144164},
                    {"x": 140.99874734432734, "y": 340.10786555145364},
                    {"x": 135.99937582867886, "y": 340.15885832496576},
                    {"x": 132.9996005274455, "y": 340.1833358450998},
                    {"x": 129.9997443363736, "y": 340.20291825886034},
                    {"x": 128.99978215612086, "y": 340.20894366802423},
                    {"x": 128.95237327033067, "y": 340.21318014896724},
                    {"x": 128.95237327033067, "y": 340.21318014896724},
                    {"x": 128.95237327033067, "y": 340.21318014896724},
                    {"x": 128.95237327033067, "y": 340.21318014896724},
                ],
                "brushColor": "#663399",
                "brushRadius": 20,
            }
        ],
        "width": 400,
        "height": 400,
    }
    use_old = os.path.exists("clf.pickle") and (len(sys.argv) == 1 or sys.argv[1] != "-t")
    clf, nrows, ncols = create_classifier(use_old)
    p = parse(ex, clf, nrows, ncols)
    print(p)
