from django.contrib import admin
from .models import Pergunta, ResultadoPersonalidade, Participante

admin.site.register(Pergunta)
admin.site.register(Participante)
admin.site.register(ResultadoPersonalidade)
# Register your models here.
