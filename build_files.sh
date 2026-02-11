#!/bin/bash
echo "🚀 BUILD START"

# Instalar uv si no está
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.cargo/bin:$PATH"

# Crear virtualenv y sincronizar dependencias
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Django commands
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "✅ BUILD END"