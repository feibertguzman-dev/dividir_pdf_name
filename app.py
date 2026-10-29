import io
import re
import zipfile
from pathlib import Path
import streamlit as st
import pypdf

# Configuración de página estilo moderno
st.set_page_config(
    page_title="PDF Splitter - Divisor de Certificados",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para una estética tipo iLovePDF premium
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #FF4B4B 0%, #E60023 50%, #B8001F 100%);
        padding: 2.2rem 2.5rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(230, 0, 35, 0.25);
    }
    
    .main-header h1 {
        margin: 0;
        font-weight: 700;
        font-size: 2.3rem;
        letter-spacing: -0.5px;
    }
    
    .main-header p {
        margin-top: 0.6rem;
        margin-bottom: 0;
        font-size: 1.05rem;
        opacity: 0.95;
    }
    
    .card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid #ECEFF1;
        box-shadow: 0 4px 14px rgba(0,0,0,0.04);
        margin-bottom: 1.2rem;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #FF4B4B 0%, #D81B60 100%);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-size: 1.05rem;
        box-shadow: 0 6px 16px rgba(216, 27, 96, 0.3);
        transition: all 0.25s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(216, 27, 96, 0.45);
        color: white;
    }
    
    .metric-badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 20px;
        background: #F8F9FA;
        font-weight: 600;
        color: #2D3748;
        border: 1px solid #E2E8F0;
        margin-right: 8px;
    }
</style>
""", unsafe_allow_html=True)

def clean_filename(name: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*]', '', name)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip('. ')
    return cleaned or "Sin_Nombre"

def extract_name_and_role(page):
    text = page.extract_text() or ""
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    # Nombre principal
    name = lines[0].rstrip('.').strip() if lines else "Certificado"
    name = clean_filename(name)
    
    # Rol o tipo de participación opcional
    role = ""
    m = re.search(r'calidad de\s+([A-ZÁÉÍÓÚÑ\s]+?)\s+con el tema', text, re.IGNORECASE)
    if m:
        role = clean_filename(m.group(1).strip()).replace(' ', '_')
    elif 'actividades en UNILASALLISTA' in text or 'RECONOCIMIENTO' in text:
        role = "RECONOCIMIENTO"
        
    return name, role, text

# Encabezado visual
st.markdown("""
<div class="main-header">
    <h1>📄 Divisor Inteligente de PDF por Nombres</h1>
    <p>Carga tu archivo de certificados tipo <b>iLovePDF</b>, extrae el nombre de cada persona automáticamente y descarga todos los PDF separados individualmente o en ZIP.</p>
