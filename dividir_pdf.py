import os
import re
from pathlib import Path
import pypdf

def clean_filename(name: str) -> str:
    """Elimina caracteres inválidos para nombres de archivo en Windows y espacios sobrantes."""
    # Eliminar caracteres prohibidos: <>:"/\|?*
    cleaned = re.sub(r'[<>:"/\\|?*]', '', name)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip('. ')
    return cleaned or "Sin_Nombre"

def extract_person_name(page) -> str:
    """Extrae el nombre de la persona del certificado."""
    text = page.extract_text() or ""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return "Certificado_Sin_Texto"
    
    # En este formato de certificados, el nombre se encuentra en la primera línea
    candidate = lines[0].rstrip('.').strip()
    return clean_filename(candidate)

def extract_role_info(page) -> str:
    """Extrae opcionalmente el rol o tipo de participación para desambiguar si hay varias páginas por persona."""
    text = page.extract_text() or ""
    m = re.search(r'calidad de\s+([A-ZÁÉÍÓÚÑ\s]+?)\s+con el tema', text, re.IGNORECASE)
    if m:
        role = m.group(1).strip()
        role = re.sub(r'\s+', '_', clean_filename(role))
        return role
    if 'actividades en UNILASALLISTA' in text or 'RECONOCIMIENTO' in text:
        return "RECONOCIMIENTO"
    return ""

def split_pdf_by_person(pdf_path: str, output_folder: str = "Certificados_Separados", include_role: bool = False):
    """
    Divide el PDF en páginas individuales y las guarda con el nombre de cada persona.
    Si una persona tiene varios certificados, añade un correlativo o el rol para no sobreescribir.
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.is_file():
        raise FileNotFoundError(f"No se encontró el archivo: {pdf_path}")
    
    out_dir = Path(output_folder)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    reader = pypdf.PdfReader(str(pdf_path))
    total_pages = len(reader.pages)
    print(f"Leyendo '{pdf_path.name}' ({total_pages} paginas)...")
    
    generated_files = []
    name_counter = {}

    for idx, page in enumerate(reader.pages):
        page_num = idx + 1
        person_name = extract_person_name(page)
        role = extract_role_info(page) if include_role else ""
        
        # Manejo de nombres duplicados para no sobreescribir
        current_count = name_counter.get(person_name, 0) + 1
        name_counter[person_name] = current_count
        
        if include_role and role:
            suffix = f"_{role}" if current_count == 1 else f"_{role}_{current_count}"
        else:
            suffix = "" if current_count == 1 else f"_{current_count}"
            
        filename = f"{person_name}{suffix}.pdf"
        output_filepath = out_dir / filename
        
        # Crear PDF individual con la página
        writer = pypdf.PdfWriter()
        writer.add_page(page)
        
        with open(output_filepath, "wb") as f_out:
            writer.write(f_out)
            
        generated_files.append((page_num, person_name, filename))
        try:
            print(f"[{page_num:02d}/{total_pages:02d}] Generado: {filename}")
        except Exception:
            print(f"[{page_num:02d}/{total_pages:02d}] Generado: {filename.encode('ascii', 'ignore').decode()}")
        
    print(f"\nProceso finalizado con exito! {len(generated_files)} certificados guardados en: {out_dir.resolve()}")
    return generated_files

if __name__ == "__main__":
    import sys
    pdf_file = sys.argv[1] if len(sys.argv) > 1 else "CertificadosConferfirmados.pdf"
    split_pdf_by_person(pdf_file)
