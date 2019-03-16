from django.db import models



#Database tables
class DoubleCheck(models.Model):
    code = models.CharField(max_length=6)
    state = models.ForeignKey(CodeState, on_delete=models.CASCADE)
    fileid = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class File(models.Model):
    path = models.TextField()

    def __str__(self):
        return self.path

class CodeState(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value




