from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from disease.services.predict_disease import predict_disease
import tensorflow as tf
import numpy as np

def predict_type(image) :
        path = 'disease/model_machine_learning/model_type.h5'
        model = load_model(path)
        class_name = ["apple", "corn", "potato"]

        resized_image = image.resize((150, 150))

        x = img_to_array(resized_image)
        x /= 255
        x = tf.expand_dims(x, axis=0)

        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)

        # Get the index of the class with the highest probability
        predicted_class_index = np.argmax(classes[0])

        # Get the name of the predicted class
        predicted_class_name = class_name[predicted_class_index]

        # Print the predicted class name
        print("Predicted type :", predicted_class_name)

        if predicted_class_name == "apple" :
            class_name = ['apple black rot', 'apple healthy', 'apple scab', 'apple cedar rust']
            model = load_model('disease/model_machine_learning/model_apple.h5')

        elif predicted_class_name == "corn" :
            class_name = ["corn common rust", "corn gray leaf spot", "corn healthy", "corn northern leaf blight"] 
            model = load_model('disease/model_machine_learning/model_corn.h5')
        else :
            class_name = ["potato early blight", "potato healthy", "potato late blight"]
            model = load_model('disease/model_machine_learning/model_potato.h5')

        predicted_disease = predict_disease(images, model, class_name)

        return predicted_disease