from django.db import models

class Participante(models.Model):
    nome = models.CharField(max_length=100)


class Pergunta(models.Model):
    texto = models.TextField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.texto

class Resposta(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.IntegerField()

    def __str__(self):
        return f"{self.participante.nome} - {self.pergunta.texto} - {self.resposta}"

class ResultadoPersonalidade(models.Model):
    participante = models.OneToOneField(Participante, on_delete=models.CASCADE)
    abertura = models.FloatField(default=0)
    conscienciosidade = models.FloatField(default=0)
    extroversao = models.FloatField(default=0)
    amabilidade = models.FloatField(default=0)
    neuroticismo = models.FloatField(default=0)

    def __str__(self):
        return f"Resultado de {self.participante.nome}"
