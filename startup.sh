#!/bin/bash
# Script de inicialização para o Render

# Garantir que o gunicorn esteja instalado
pip install gunicorn

# Verificar a instalação do wkhtmltopdf
apt-get update -y && apt-get install -y wkhtmltopdf
which wkhtmltopdf
ls -la /usr/bin/wkhtmltopdf || echo "wkhtmltopdf não encontrado em /usr/bin"
export WKHTMLTOPDF_PATH=$(which wkhtmltopdf)
echo "WKHTMLTOPDF_PATH=$WKHTMLTOPDF_PATH"

# Criar diretórios necessários
mkdir -p pdfs
chmod 755 pdfs

# Executar o aplicativo
exec python -m gunicorn app:app --bind=0.0.0.0:$PORT --log-file=- 