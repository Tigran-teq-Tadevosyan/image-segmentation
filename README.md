# Image Segmentation

## Description
This little program is predicting edges of objects in the images bassed on the (R,G,B) values change in the image.
Right now it only works with 'jpg' images
Program was tested on 'Ubuntu 16.04' with 'Python 3.6.5 |Anaconda, Inc.|'

## Some Screenshots

### Original Images
![alt text](https://raw.githubusercontent.com/Tigran-teq-Tadevosyan/image-segmentation/master/sample-images/sample-graphic.jpg)
![alt text](https://raw.githubusercontent.com/Tigran-teq-Tadevosyan/image-segmentation/master/sample-images/jpeg-home.jpg)

### After Processing
![alt text](https://raw.githubusercontent.com/Tigran-teq-Tadevosyan/image-segmentation/master/result/Screenshot.png)
![alt text](https://raw.githubusercontent.com/Tigran-teq-Tadevosyan/image-segmentation/master/result/Screenshot2.png)

## Installation and Excution

1. Install PyQt5
    ```shell
    pip install PyQt5
    ```
2. Run the program by going to the directory
    * If you are using windows run
    ```bash
    pyuic5 -x ./main.ui -o ./window_ui.py
    python start.py
    ```
    * If you are using OSX/Linux run
    ```shell
    sudo chmod -x ./run.sh # This will make 'run.sh' shell script executable so it must be executed just ones
    ./run.sh
    ```
## License
[MIT](https://choosealicense.com/licenses/mit/)