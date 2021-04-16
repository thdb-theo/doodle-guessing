# baseline cnn model for mnist
from numpy import mean
from numpy import std
from matplotlib import pyplot
from sklearn.model_selection import KFold
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD


# load train and test dataset
def load_dataset():
    # load dataset
    (trainX, trainY), (testX, testY) = mnist.load_data()
    print(trainX[0], trainY[0])
    # reshape dataset to have a single channel
    trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
    testX = testX.reshape((testX.shape[0], 28, 28, 1))
    # one hot encode target values
    trainY = to_categorical(trainY)
    testY = to_categorical(testY)
    return trainX, trainY, testX, testY


# scale pixels
def prep_pixels(train, test):
    # convert from integers to floats
    train_norm = train.astype("float32")
    test_norm = test.astype("float32")
    # normalize to range 0-1
    train_norm = train_norm / 255.0
    test_norm = test_norm / 255.0
    # return normalized images
    return train_norm, test_norm


# define cnn model
def define_model():
    model = Sequential()
    model.add(
        Conv2D(
            32,
            (3, 3),
            activation="relu",
            kernel_initializer="he_uniform",
            input_shape=(28, 28, 1),
            padding="same",
        )
    )
    model.add(Conv2D(32, (3, 3), activation="relu", padding="same"))
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(64, (3, 3), activation="relu", padding="same"))
    model.add(Conv2D(64, (3, 3), activation="relu", padding="same"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Flatten())
    model.add(Dense(128, activation="relu", kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation="relu", kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation="softmax"))

    # compile model
    opt = SGD(
        lr=0.01,
        momentum=0.9,
    )
    model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=["accuracy"])
    return model


# evaluate a model using k-fold cross-validation
def evaluate_model(trainX, trainY, testX, testY):
    # prepare cross validation
    # enumerate splits
    # define model
    model = define_model()
    print(model.summary())
    # select rows for train and test
    # fit model
    history = model.fit(
        trainX,
        trainY,
        epochs=10,
        batch_size=32,
        validation_data=(testX, testY),
        verbose=1,
    )

    model.save("model.keras")

    # evaluate model
    _, acc = model.evaluate(testX, testY, verbose=0)
    # stores scores
    return acc


trainX, trainY, testX, testY = load_dataset()
# prepare pixel data
trainX, testX = prep_pixels(trainX, testX)
# evaluate model
acc = evaluate_model(trainX, trainY, testX, testY)
print("> %.3f" % (acc * 100.0))
