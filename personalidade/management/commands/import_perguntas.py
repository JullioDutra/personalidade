import pandas as pd
from django.core.management.base import BaseCommand
from personalidade.models import Pergunta

class Command(BaseCommand):
    help = 'Importa perguntas de um arquivo Excel para o modelo Pergunta'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Caminho para o arquivo Excel')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']

        # Use pandas para ler o arquivo Excel
        df = pd.read_excel(file_path)

        # Iterar sobre cada linha do DataFrame e criar um objeto Pergunta
        for _, row in df.iterrows():
            Pergunta.objects.create(
                texto=row['texto'],
                categoria=row['categoria']
            )

        self.stdout.write(self.style.SUCCESS('Perguntas importadas com sucesso'))
