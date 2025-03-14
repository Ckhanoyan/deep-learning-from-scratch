# Anchor Boxes in Object Detection 

What if you want to detect at least one object in an image? That is where anchor boxes come in. We are using YOLO as an example for this situation. 

## How anchor Boxes Work

They are kind of predefined shapes where they come in various sizes and aspect ratios... The boxes can be placed at different locations in the image or even in the same location, e.g., a person standing by a car. We have to consider using IoU (intersection over union), and this model will help predict an offset for the position, size, and confidence score for each anchor box. For the low probabilites, we can remove them all depending on our decided threshold, e.g., < 0.6, and we want to keep higher probabilities, e.g., > 0.6. 
* Class probability: the likelihood that the anchor box contains an object, given its class, e.g., car, person, dog, etc.
* Bounding Box Adjustments: the model predicts offsets that adjust the anchor box to better match the object
