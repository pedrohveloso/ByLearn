from reportlab.pdfgen import canvas # Onde "desenhamos" no PDF
from reportlab.lib.pagesizes import A4 # (210*mm,297*mm)
from reportlab.lib.units import cm, inch, mm # Padrão = Points
from reportlab.pdfbase import pdfmetrics # Usamos para registrar a fonte
from reportlab.pdfbase.ttfonts import TTFont # Criar a fonte em si
from reportlab.lib import colors # Trabalhar com cores

# Seta se o Debug está ativo (para tamanho e régua)
DEBUG = False

# Conversor de tamanhos
def mostrar_tamanho():
    """Mostra o tamanho de mm, cm e pelegadas convertido em pontos"""
    print(f'1 mm vale {mm} pontos')
    print(f'1 cm vale {cm} pontos')
    print(f'1 polegada vale {inch} pontos')

def desenhar_regua(pdf, pagina):
    """Desenha uma régua para facilitar entender a posição de cada elemento

    Args:
        pdf: O Canvas que você está trabalhando
        pagina: O tamanho da página atual
    """
    pdf.setFontSize(8)
    pagina_y = int(pagina[1] / cm)
    pagina_x = int(pagina[0] / cm)

    for y in range(pagina_y):
        pdf.drawString(0 * cm, y * cm, f'y{y}')

    for x in range(pagina_x):
        pdf.drawString(x * cm, (pagina_y - 0) * cm, f'x{x}')

def mostrar_fontes_disponiveis(pdf):
    """Mostra todas as fontes disponíveis para uso"""

    print(pdf.getAvaliableFonts())

def registrar_fonte(titulo_fonte, arquivo_fonte):
    """Registra Fontes para serem utilizadas"""
    pdfmetrics.registerFont(TTFont(titulo_fonte, arquivo_fonte))

# Só entra no IF se executarmos o arquivo diretamente
if '__name__' == '__main__':

    # Valores do arquivo
    arquivo = "Curso de PDF.pdf"
    titulo_arquivo = "Integrando o Python com PDF"
    tamanho_pagina_arquivo = A4

    # Configura o PDF
    pdf = canvas.Canvas(arquivo, pagesize=tamanho_pagina_arquivo)
    pdf.setTitle(titulo_arquivo) 

    # Valores do título e subtítulo
    titulo_conteudo = "ByLearn Apresenta:"
    subtitulo_conteudo = "Aprenda a manipular arquivos PDF com o Python"
    
    # Configura o Título
    registrar_fonte('Open-Sans', 'OpenSans-Regular.ttf')
    pdf.setFont('OpenSans', 36)
    pdf.drawCentredString((210*mm)/2, (29.7 - 2) * cm, titulo_conteudo)
   
    # Configura o subtítulo
    pdf.setFillColorRGB(0, 0, 200)
    pdf.setFontSize('Times-Roman', 18)
    pdf.drawCentredString((210*mm)/2, (29.7 - 3) * cm, subtitulo_conteudo)
    
    # Desenha a linha divisória
    pdf.line(0.7 * cm,  26.4 * cm, 20.5 * cm, 26.4 * cm)
    
    # Valores do corpo do PDF
    conteudo_curso = [ 
        'Neste curso você aprenderá: ',
        '- Extrair informações de PDFs existentes',
        '- Extrair texto de PDFs existentes',
        '- Juntar PDFs (Merge)',
        '- Rotacionar páginas',
        '- Dividir PDFs (Split)',
        '- Adicionar senha',
        '- Trabalhar com arquivos com senha',
        '- Gerar PDFs através de arquivos HTML ou URL',
        '- Criar um PDF do zero'
    ]

    # Configuração do corpo do PDF
    from reportlab.lib import colors

    texto = pdf.beginText(1.5 * cm, 25.5 * cm)
    texto.setFillColor(colors.darkgreen)
    texto.setFont('Times-Roman', 18)

    for linha in conteudo_curso:
        texto.textLine(linha)

    pdf.drawText(texto) # Funciona com textos longos, como listas de textos

    # Valores da imagem
    logo_bylearn = 'bylearn.jpg'

    # Configuração da imagem
    pdf.drawImage(logo_bylearn, 6.5 * cm, 9 * cm)

    # Configurando a página 2
    pdf.showPage()

    # Valores de agradecimento
    agradecimento_titulo = 'Muito Obrigado Pela Aternção'
    agradecimento_subtitulo = 'Nos Vemos no Próximo Curso!'

    # Configuração do agradecimento
    pdf.setFont('OpenSans', 36)
    pdf.drawCentredString((210*mm)/2, (29.7 / 2) * cm + 25, agradecimento_titulo)
    pdf.setFontSize(28)
    pdf.drawCentredString((210*mm)/2, (29.7 / 2) * cm - 25, agradecimento_subtitulo)

    # Mostrando informações de Debug
    if DEBUG:
        mostrar_tamanho()
        desenhar_regua(pdf, tamanho_pagina_arquivo)

    # Salvando o arquivo
    pdf.save()
