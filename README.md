# 📄 Divisor de Certificados PDF por Nombre (Estilo iLovePDF)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/PyPDF-4.0%2B-EC1C24?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="PyPDF" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
  <img src="https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/GitHub%20Pages-Deploy-222222?style=for-the-badge&logo=githubpages&logoColor=white" alt="GitHub Pages" />
  <img src="https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge" alt="Licencia" />
</p>

<p align="center">
  Herramienta inteligente y moderna para dividir documentos masivos de certificados o diplomas en archivos PDF individuales, extrayendo automáticamente el nombre de cada persona, evitando sobreescrituras por duplicados y generando paquetes ZIP listos para su distribución.
</p>

---

## 🌐 Enlaces del Proyecto

| Recurso | Enlace | Estado |
| :--- | :--- | :--- |
| 🚀 **Landing Page (GitHub Pages)** | [Ver Landing Page](https://tu-usuario.github.io/tu-repositorio/) *(al desplegar en GitHub Pages)* | 🟢 Listo (`index.html` en raíz) |
| ⚡ **Aplicación Web en Streamlit** | [Abrir App en Streamlit](https://tu-app-de-certificados.streamlit.app) *(URL tentativa)* | 🟡 Reemplazar con tu URL real |
| 💻 **Repositorio de Código** | [GitHub Repository](https://github.com) | 📁 Código Fuente |

> [!NOTE]
> Puedes actualizar la URL de Streamlit directamente en `index.html` buscando la etiqueta `data-streamlit-url` o los enlaces con la clase `cta-streamlit-link`.

---

## ✨ Características Principales

- **🎯 Detección Inteligente de Nombres**: Extrae con precisión nombres y apellidos, soportando caracteres en español (tildes, `ñ`, diéresis).
- **🛡️ Cero Sobreescrituras (Control de Duplicados)**: Si un participante cuenta con múltiples certificados (ej. *Organizador* y *Ponente*), numera automáticamente (`_2.pdf`) o añade su rol para salvaguardar todos los diplomas.
- **📦 Empaquetado y Descarga en ZIP**: En la interfaz interactiva, comprime y descarga todos los certificados generados con un solo clic.
- **🧹 Sanitización de Nombres de Archivo**: Remueve caracteres prohibidos por los sistemas operativos (`:`, `\`, `/`, `*`, `?`, `"`, `<`, `>`, `|`).
- **🔒 100% Privado y en Memoria**: El procesamiento se realiza en memoria volátil de sesión sin almacenar tus documentos en bases de datos externas.
- **⚡ Doble Modo de Uso**: Interfaz web moderna (tipo iLovePDF) o script de consola para automatización por lotes.

---

## 🛠️ Tecnologías Empleadas

- **[Python](https://www.python.org/)**: Lenguaje base para el procesamiento de archivos y la lógica de backend.
- **[Streamlit](https://streamlit.io/)**: Framework para la creación de la interfaz web interactiva rápida y reactiva.
- **[pypdf](https://pypdf.readthedocs.io/)**: Librería moderna en Python puro para lectura, extracción de texto y particionado de archivos PDF.
- **[HTML5 / CSS3 / JavaScript](https://developer.mozilla.org/)**: Maquetación y estilos de la Landing Page moderna optimizada para GitHub Pages.
- **[GitHub Pages](https://pages.github.com/)**: Alojamiento estático gratuito del sitio promocional / landing page (`index.html`).

---

## 🚀 Opciones de Uso

### Opción 1: Interfaz Web Interactiva (Recomendado)

Una experiencia visual donde puedes arrastrar cualquier archivo PDF, previsualizar la lista de nombres detectados, seleccionar el formato del nombre de salida y descargar todo en un archivo ZIP.

1. **Vía Acceso Directo (Windows)**:
   Haz doble clic sobre el archivo ejecutable [`iniciar_app.bat`](file:///c:/Users/Feibert/OneDrive/Documents/UNILASALLISTA/Dividir%20PDF/iniciar_app.bat).
   
2. **Vía Terminal / Consola**:
   ```bash
   streamlit run app.py
   ```
   Se abrirá automáticamente en tu navegador web en: `http://localhost:8501`

---

### Opción 2: Script Directo por Consola (CLI)

Ideal para servidores, tareas programadas o procesamiento instantáneo sin abrir navegador:

```bash
# Procesar archivo por defecto
python dividir_pdf.py

# O especificar la ruta de cualquier archivo PDF:
python dividir_pdf.py "ruta/a/tu/archivo.pdf"
```

Los certificados individuales se guardarán ordenados en la carpeta:
📁 `Certificados_Separados/`

---

## 💻 Instalación Local Paso a Paso

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd "Dividir PDF"
   ```

2. **Crear y activar un entorno virtual (recomendado)**:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🌐 Guía de Despliegue en GitHub

### 1. Desplegar la Landing Page en GitHub Pages

Dado que el archivo `index.html` se encuentra en la raíz del proyecto:

1. Ve a tu repositorio en **GitHub**.
2. Entra en **Settings** (Configuración) > **Pages** (menú lateral izquierdo).
3. En la sección **Build and deployment**:
   - **Source**: `Deploy from a branch`
   - **Branch**: Selecciona `main` (o `master`) y carpeta `/(root)`.
4. Haz clic en **Save**. En 1-2 minutos tu landing estará activa en:  
   `https://<tu-usuario>.github.io/<nombre-del-repo>/`

### 2. Desplegar la App en Streamlit Community Cloud

1. Ingresa a [share.streamlit.io](https://share.streamlit.io/).
2. Conecta tu cuenta de GitHub y haz clic en **New app**.
3. Selecciona tu repositorio, rama `main` y en *Main file path* coloca: `app.py`.
4. Haz clic en **Deploy!**
5. Copia la URL pública generada (ej. `https://tu-app-de-certificados.streamlit.app`) y reemplázala en el botón del `index.html`.

---

## 📁 Estructura del Proyecto

```plaintext
Dividir PDF/
│
├── index.html                 # 🚀 Landing Page moderna para GitHub Pages
├── app.py                     # ⚡ Aplicación Web interactiva en Streamlit
├── dividir_pdf.py             # 💻 Script CLI de Python para procesamiento directo
├── requirements.txt           # 📦 Dependencias del proyecto (streamlit, pypdf)
├── iniciar_app.bat            # 🖱️ Acceso rápido para ejecutar en Windows
├── README.md                  # 📖 Documentación y guía del proyecto
│
└── Certificados_Separados/    # 📁 Carpeta de salida para PDFs generados
```

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Consulta el código fuente libremente para adaptarlo a tus necesidades institucionales o personales.
