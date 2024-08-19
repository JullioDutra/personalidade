from django import forms

class TestePersonalidadeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        perguntas = kwargs.pop('perguntas')
        super(TestePersonalidadeForm, self).__init__(*args, **kwargs)

        for pergunta in perguntas:
            self.fields[f'pergunta_{pergunta.id}'] = forms.ChoiceField(
                label=pergunta.texto,
                choices=[
                    (1, '😟 Muito Baixo'),
                    (2, '😐 Baixo'),
                    (3, '😐 Médio'),
                    (4, '🙂 Alto'),
                    (5, '😃 Muito Alto'),
                ],
                widget=forms.RadioSelect,
                required=True
            )
