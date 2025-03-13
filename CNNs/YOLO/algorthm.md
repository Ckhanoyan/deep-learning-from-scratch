# You Only Look Once

Well, yes... It is not that you only live once. It is more about computational costs when you look identify objects once in an image without going through every window slide. Apaprently, this algorithm seems to be one of the most popular methods for real-time object detection in images and videos. So, YOLO treats the entire image as a grid, e.g., 3x3x8, and divides it into smaller cells. Each of these cells is responsible for detecting objects, and YOLO is responsible to predict the bounding box coordinates, e.g., bx, by, bh, bw. You may have something like this below:

Y = pc, bx, by, bh, bw, c1, c2, c3

* Where pc is detecting an object in the image
* bx and by are the center coordinates of the bounding box (relative to the grid cell)
* where bh and bw are the width and height of the bounding box detected within the cell
* where c1, c2, and c3 are the classes, e.g., vehicle, pedistrian, or traffic lights

### How do we confirm that we have the correct or accurate bounding box?

We can use the confidence score for that as well. We can look at the probability that an object exists in the box, and we can use the intersection over union (IoU) between the predicted bounding box and the ground truth box.

### Use cases 

Many use cases can apply to this YOLO algorithm such as autonomous vehicles, surveillance systems, robotics, medical imaging, and augmented reality. 

![image](https://github.com/user-attachments/assets/7cb660eb-5567-4c24-bbdb-2d495d2e6cb6)
