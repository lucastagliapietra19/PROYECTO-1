from django import forms

class Familiar_Form(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    nombre = forms.CharField(label='Nombre', max_length=100, required=True)
    edad = forms.IntegerField(label='Edad', required=True)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', required=True)

    def fill_form(self, familiar):
        self.fields['id'].initial = familiar.id
        self.fields["nombre"].initial = familiar.nombre
        self.fields["edad"].initial = familiar.edad
        self.fields["fecha_nacimiento"].initial = familiar.fecha_nacimiento
        return self