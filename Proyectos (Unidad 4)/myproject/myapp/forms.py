from django import forms


class FormularioEntregable(forms.Form):

    titulo=forms.CharField(label="Título del proyecto: ", required=True)
    foto=forms.ImageField(label="Foto (URL): ", required=False)
    descripcion=forms.CharField(label="Descripción del proyecto: ", widget=forms.Textarea)
    tag=forms.CharField(label="TAGS: ", required=True)
    url=forms.CharField(label="URL de github: ", required=True)

