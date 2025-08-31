# -*- coding: utf-8 -*-
"""
ARCHIVO DE EJEMPLO - NO USAR DIRECTAMENTE
==========================================

Este archivo contiene la configuración de ejemplo para CV-Alchemist.
Para usar el proyecto:

1. MODIFICA este archivo con tu API key real
2. O crea un nuevo archivo 'config.py' basado en este ejemplo
3. NUNCA subas tu 'config.py' real a GitHub

El archivo real 'config.py' está en .gitignore para proteger tu API key.
"""

# Configuración de la API de Google Gemini
GEMINI_API_KEY = "tu_api_key_aqui"

# Configuración del modelo de Gemini
GEMINI_MODEL = "gemini-1.5-flash-latest"

# Configuración de carpetas (para uso local, no en Colab)
LOCAL_CV_FOLDER = "./cv_base/"
LOCAL_STUDIES_FOLDER = "./plan_de_estudios/"

# Configuración de logging
LOG_LEVEL = "INFO"
LOG_FILE = "cv_alchemist.log"

# Configuración de timeouts
REQUEST_TIMEOUT = 30  # segundos
MAX_RETRIES = 3

# Configuración de prompts
MAX_TOKENS = 4000
TEMPERATURE = 0.7

"""
INSTRUCCIONES DE USO:

1. MODIFICA este archivo con tu API key real de Gemini
2. O crea un nuevo archivo 'config.py' basado en este ejemplo
3. NUNCA subas tu 'config.py' real a GitHub (está en .gitignore)

Para obtener una API key de Gemini:
1. Ve a https://makersuite.google.com/app/apikey
2. Crea un nuevo proyecto o selecciona uno existente
3. Genera una nueva API key
4. Copia la key y pégala en este archivo

IMPORTANTE: 
- Mantén tu API key segura y no la compartas públicamente
- Este archivo de ejemplo SÍ se subirá a GitHub
- Tu archivo real 'config.py' NO se subirá (está protegido por .gitignore)
""" 