from django.shortcuts import render, redirect
from .models import Participante, Pergunta, Resposta, ResultadoPersonalidade
from django.contrib import messages

def teste_personalidade(request):
    perguntas = Pergunta.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        if not nome:
            messages.error(request, 'Por favor, insira um nome.')
            return render(request, 'teste_personalidade.html', {'perguntas': perguntas})
        
        participante = Participante.objects.create(nome=nome)

        for pergunta in perguntas:
            resposta = request.POST.get(f'pergunta_{pergunta.id}')
            if resposta:
                Resposta.objects.create(
                    participante=participante,
                    pergunta=pergunta,
                    resposta=int(resposta)
                )
        
        calcular_resultado_personalidade(participante)
        return redirect('resultado_personalidade', participante_id=participante.id)
    
    return render(request, 'teste_personalidade.html', {'perguntas': perguntas})

def resultado_personalidade(request, participante_id):
    try:
        participante = Participante.objects.get(id=participante_id)
        resultado = ResultadoPersonalidade.objects.get(participante=participante)
    except Participante.DoesNotExist:
        messages.error(request, 'Participante não encontrado.')
        return redirect('teste_personalidade')
    except ResultadoPersonalidade.DoesNotExist:
        messages.error(request, 'Você precisa realizar o teste de personalidade primeiro.')
        return redirect('teste_personalidade')

    return render(request, 'resultado_personalidade.html', {'resultado': resultado})

def calcular_resultado_personalidade(participante):
    respostas = Resposta.objects.filter(participante=participante)
    categorias = ['Abertura', 'Conscienciosidade', 'Extroversao', 'Amabilidade', 'Neuroticismo']
    soma = {cat: 0 for cat in categorias}
    count = {cat: 0 for cat in categorias}

    for resposta in respostas:
        categoria = resposta.pergunta.categoria
        soma[categoria] += resposta.resposta
        count[categoria] += 1

    resultado, created = ResultadoPersonalidade.objects.get_or_create(participante=participante)
    for cat in categorias:
        setattr(resultado, cat.lower(), round((soma[cat] / count[cat]) * 20) if count[cat] > 0 else 0)

    resultado.save()