</div>
""", unsafe_allow_html=True)

# Barra lateral con configuraciones
with st.sidebar:
    st.header("⚙️ Opciones de División")
    naming_option = st.radio(
        "Formato del nombre del archivo:",
        [
            "Solo Nombre (ej. Feibert Alirio Guzmán Pérez.pdf)",
            "Nombre + Rol (ej. Feibert Alirio Guzmán Pérez_ORGANIZADOR.pdf)",
            "Número + Nombre (ej. 01_Feibert Alirio Guzmán Pérez.pdf)"
        ]
    )
    
    st.markdown("---")
    st.info("💡 **Consejo:** El algoritmo detecta automáticamente nombres con tildes, caracteres en español y maneja personas con múltiples certificados para que ningún archivo se sobrescriba.")

# Carga de archivo
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("1. Subir archivo PDF")
    
    default_sample = Path("CertificadosConferfirmados.pdf")
    use_sample = False
    
    uploaded_file = st.file_uploader("Selecciona o arrastra el archivo PDF aquí", type=["pdf"])
    
    if uploaded_file is None and default_sample.exists():
        if st.checkbox("Cargar archivo local de ejemplo (CertificadosConferfirmados.pdf)", value=True):
            use_sample = True

pdf_bytes = None
file_display_name = ""

if uploaded_file is not None:
    pdf_bytes = uploaded_file.read()
    file_display_name = uploaded_file.name
elif use_sample:
    with open(default_sample, "rb") as f:
        pdf_bytes = f.read()
    file_display_name = default_sample.name

if pdf_bytes:
    reader = pypdf.PdfReader(io.BytesIO(pdf_bytes))
    total_pages = len(reader.pages)
    
    with col2:
        st.subheader("2. Resumen del Documento")
        st.markdown(f"""
        <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:12px; padding:1.2rem; margin-bottom:1rem;">
            <p style="margin:0; font-size:1.05rem; color:#166534;">✅ <b>Archivo:</b> {file_display_name}</p>
            <p style="margin:5px 0 0 0; font-size:1.05rem; color:#166534;">📄 <b>Páginas detectadas:</b> {total_pages}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Procesar y previsualizar lista de nombres extraídos
    st.markdown("---")
    st.subheader(f"3. Nombres Extraídos ({total_pages} certificados)")
    
    extracted_records = []
    name_counter = {}
    
    for idx, page in enumerate(reader.pages):
        page_num = idx + 1
        name, role, full_text = extract_name_and_role(page)
        
        # Conteo para evitar colisiones
        count = name_counter.get(name, 0) + 1
        name_counter[name] = count
        
        if "Solo Nombre" in naming_option:
            suffix = f"_{count}" if count > 1 else ""
            final_filename = f"{name}{suffix}.pdf"
        elif "Nombre + Rol" in naming_option:
            role_part = f"_{role}" if role else ""
            suffix = f"_{count}" if count > 1 else ""
            final_filename = f"{name}{role_part}{suffix}.pdf"
        else:
            final_filename = f"{page_num:02d}_{name}.pdf"
            
        extracted_records.append({
            "Página": page_num,
            "Nombre Extraído": name,
            "Rol / Modalidad": role or "N/A",
            "Nombre de Archivo Final": final_filename,
            "_page_obj": page
        })
    
    # Vista previa en tabla moderna
    preview_data = [
        {"Pág.": r["Página"], "Nombre Extraído": r["Nombre Extraído"], "Rol": r["Rol / Modalidad"], "Archivo Generado": r["Nombre de Archivo Final"]}
        for r in extracted_records
    ]
    st.dataframe(preview_data, use_container_width=True, height=280)
    
    # Botón de Procesar y Descargar
    st.markdown("### 4. Generar y Descargar")
    btn_col1, btn_col2 = st.columns([1, 1], gap="medium")
    
    with btn_col1:
        if st.button("🚀 Dividir PDF y Guardar en Carpeta Local"):
            output_dir = Path("Certificados_Separados")
            output_dir.mkdir(exist_ok=True)
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, rec in enumerate(extracted_records):
                writer = pypdf.PdfWriter()
                writer.add_page(rec["_page_obj"])
                dest_path = output_dir / rec["Nombre de Archivo Final"]
                with open(dest_path, "wb") as f_out:
                    writer.write(f_out)
                
                progress = (i + 1) / total_pages
                progress_bar.progress(progress)
                status_text.text(f"Guardando [{i+1}/{total_pages}]: {rec['Nombre de Archivo Final']}")
                
            st.success(f"🎉 ¡Listos los {total_pages} certificados guardados en la carpeta: `{output_dir.resolve()}`!")
            
    with btn_col2:
        # Generar ZIP en memoria para descarga directa estilo LovePDF
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for rec in extracted_records:
                page_writer = pypdf.PdfWriter()
                page_writer.add_page(rec["_page_obj"])
                pdf_page_buffer = io.BytesIO()
                page_writer.write(pdf_page_buffer)
                zip_file.writestr(rec["Nombre de Archivo Final"], pdf_page_buffer.getvalue())
                
        zip_buffer.seek(0)
        st.download_button(
            label="📦 Descargar Todos en un Archivo .ZIP",
            data=zip_buffer.getvalue(),
            file_name=f"Certificados_Separados_{Path(file_display_name).stem}.zip",
            mime="application/zip"
        )
else:
    st.info("👆 Por favor sube un archivo PDF o marca la casilla para procesar los certificados de ejemplo.")
