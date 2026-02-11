#!/bin/bash
echo "🚀 BUILD START"

# Deshabilitar temporalmente la protección PEP 668
export PIP_BREAK_SYSTEM_PACKAGES=1

# Forzar reinstalación
python3 -m pip install --force-reinstall -r requirements.txt

# Si el comando anterior falla, intentar con --break-system-packages
if [ $? -ne 0 ]; then
    python3 -m pip install --break-system-packages -r requirements.txt
fi

python3 manage.py collectstatic --noinput
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "✅ BUILD END"