# Non Max Suppression 

Since I am interested in this CNN using image detection, this algorthm is really interesting as I am hoping to become more familiar with how it works. This non-max suppression (NMS) is one technique used in object detection algorithms to remove redundant bounding boxes and only keep the most accurate or confident ones (high scores or > threshold). 

### Ok, but why is it needed?

We may have multiple bounding boxes with different confidence scores so we do not want to have multiple boxes representing the same object because the boxes may overlay with each other. NMS applies to eliminate such as that and keep only the best bounding box for each object detected in an image. 

We also have to consider IoU where we calculate the intersection over union (see the image below). 

![image](https://github.com/user-attachments/assets/99c191b9-fb3c-45c3-8c6c-317d1101fa00)

* The first step is to figure out the bounding boxes based on their confidence scores that represent how likely it is that the box contains an object. The box with the highest confidence score is processed first.
* Select the Box with the highest score as the "anchor" box.
* Remove boxes with high IoU.
* Repeat until all boxes are processed in an image.
* Output the selected boxes.

### To calculate the IoU between two boxes like above: 

    def iou(box1, box2):
    """Implement the intersection over union (IoU) between box1 and box2
    
    Arguments:
    box1 -- first box, list object with coordinates (box1_x1, box1_y1, box1_x2, box_1_y2)
    box2 -- second box, list object with coordinates (box2_x1, box2_y1, box2_x2, box2_y2)
    """
    (box1_x1, box1_y1, box1_x2, box1_y2) = box1
    (box2_x1, box2_y1, box2_x2, box2_y2) = box2

    # Calculate the (yi1, xi1, yi2, xi2) coordinates of the intersection of box1 and box2.
    xi1 = max(box1_x1, box2_x1)
    yi1 = max(box1_y1, box2_y1)
    xi2 = min(box1_x2, box2_x2)
    yi2 = min(box1_y2, box2_y2)
    inter_width = max(xi2 - xi1, 0)
    inter_height = max(yi2 - yi1, 0)
    inter_area = inter_width * inter_height
    
    # Calculate the Union area by using Formula: Union(A,B) = A + B - Inter(A,B)
    box1_area = (box1_x2 - box1_x1) * (box1_y2 - box1_y1)
    box2_area = (box2_x2 - box2_x1) * (box2_y2 - box2_y1)
    union_area = box2_area + box1_area - inter_area
    
    # compute the IoU
    iou = inter_area / union_area if union_area != 0 else 0
    
    return iou
