
from django.forms import ModelForm
from .models import Examenes
from django import forms





class ExamForm(ModelForm):
    class Meta:
        model = Examenes
        fields = ['name', 'addres', 'phone', 'email', 'id', 'exam', 'image',]

        def select(self, ExamForm):
            exam = select
            if exam == 'glucosa':
                print ("asdfasdfsadfadsf")

            return ExamForm



## aca fusionamos por decirlo asi el formulario con el modelo. el fields del form debe ir todos los fields del model
## se importael ModelForm para facilitar la fusion de model y forms