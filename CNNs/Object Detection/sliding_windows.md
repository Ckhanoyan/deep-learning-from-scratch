# Sliding Windows Detection ConvNet 

Sliding window detection helps detect objects and landmark in an image, involving sliding a fixed-size window across the entire image at multiple scales. It also makes predictions at each location such as telling you if there is an object. To move a fixed-size window across the image will be done horizonally and vertically to examine every possible object. 

### Pros 

The algorithm is easy to understand and implement, and it does not require any sophisticated architectures or pre-trained models. It does exhaustive search such as checking every part of the image so that way it will not miss an object as long as they fit within the window size. 

### Cons 

Sliding windows can be computationally expensive with large images or multiple scales. It may also overlap regions in the same features leading to unnecessary inefficienes and computational costs. Sometimes, it does not respond well to objects that may have varying sizes and aspect ratios. For more complex objects, sliding windows might struggle to make accurate detection. 

![image](https://github.com/user-attachments/assets/842a6786-70b7-49c6-85ce-75fe98abbfe2)


## There is a modern approach, which is called... YOLO! Let's find out next.
