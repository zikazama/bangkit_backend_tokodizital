from django.apps import AppConfig
from tensorflow.keras.models import load_model


class DiseaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'disease'

    def ready(self) : 
        PATH_TYPE = 'disease/models/model_type_3.h5'
        PATH_APPLE = 'disease/models/model_type_3.h5'
        PATH_POTATO = 'disease/models/model_type_3.h5'
        PATH_CORN = 'disease/models/model_type_3.h5'

        self.model_type = load_model(PATH_TYPE)
        print("Load Model Type Success!!!")

        self.apple_model = load_model(PATH_APPLE)
        print("Load Model Apple Success!!!")

        self.potato_model = load_model(PATH_POTATO)
        print("Load Model Potato Success!!!")

        self.corn_model = load_model(PATH_CORN)
        print("Load Model Corn Success!!!")

