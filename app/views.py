from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def home(request):
    return render(request, "home.html")


def gerar_certificado(request):
    # Carrega o template HTML
    template_path = 'certificado.html'
    template = get_template(template_path)

    # Contexto para o template
    contexto = {
        'nome': 'Fulano da Silva Sauro',
        'evento': '45ª tentativa de fazer esse certificado imprimir o fundo usando django/xhtml2pdf'
    }

    # Renderiza o template com o contexto
    html_content = template.render(contexto)

    # Cria um arquivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="certificado.pdf"'

    # Converte o HTML para PDF
    pisa.CreatePDF(
        html_content,
        dest=response,
        encoding='utf-8'
    )

    # Retorna a resposta com o PDF
    return response
