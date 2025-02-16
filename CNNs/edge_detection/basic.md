# Edge Detection 

Edge detection is a technique used in image processing to identify points in an image, e.g., boundaries between different regions or significant changes in pixel values. The goal of edge detection is basically to find the edges and highlight that, but how do we do that? 

![image](https://github.com/user-attachments/assets/d3ac0c02-26dc-49dd-8de8-d9d97dd74b97)

## Sobel Filter 

It is one of the most commonly used filters for edge detection, which it works by emphasizing the changes in intensity in both horizontal and vertical directions. It uses two filters to detect horizonatal and vertical edges. For coding, it may look like this below: 

*Horizontal edge*

    Sobel_x = [[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]]

*Vertical edge*

    Sobel_y = [[-1, -2, -1],
               [ 0,  0,  0],
               [ 1,  2,  1]]

And then you may get the overall edge intensity by combining the results from both the convolutions 

    Edge_magnitude = sqrt(Sobel_x^2 + Sobel_y^2)

### Scharr Filter 

The same goes to Scharr Filter, but it places more emphasis on the center pixel - which makes it more sensitive to edge detection. The primary difference is the weights used in the filters. 

*Horizontal Edge*

    Scharr_x = [[-3, 0, 3],
                [-10, 0, 10],
                [-3, 0, 3]]

*Vertical Edge*

    Scharr_y = [[-3, -10, -3],
                [ 0,   0,  0],
                [ 3,  10,  3]]

### Padding

Now, what is padding? It refers to adding extra pixels (usually zero) around the border of the input image. Why....??? Because it is used to control the spatial dimensions of the output after the convolution operation and to ensure that the filter is applied to every pixel of the image, including those near the edges. There are two main types of padding in CNNs. 

* Valid Padding: no padding is applied to the image, which means that the filter is only applied to regions where it can fully fit inside the image. It also means that the output size will be smaller than the input size (e.g., 5x5 will become 3x3).
* Same Padding: padding is applied to the image so that way the output will have the same size as the input image. The filter will be padded with zeros around the edges ensuring that every pixel in the input is processed (e.g., 5x5 > 5x5).

![image](https://github.com/user-attachments/assets/84414e72-a0d0-47cd-97a0-2e58d57a42e5)

