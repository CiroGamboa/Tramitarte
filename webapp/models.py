from django.db import models
from pathlib import Path
import os


#Database tables
# class File(models.Model):
#     path = models.TextField()
#     def __str__(self):
#         return self.path

class CodeState(models.Model):
    value = models.CharField(max_length=50)
    def __str__(self):
        return self.value



# class ImageTable(models.Model):
#     model_pic = models.ImageField(upload_to = 'docs/', default = 'images/')


class VehicleSell(models.Model):
    code = models.CharField(max_length=6, unique = True)
    state = models.ForeignKey(CodeState, on_delete=models.CASCADE)
    # fileid = models.ForeignKey(File, on_delete=models.CASCADE)
    seller_cedula = models.ImageField(upload_to = 'docs/cedulas/', default = 'images/', blank=True)
    seller_propiedad = models.ImageField(upload_to = 'docs/propiedad/', default = 'images/', blank=True)
    buyer_cedula = models.ImageField(upload_to = 'docs/cedulas', default = 'images/', blank=True)
    buyer_propiedad = models.ImageField(upload_to = 'docs/propiedad', default = 'images/', blank=True)

    def __str__(self):
        return self.code


class DatabaseHandler():
    '''
    Class in charge of managing some data related to the db
    '''
    def init_db(self):
        '''
        Initialize the database with test data
        '''
        # Creating States
        state_generated = CodeState.objects.create(value="generated")
        state_checked = CodeState.objects.create(value="checked")

        # Creating File
        # test_path = "test_tramit_files/"
        # if not os.path.exists(test_path):
        #     os.makedirs(test_path)
        
        # file_name = "test_file.txt"
        # with open(os.path.join(test_path, file_name), 'w'):
        #     pass
        
        # test_file = open(file_name,"w")
        # test_file.write("Hello, World!")

        ## DB Handling
        # test_record = File.objects.create(path=os.path.join(test_path, file_name))
        # test_record.save()








