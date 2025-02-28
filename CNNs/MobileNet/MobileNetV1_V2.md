# What are MobileNetV1 and MobileNetV2? 

The V1 is a lightweight deep learning architecture designed for mobile and embedded vision applications. The most important thing we should know is that it is built on depthwise separable convolutions that split a traditional convolution operation into two steps:
* Depthwise conv (this operates on each input channel)
* Pointwise conv (1x1)

This V1 helps improve efficiency by reducing the number of parameters and computation required compared to traditional convolutions, and it fits better for mobile and embedded vision applications. Meanwhile, the V2 introduces inverted residuals with linear bottlenecks to improve performance. V2 reduces the computational cost and improves the speed of the model compared to the V1 by doing skip connections (like ResNet) between bottleneck layers to ensure better gradient flow and higher accuracy. V2 helps improve real-time applications such as detection for example. 

## Real Life Use Case

Who is using MobileNetV2 and its intergration with ResNet connections? Google for example. 

Google uses V2 for real-time object detection in their TensorFlow Lite framework that is designed for running machine learning models on mobile and embedded devices. One of use cases is Google Lens that allows users to search for information based on images.

For example, users take a photo or use their camera to identify objects, translate text, or even get shopping recommendations. So, Google wants users to achieve by getting more information on images they take, and they deploy a V2 model on mobile devices without too much computational cost. In addition, ResNet connections can be applied to improve the model's learning capabilities by enhancing gradient flow, which makes it easier to train deeper models and results in more accurate predictions, especially for complex visual tasks.

![image](https://github.com/user-attachments/assets/0ab99944-1b70-4edc-a529-5b4608849a1a)
