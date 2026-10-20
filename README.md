# MISIÓN: RESCATE DEL REPOSITORIO 🚀

## Contexto
El Centro de Control perdió su guía de operación justo antes de una misión.
Dos equipos deberán reconstruirla sin pisar los cambios del otro. ¡Cada modificación pasa por Pull Request!

## Reglas del juego
- **Una sola copia remota** del repositorio compartido por pareja de equipos.
- Dos equipos: **Aurora** y **Órbita**. Todos trabajan sobre el mismo repositorio remoto.
- `main` = versión publicada; `develop` = zona de integración; `feature/...` = trabajo aislado.
- No modificar `main` ni `develop` directamente durante el juego.
- Cada PR debe tener un autor y revisores del otro equipo.
- Los demás integrantes alternan los roles de conductor y navegador.

## Archivos para el reto
- `panel/estado.md`: archivo compartido que provocará el conflicto deliberado.
- `misiones/aurora.md` y `misiones/orbita.md`: hojas de trabajo por equipo.
- `manual/comandos.md`: guía inicial que completarán durante el taller.
- `.github/PULL_REQUEST_TEMPLATE.md`: texto guía que GitHub carga al abrir un PR.
- `scripts/verificar.py`: comprobación local opcional que no necesita dependencias.

**Inicio:** el docente creará el repositorio remoto desde estos archivos, con `main` y `develop`, e invitará a los participantes como colaboradores con permisos de escritura.

## Objetivo final
Completar dos PR revisados, corregidos e integrados a `develop`; resolver el conflicto; abrir un PR `develop` → `main` y explicar por escrito el Git Flow recorrido. La **única entrega escrita** es esa explicación final. La evidencia práctica queda en GitHub.
