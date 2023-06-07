from tensorflow.keras.preprocessing.image import img_to_array
import tensorflow as tf
import numpy as np

from disease.services.predict_desease import predict_disease

def predict_type(image, model, model_apple) :
        resized_image = image.resize((150, 150))
        class_name = ["apple", "corn", "potato"]

        x = img_to_array(resized_image)
        x /= 255
        x = tf.expand_dims(x, axis=0)

        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)

        # Get the index of the class with the highest probability
        predicted_class_index = np.argmax(classes[0])
        predicted_class_name = class_name[predicted_class_index]
        predicted_disease = ""

        # if(predicted_class_name == "potato") :
        #         class_name = ["potato early blight", "potato healthy", "potato late blight"]
        #         predicted_disease = predict_disease(images, model_potato, class_name)

        elif(predicted_class_name == "apple") :
                class_name = ['apple black rot', 'apple healthy', 'apple scab', 'apple cedar rust']
                predicted_disease = predict_disease(images, model_apple, class_name)

        # Print the predicted class name
        print(predicted_disease)
        return predicted_disease
