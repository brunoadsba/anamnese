from flask import Flask, render_template, send_from_directory, request, jsonify, make_response
import pdfkit
import os
import json
import subprocess
from datetime import datetime
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app)
app.wsgi_app.add_files('./image/', prefix='image/')

@app.route('/')
def index():
    return send_from_directory('.', 'form.html')

@app.route('/image/<path:filename>')
def serve_image(filename):
    return send_from_directory('image', filename)

@app.route('/gerar-pdf', methods=['POST'])
def gerar_pdf():
    try:
        # Recebe os dados do formulário via POST
        form_data = request.json
        
        # Gera um nome para o arquivo com timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_filename = f"anamnese_{timestamp}.pdf"
        pdf_path = os.path.join('pdfs', pdf_filename)
        
        # Certifica-se de que o diretório existe
        os.makedirs('pdfs', exist_ok=True)
        
        # Preparar os dados da imagem - caminho absoluto para a logo
        logo_file = os.path.abspath(os.path.join('image', 'logo_bg.png'))
        form_data['logo_path'] = f"file:///{logo_file}"
        
        # Renderiza o template HTML com os dados do formulário
        html_content = render_template('pdf_template.html', data=form_data)
        
        # Configura as opções do pdfkit
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'enable-local-file-access': None  # Permite acesso a arquivos locais
        }
        
        # Define o caminho para o executável wkhtmltopdf
        wkhtmltopdf_path = None
        
        # Primeiro tenta obter do ambiente (definido no startup.sh)
        if os.environ.get('WKHTMLTOPDF_PATH'):
            wkhtmltopdf_path = os.environ.get('WKHTMLTOPDF_PATH')
        # Depois tenta encontrar no PATH ou em locais comuns
        else:
            try:
                # Tenta usar o comando 'which' para localizar o executável
                wkhtmltopdf_path = subprocess.check_output(['which', 'wkhtmltopdf']).decode('utf-8').strip()
            except:
                # Caminhos comuns para o wkhtmltopdf
                possible_paths = [
                    '/usr/bin/wkhtmltopdf',
                    '/usr/local/bin/wkhtmltopdf',
                    '/opt/wkhtmltopdf/bin/wkhtmltopdf',
                    'wkhtmltopdf'  # Tenta o comando diretamente
                ]
                
                for path in possible_paths:
                    if os.path.exists(path) or path == 'wkhtmltopdf':
                        wkhtmltopdf_path = path
                        break
        
        if not wkhtmltopdf_path:
            raise Exception("wkhtmltopdf não encontrado. Por favor, instale-o ou forneça o caminho correto.")
            
        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
        
        # Log para debug
        print(f"Usando wkhtmltopdf em: {wkhtmltopdf_path}")
        
        # Gera o PDF
        pdfkit.from_string(html_content, pdf_path, options=options, configuration=config)
        
        # Retorna o caminho do PDF gerado
        return jsonify({
            'success': True,
            'message': 'PDF gerado com sucesso',
            'filename': pdf_filename
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro ao gerar PDF: {str(e)}'
        }), 500

@app.route('/pdfs/<path:filename>')
def serve_pdf(filename):
    return send_from_directory('pdfs', filename)

if __name__ == '__main__':
    # Obter porta do ambiente (necessário para o Render)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 