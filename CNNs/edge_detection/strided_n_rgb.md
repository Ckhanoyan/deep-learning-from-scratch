# Strided Convolution 

In a regular convolution, we just slide the filter like 3x3 over the image as it will be repeated over the entire image. For example, if our stride is 1, then the filter will jsut slide over the image one pixel at a time. Now if our stride is 2 (s = 2), then our filter will slide over the image two pixels at a time. What does that even do anyways? 

* It helps reduce the spatial dimensions or the size of the output feature map
* It also helps reduce computational costs and the amount of memory required for storing intermediate results
* Larger strides will result in greater downsampling of the input image so if s = 2, the output will have about half the spatial dimensions of the input. Example: input image of 5x5 with a filter of 3x3 (also with s = 2), the output image will become 2 x 2.

# Convolutions on RGB Images 

RGB images have three channels, Red, Green, and Blue, each with pixel values. An RGB image is represented as a 3D matrix (height x width x 3). 
