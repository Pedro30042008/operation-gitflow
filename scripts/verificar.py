#!/usr/bin/env python3
"""Comprobación local opcional, sin bibliotecas adicionales."""
from pathlib import Path

base = Path(__file__).resolve().parents[1]
archivos = ["panel/estado.md", "misiones/aurora.md", "misiones/orbita.md", "manual/comandos.md"]
print("CENTRO DE CONTROL — comprobación de archivos")
for ruta in archivos:
    p = base / ruta
    print(("OK" if p.is_file() else "FALTA") + "  " + ruta)

panel = (base / "panel/estado.md").read_text(encoding="utf-8")
print("
Estado actual:")
for linea in panel.splitlines():
    if "ESTADO DE LA MISIÓN:" in linea:
        print(linea)
print("
Recuerda: el resultado final debe reflejar los acuerdos de ambos equipos.")
