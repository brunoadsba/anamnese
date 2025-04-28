# Anamnese Psicanalítica

Um sistema web para preenchimento e geração de formulários de anamnese psicanalítica em PDF.

## Funcionalidades

- Formulário completo de anamnese psicanalítica
- Interface responsiva e amigável
- Geração de PDF com os dados preenchidos
- Design moderno e profissional

## Tecnologias Utilizadas

- HTML5 e CSS3 com Tailwind CSS
- JavaScript para interação no cliente
- Flask (Python) para o backend
- PDFKit para geração de documentos PDF

## Instalação

1. Clone o repositório:
```
git clone https://github.com/brunoadsba/anamnese.git
cd anamnese
```

2. Crie um ambiente virtual e instale as dependências:
```
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Instale o wkhtmltopdf (necessário para o PDFKit):
```
# Ubuntu/Debian
sudo apt-get install wkhtmltopdf

# Windows
# Baixe o instalador em: https://wkhtmltopdf.org/downloads.html
```

4. Execute o aplicativo:
```
python app.py
```

5. Acesse o formulário em seu navegador:
```
http://127.0.0.1:5000
```

## Estrutura do Projeto

- `app.py` - Aplicação Flask principal
- `form.html` - Formulário de anamnese
- `templates/pdf_template.html` - Template para geração de PDF
- `image/` - Diretório com imagens e logo
- `requirements.txt` - Lista de dependências do projeto

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

## Autor

Bruno Barbosa 