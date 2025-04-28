#!/bin/bash
# Script de inicialização para o Render

# Criar diretórios necessários
mkdir -p pdfs
chmod 755 pdfs

# Executar o aplicativo
exec gunicorn app:app --bind=0.0.0.0:$PORT --log-file=- 