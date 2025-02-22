def convolutional_model(input_shape):

    input_img = tf.keras.Input(shape=input_shape)

    Z1 = Conv2D(15, (5, 5), strides = 1, padding = 'SAME')(in_img)
    A1 = tf.keras.layers.ReLU()(Z1)
    P1 = MaxPooling2D(pool_size = (10, 10), strides = 4, padding = 'SAME')(A1)
    Z2 = Conv2D(20, (3, 3), strides = 1, padding = 'SAME')(P1)
    A2 = tf.keras.layers.ReLU()(Z2)
    P2 = tf.keras.layers.MaxPool2D(pool_size = (2, 2), strides = 2, padding = 'SAME')(A2)
    F =  tf.keras.layers.Flatten()(P2)
  
    outputs = tf.keras.layers.Dense(units= 8, activation='softmax')(F)
    
    model = tf.keras.Model(inputs=in_img, outputs=outputs)
  
    return model
