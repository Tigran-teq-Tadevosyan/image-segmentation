# Image Segmentation

## Description
This little program is predicting edges of objects in the images bassed on the (R,G,B) values change in the image.
Right now it only works with 'jpg' images
Program was tested on 'Ubuntu 16.04' with 'Python 3.6.5 |Anaconda, Inc.|'

## Some Screenshots

### Original Image
![alt text](https://raw.githubusercontent.com/Tigran-teq-Tadevosyan/image-segmentation/master/sample-images/sample-graphic.jpg)

### After Processing
![alt text](https://raw.githubusercontent.com/Tigran-teq-Tadevosyan/image-segmentation/master/result/Screenshot.png)

## Installation and Excution

1. Install PyQt5
    ```bash
    pip install foobar
    ```
2. Run the program by going to the directory
    * If you are using windows run
    ```bash
    pyuic5 -x ./main.ui -o ./window_ui.py
    python start.py
    ```
    * If you are using OSX/Linux run
    ```bash
    sudo chmod -x ./run.sh #this will make 'run.sh' shell script executable
    ./run.sh
    ```
## License
[MIT](https://choosealicense.com/licenses/mit/)