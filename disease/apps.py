from django.apps import AppConfig
import gcsfs
import h5py
from tensorflow.keras.models import load_model


class DiseaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'disease'

    def ready(self) : 
        FS = gcsfs.GCSFileSystem(project="toko-dizital",
                         token="gcpCredentials.json")
        with FS.open("gs://toko-dizital/model/model_type_3.h5", 'rb') as model_file:
            model_gcs = h5py.File(model_file, 'r')
            model = load_model(model_gcs)

        self.model_type = model

        print("Load Model Type Success!!!")
        # with FS.open("gs://toko-dizital/model/model_potato_4.h5", 'rb') as model_file:
        #     model_gcs = h5py.File(model_file, 'r')
        #     model = load_model(model_gcs)

        # self.potato_model = model
        # print("Load Model Potato Success!!!")

        with FS.open("gs://toko-dizital/model/model_apple_2.h5", 'rb') as model_file:
            model_gcs = h5py.File(model_file, 'r')
            model = load_model(model_gcs)

        self.apple_model = model
        print("Load Model Apple Success!!!")
