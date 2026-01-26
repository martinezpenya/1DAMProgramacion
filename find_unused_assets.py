#!/usr/bin/env python3
import os
import re
import glob

def get_image_extensions():
    """Retorna las extensiones de archivo de imagen comunes"""
    return {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp', '.ico', '.xcf', '.mp4', '.avi', '.mov'}

def find_asset_files(docs_path):
    """Encuentra todos los archivos en carpetas assets dentro de UDxx"""
    asset_files = []
    
    # Buscar todas las carpetas UDxx/assets
    pattern = os.path.join(docs_path, 'UD*/assets/**')
    all_files = glob.glob(pattern, recursive=True)
    
    # Filtrar solo archivos (no directorios)
    for file_path in all_files:
        if os.path.isfile(file_path):
            # Obtener la ruta relativa desde docs
            rel_path = os.path.relpath(file_path, docs_path)
            asset_files.append({
                'full_path': file_path,
                'relative_path': rel_path,
                'filename': os.path.basename(file_path),
                'extension': os.path.splitext(file_path)[1].lower()
            })
    
    return asset_files

def find_markdown_files(docs_path):
    """Encuentra todos los archivos markdown"""
    pattern = os.path.join(docs_path, '**/*.md')
    return glob.glob(pattern, recursive=True)

def search_references_in_markdown(md_files, asset_files):
    """Busca referencias a archivos de assets en archivos markdown"""
    referenced_assets = set()
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Buscar referencias de imágenes markdown: ![](path) o ![alt](path)
            img_pattern = r'!\[.*?\]\(([^)]+)\)'
            matches = re.findall(img_pattern, content)
            
            # También buscar tags HTML <img src="path">
            html_img_pattern = r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>'
            html_matches = re.findall(html_img_pattern, content)
            
            all_matches = matches + html_matches
            
            for match in all_matches:
                # Limpiar la ruta (quitar parámetros de query, etc.)
                clean_path = match.split('?')[0].split('#')[0]
                referenced_assets.add(clean_path)
                
                # También agregar solo el nombre del archivo por si la referencia es solo por nombre
                filename = os.path.basename(clean_path)
                referenced_assets.add(filename)
                
        except Exception as e:
            print(f"Error leyendo {md_file}: {e}")
    
    return referenced_assets

def main():
    docs_path = './docs'
    
    print("=== Analizando archivos de assets no referenciados ===\n")
    
    # Encontrar todos los archivos en carpetas assets
    asset_files = find_asset_files(docs_path)
    print(f"Total de archivos en carpetas assets: {len(asset_files)}")
    
    # Encontrar todos los archivos markdown
    md_files = find_markdown_files(docs_path)
    print(f"Total de archivos markdown: {len(md_files)}\n")
    
    # Buscar referencias en markdown
    referenced_assets = search_references_in_markdown(md_files, asset_files)
    
    # Categorizar archivos
    image_extensions = get_image_extensions()
    unused_assets = []
    used_assets = []
    
    for asset in asset_files:
        is_referenced = False
        
        # Verificar diferentes formas de referencia
        checks = [
            asset['filename'],  # Solo nombre de archivo
            asset['relative_path'],  # Ruta relativa completa
            asset['relative_path'].replace('\\', '/'),  # Asegurar barras normales
            'assets/' + asset['filename'],  # Con prefijo assets/
        ]
        
        # También verificar rutas relativas desde diferentes UDs
        ud_match = re.match(r'(UD\d+)', asset['relative_path'])
        if ud_match:
            ud_name = ud_match.group(1)
            checks.append(f"{ud_name}/assets/{asset['filename']}")
            checks.append(f"./{ud_name}/assets/{asset['filename']}")
            checks.append(f"../{ud_name}/assets/{asset['filename']}")
        
        for check in checks:
            if check in referenced_assets:
                is_referenced = True
                break
        
        if is_referenced:
            used_assets.append(asset)
        else:
            unused_assets.append(asset)
    
    # Mostrar resultados
    print("=== ARCHIVOS NO REFERENCIADOS ===")
    if unused_assets:
        for asset in unused_assets:
            print(f"❌ {asset['relative_path']}")
        print(f"\nTotal no referenciados: {len(unused_assets)}")
    else:
        print("✅ Todos los archivos están siendo referenciados")
    
    print(f"\n=== RESUMEN ===")
    print(f"Total archivos en assets: {len(asset_files)}")
    print(f"Archivos referenciados: {len(used_assets)}")
    print(f"Archivos NO referenciados: {len(unused_assets)}")
    
    # Mostrar por tipo de archivo
    print(f"\n=== DESGLOSE POR TIPO ===")
    unused_by_ext = {}
    for asset in unused_assets:
        ext = asset['extension']
        if ext not in unused_by_ext:
            unused_by_ext[ext] = []
        unused_by_ext[ext].append(asset)
    
    for ext, files in unused_by_ext.items():
        print(f"{ext}: {len(files)} archivos")
        for file in files[:5]:  # Mostrar máximo 5 ejemplos
            print(f"  - {file['relative_path']}")
        if len(files) > 5:
            print(f"  ... y {len(files)-5} más")

if __name__ == "__main__":
    main()
