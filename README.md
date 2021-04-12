
<h1 align="center">
  Digit doodle guesser
</h1>

## 🚀 Quick start
- **Installation**

1. Firstly, clone the directory: `git clone https://github.com/thdb-theo/doodle-guessing/`
2. Then, locate the directory and the start the server with `npm run develop`
3. Lastly, enter the directory `src/api` and the start the backend server with `python listener.py`. Add the `-t` flag if you want to train the classifier. Otherwise it will use the pickled classifier in `clf.pickle`
4. Now you can open `localhost:8000` in your favourite webbrowser and start drawing!

- **What is this**

    On this site you can draw a digit and the machine learing algorithm will guess what you have drawn. 


-  **How?**

    The classifier uses a machine learning algorithm called a [Support-vector machine](https://en.wikipedia.org/wiki/Support-vector_machine) (SVM). The machine has been trained using the [MNIST](http://yann.lecun.com/exdb/mnist/) database.
    
    When you draw a digit, we send the data to a separate web server using a HTTP requst. The server is written in Python which parser the data and creates a matrix which should look like the drawing that was sent. Unfortunately, the size of the canvas and the size of the training images is vastly different. To scale down the image, we use bilinear intorpolation. We send the scaled down image through the classifier which guesses what digit was drawn.
 

-  **Examples**

Hurray! We guessed correctly!
<p float="left">
<img src="media/three-example.png" alt="alt text" height="300">
<img src="media/eight-example.png" alt="alt text" height="300">
</p>

However it is far from perfect :(

<img src="media/nine-wrong.png" alt="alt text" height="300">

