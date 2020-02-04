# PanCard-Face-Extraction

OBjective of this Project was to extract the user face from pancard. 
I used various computer vision technique steps as follows.

1) Conversion of RBG Image to GrayScale Level, this make image handling easy.
2) Apply thresholding, this will help us to remove white background.
3) Apply Morphological techniques like opening and closing which will remove all small dot patches from image and only give us card 
4) We will Face.xml with haarcascade classifier to extract the face from card.

Results are given below:

# Initial Image
![pan](https://user-images.githubusercontent.com/39022530/73719685-27d86f80-4746-11ea-8a11-aa57ef8a8d00.jpg)

# Extracted Card  
![face2](https://user-images.githubusercontent.com/39022530/73719684-273fd900-4746-11ea-9e2d-73d0ee8ae3d2.PNG)

# Extracted face from card
![face1](https://user-images.githubusercontent.com/39022530/73719683-273fd900-4746-11ea-8528-b7fbab8aad1e.PNG)

