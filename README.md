# 🧪 CV-Alchemist: Transformación Inteligente de CVs con IA

## 📋 Introducción

### Nombre del Proyecto
**CV-Alchemist** - Sistema de Optimización Automatizada de Currículums Vitae mediante Ingeniería de Prompts y Modelos de IA Generativa

### 📄 Documentación del Proyecto
📋 [Presentación de la Propuesta del Proyecto](https://drive.google.com/file/d/1fMh9jzWs6ENSqsfOZhWcoQ_rZp5JKbWR/view?usp=drive_link)

### Presentación del Problema a Abordar

En el mercado laboral actual, los candidatos enfrentan un desafío crítico: **la optimización de CVs para sistemas ATS (Applicant Tracking Systems)** y la adaptación específica para cada oferta de trabajo. Este problema es especialmente relevante porque:

- **Los filtros ATS rechazan automáticamente** hasta el 75% de los CVs que no contienen las palabras clave específicas del puesto
- **La personalización manual** de CVs para cada aplicación consume tiempo valioso y recursos del candidato
- **La falta de alineación** entre las habilidades del candidato y los requisitos del puesto reduce significativamente las probabilidades de éxito
- **La transición de carrera** requiere una reformulación estratégica que destaque la relevancia de experiencias previas

### Desarrollo de la Propuesta de Solución

La solución se vincula directamente al desarrollo de modelos de IA mediante la implementación de **técnicas avanzadas de Prompt Engineering** que aprovechan las capacidades de modelos generativos como Google Gemini. Los prompts diseñados incluyen:

1. **Prompt de Estructuración**: Transforma descripciones de puestos desordenadas en información estructurada y accionable
2. **Prompt de Actualización**: Integra nueva formación académica en CVs existentes de manera coherente
3. **Prompt de Optimización**: Alinea CVs con requisitos específicos de puestos, optimizando para sistemas ATS

### Justificación de la Viabilidad del Proyecto

**Viabilidad Técnica:**
- **APIs disponibles**: Google Gemini API proporciona capacidades robustas de procesamiento de lenguaje natural
- **Librerías maduras**: PyPDF2 y google-generativeai ofrecen funcionalidades probadas y documentadas
- **Infraestructura**: Google Colab proporciona entorno de desarrollo gratuito y escalable

**Recursos y Tiempo:**
- **Desarrollo**: 2-3 semanas de implementación incremental
- **Costos**: Uso gratuito de Google Colab y cuota gratuita de Gemini API
- **Mantenimiento**: Código modular y bien documentado para futuras mejoras

## 🎯 Objetivos

### Objetivo Principal
Desarrollar un sistema automatizado que transforme CVs genéricos en documentos optimizados y personalizados para puestos específicos, maximizando las probabilidades de pasar filtros ATS y destacar ante reclutadores.

### Objetivos Específicos
1. **Automatizar la extracción** de texto de archivos PDF (CVs y planes de estudio)
2. **Estructurar información** de descripciones de puestos mediante IA
3. **Integrar formación académica** en CVs existentes de manera coherente
4. **Optimizar CVs** para requisitos específicos de puestos usando palabras clave relevantes
5. **Implementar técnicas de Prompt Engineering** para maximizar la efectividad de la IA

## 🔬 Metodología

### Enfoque de Desarrollo
El proyecto sigue una metodología **iterativa e incremental**, dividida en fases claramente definidas:

1. **Fase de Preparación**: Instalación de dependencias y configuración del entorno
2. **Fase de Extracción**: Procesamiento de archivos PDF y extracción de texto
3. **Fase de Estructuración**: Organización de información mediante IA
4. **Fase de Transformación**: Generación de CVs actualizados y optimizados
5. **Fase de Validación**: Verificación de resultados y ajustes de prompts

### Procedimientos Implementados
- **Procesamiento de PDFs**: Lectura automatizada de múltiples archivos con manejo de errores
- **Ingeniería de Prompts**: Diseño iterativo de instrucciones para la IA
- **Flujo de Trabajo en Dos Etapas**: Actualización del CV base seguida de optimización específica
- **Manejo de Errores**: Diagnóstico automático de problemas comunes (cuotas de API, archivos faltantes)

### Justificación de la Metodología
Este enfoque garantiza que cada fase construya sobre la anterior, permitiendo validación temprana y ajustes incrementales. La separación en etapas facilita el debugging y la optimización de cada componente individualmente.

## 🛠️ Herramientas y Tecnologías

### Técnicas de Prompting Utilizadas

1. **Prompt de Rol Específico**: 
   - *"Actúa como un analista de datos experto en Recursos Humanos"*
   - **Justificación**: Define claramente el contexto y expertise esperado de la IA

2. **Prompt de Estructuración con Reglas Explícitas**:
   - Formato específico de salida con títulos en negrita y listas
   - **Justificación**: Garantiza consistencia en la estructura de la respuesta

3. **Prompt de Proceso de Pensamiento**:
   - Instrucciones paso a paso para análisis comparativo
   - **Justificación**: Guía el razonamiento de la IA hacia estrategias específicas

4. **Prompt de Restricciones Críticas**:
   - Reglas como "No inventes experiencia" y "Sé preciso y honesto"
   - **Justificación**: Previene alucinaciones y mantiene la integridad de la información

### Stack Tecnológico
- **Google Gemini API**: Modelo de IA generativa para procesamiento de lenguaje natural
- **Python**: Lenguaje de programación principal con librerías especializadas
- **PyPDF2**: Procesamiento y extracción de texto de archivos PDF
- **Google Colab**: Entorno de desarrollo y ejecución en la nube

## 💻 Implementación

### Arquitectura del Sistema
El proyecto implementa un **pipeline de procesamiento secuencial** que transforma inputs no estructurados en CVs optimizados:

```
PDFs de Entrada → Extracción de Texto → Estructuración con IA → CV Maestro → Optimización Específica → CV Final
```

### Componentes Principales

#### 1. Módulo de Extracción de Datos
```python
def extraer_texto_de_pdf(ruta_pdf):
    texto = ""
    try:
        with open(ruta_pdf, 'rb') as archivo:
            lector = PyPDF2.PdfReader(archivo)
            for pagina in lector.pages:
                texto += pagina.extract_text() + "\n"
        return texto
    except Exception as e:
        print(f"Error al leer el archivo {ruta_pdf}: {e}")
        return None
```

#### 2. Sistema de Prompts Inteligentes
```python
prompt_estructurador = f"""
Actúa como un analista de datos experto en Recursos Humanos. 
Tu tarea es tomar el siguiente texto de una descripción de puesto, 
que está desordenado y contiene información irrelevante, 
y estructurarlo de forma clara y concisa.
...
"""
```

#### 3. Pipeline de Transformación en Dos Etapas
- **Etapa 1**: Generación del CV Maestro actualizado con nueva formación
- **Etapa 2**: Optimización específica para el puesto objetivo

### Flujo de Ejecución
1. **Configuración**: Instalación de dependencias y configuración de API
2. **Preparación**: Creación de estructura de carpetas y carga de archivos
3. **Extracción**: Procesamiento de PDFs y conversión a texto
4. **Estructuración**: Limpieza y organización de descripción del puesto
5. **Transformación**: Generación secuencial de CVs mediante prompts
6. **Salida**: Presentación de resultados en formato optimizado

## 🚀 Uso del Sistema

### Requisitos Previos
- Cuenta de Google Cloud con API Key de Gemini
- Acceso a Google Colab
- Archivos PDF del CV base y plan de estudios
- Librería `reportlab` para generación de PDFs (incluida en requirements.txt)

### Instalación y Configuración Local

#### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/cv-alchemist.git
cd cv-alchemist
```

#### Paso 2: Configurar la API Key
1. **Copia el archivo de ejemplo:**
   ```bash
   cp config_example.py config.py
   ```

2. **Edita `config.py` con tu API key real:**
   ```python
   GEMINI_API_KEY = "tu_api_key_real_aqui"
   ```

3. **Obtén tu API key de Gemini:**
   - Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Crea un nuevo proyecto o selecciona uno existente
   - Genera una nueva API key
   - Copia la key y pégala en `config.py`

#### Paso 3: Instalar Dependencias
```bash
pip install -r requirements.txt
```

**Nota:** El archivo `requirements.txt` incluye `reportlab` para la generación automática de PDFs de los CVs generados.

#### Paso 4: Preparar Archivos PDF
- Coloca tu CV base en la carpeta `cv_base/`
  - 📁 [Acceso a carpeta cv_base en Google Drive](https://drive.google.com/drive/folders/15Y1emmxg4M2XlRbY8oY-AWJ2VHEge3YR?usp=drive_link)
- Coloca los archivos de tu plan de estudios en `plan_de_estudios/`
  - 📁 [Acceso a carpeta plan_de_estudios en Google Drive](https://drive.google.com/drive/folders/13868l7n-mJJ_vfZD8g5x_RYOXDjJVQoa?usp=drive_link)

### Uso en Google Colab

#### Instalación
```bash
!pip install -q google-generativeai PyPDF2
```

#### Configuración
```python
import google.generativeai as genai
genai.configure(api_key=tu_api_key)
```

#### Ejecución
1. Ejecutar todas las celdas del notebook en secuencia
2. Subir archivos PDF en las carpetas correspondientes
3. Ejecutar el pipeline de transformación
4. Obtener CVs optimizados listos para uso

### Flujo de Trabajo Completo

#### Para Usuarios Locales:
1. **Clonar** el repositorio de GitHub
2. **Configurar** la API key en `config.py`
3. **Instalar** dependencias con `pip install -r requirements.txt`
4. **Preparar** archivos PDF en las carpetas correspondientes
   - 📁 [Acceso a carpeta cv_base en Google Drive](https://drive.google.com/drive/folders/15Y1emmxg4M2XlRbY8oY-AWJ2VHEge3YR?usp=drive_link)
   - 📁 [Acceso a carpeta plan_de_estudios en Google Drive](https://drive.google.com/drive/folders/13868l7n-mJJ_vfZD8g5x_RYOXDjJVQoa?usp=drive_link)
5. **Ejecutar** el script principal: `python proyecto_cv_alchemist.py`
6. **📄 PDFs generados automáticamente** en la carpeta `cvs_generados/`

#### Para Usuarios de Google Colab:
1. **Abrir** el notebook `Proyecto_CV_Alchemist.ipynb` en Colab
2. **Configurar** la API key en los Secrets de Colab
3. **Subir** archivos PDF usando el panel de archivos
   - 📁 [Acceso a carpeta cv_base en Google Drive](https://drive.google.com/drive/folders/15Y1emmxg4M2XlRbY8oY-AWJ2VHEge3YR?usp=drive_link)
   - 📁 [Acceso a carpeta plan_de_estudios en Google Drive](https://drive.google.com/drive/folders/13868l7n-mJJ_vfZD8g5x_RYOXDjJVQoa?usp=drive_link)
4. **Ejecutar** todas las celdas en secuencia
5. **Obtener** los CVs optimizados
6. **📄 PDFs generados automáticamente** en `/content/cvs_generados/`

### ⚠️ Notas Importantes
- **NUNCA subas `config.py` a GitHub** (está protegido por .gitignore)
- **`config_example.py` SÍ se sube** como referencia para otros usuarios
- **Mantén tu API key segura** y no la compartas públicamente
- **Para uso en Colab**, usa los Secrets integrados en lugar de archivos de configuración

## 📄 Generación de PDFs

### Funcionalidad Automática Integrada
El sistema CV-Alchemist incluye **generación automática de PDFs** integrada directamente en el flujo de trabajo principal:

- **CV Maestro Actualizado**: PDF del CV base con la nueva formación integrada
- **CV Final Optimizado**: PDF del CV optimizado para el puesto específico

### Archivos Incluidos
- **`Proyecto_CV_Alchemist.ipynb`**: Notebook principal con generación automática de PDFs integrada
- **`proyecto_cv_alchemist.py`**: Script Python con funcionalidad de PDFs incluida
- **`requirements.txt`**: Incluye `reportlab` para la generación de PDFs

### Uso Automático
```python
# Los PDFs se generan automáticamente al final del proceso
# No requiere pasos adicionales ni scripts separados
```

### Características de los PDFs
- **Formato profesional**: A4 con estilos consistentes
- **Timestamp automático**: Nombres únicos con fecha y hora
- **Carpeta organizada**: Todos los PDFs se guardan en `cvs_generados/`
- **Descarga directa**: Listos para usar en aplicaciones de trabajo
- **Integración completa**: Funciona tanto en Google Colab como localmente

## 📊 Resultados Esperados

### Beneficios del Sistema
- **Ahorro de tiempo**: Automatización del proceso de personalización de CVs
- **Mayor efectividad**: Optimización para sistemas ATS y reclutadores
- **Consistencia**: Formato y estructura estandarizados
- **Escalabilidad**: Capacidad de procesar múltiples puestos simultáneamente

### Métricas de Éxito
- **Tasa de paso ATS**: Incremento en la superación de filtros automáticos
- **Tiempo de personalización**: Reducción del 80% en tiempo de adaptación
- **Calidad de alineación**: Mejora en la relevancia de habilidades destacadas

## 🔮 Futuras Mejoras

### Expansión de Funcionalidades
- Integración con múltiples modelos de IA (GPT-4, Claude)
- Análisis de sentimiento en descripciones de puestos
- Generación automática de cartas de presentación
- Dashboard de métricas de efectividad
- **✅ Generación automática de PDFs** (Implementado)

### Optimización Técnica
- Implementación de caché para respuestas de IA
- Paralelización del procesamiento de múltiples CVs
- Interfaz web para usuarios no técnicos
- API REST para integración con otros sistemas
- **✅ Formato PDF profesional** (Implementado)

---

## 📝 Licencia
Este proyecto fue desarrollado como parte de la [Diplomatura de Data Science en Coder House](https://www.coderhouse.com/ar/diplomaturas/data/) y está destinado a fines educativos y de desarrollo profesional.

## 👥 Autor
**Vanesa Mizrahi** - Estudiante de Data Science y Prompting Engineer

## 📞 Contacto
- **Email**: vanesarmizrahi@gmail.com
- **LinkedIn**: [vanesamizrahi](https://www.linkedin.com/in/vanesamizrahi)
- **Kaggle**: [vanesamizrahi](https://www.kaggle.com/vanesamizrahi) 