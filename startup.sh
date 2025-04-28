#!/bin/bash
# Script de inicialização para o Render

# Garantir que o gunicorn esteja instalado
pip install gunicorn

# Criar diretórios necessários
mkdir -p pdfs
chmod 755 pdfs

# Executar o aplicativo
exec python -m gunicorn app:app --bind=0.0.0.0:$PORT --log-file=- 