import zipfile
import json
import shutil
from pathlib import Path

BASE = Path("temp")

def extrair_zip(zip_path, destino):
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(destino)

def ler_manifest(pasta):
    with open(pasta / "manifest.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["header"]["uuid"], data["header"]["version"]

def atualizar_world_json(arquivo, uuid, version):
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = json.load(f)

    conteudo.append({
        "pack_id": uuid,
        "version": version
    })

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(conteudo, f, indent=4)

def copiar_pasta(origem, destino):
    shutil.copytree(origem, destino, dirs_exist_ok=True)
