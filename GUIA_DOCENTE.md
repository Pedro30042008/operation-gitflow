# Guía para facilitar el workshop

1. Crea UN repositorio vacío en GitHub, sin inicializar README. Sube este paquete como `main` (puedes hacerlo con `git init`, `git add .`, `git commit`, `git branch -M main`, `git remote add origin URL`, `git push -u origin main`).
2. Crea `develop` desde `main` y publícala. Invita a ambos equipos como colaboradores con permiso de escribir. Si no tienen permisos, no podrán subir ramas al mismo remoto.
3. Pide que TODOS clonen **después** de crear `develop` y que ambos equipos creen sus features desde el mismo estado inicial de `develop`, **antes de fusionar cualquier PR**. Esto es necesario para que aparezca el conflicto previsto.
4. Cada equipo trabaja en su archivo propio Y en `panel/estado.md`. Alternan roles de conductor/navegador.
5. Cada equipo hace push y abre PR a `develop`. La revisión es cruzada, incluyendo al menos una petición concreta de mejora y una respuesta del autor.
6. Integra PR Aurora primero. El PR Órbita debería mostrar un conflicto en `panel/estado.md` porque ambas ramas reemplazaron el mismo texto inicial. Si no surge automáticamente, comprueba que ambos partieron del mismo commit de `develop`.
7. En Órbita: `git switch feature/orbita-aterrizaje`; `git fetch origin`; `git merge origin/develop`; abre `panel/estado.md`, elimina marcadores `<<<<<<<`, `=======`, `>>>>>>>`, redacta un estado de consenso, `git add panel/estado.md`, `git commit`, `git push`. No usar `git push --force`.
8. Tras aprobar Órbita, integra a `develop`. Un estudiante crea el PR final **develop → main**; otro lo revisa y aprueba; merge.
9. Evidencia: repositorio remoto con PR, comentarios, revisiones, historial y cambios. No pedir capturas ni reporte adicional. La única entrega escrita es la explicación final de Git Flow.

Nota: las opciones "Request changes" y "Approve" pueden depender de permisos y de si el usuario es autor del PR. En repositorios públicos también interviene la configuración de protección de ramas. La revisión es una actividad pedagógica obligatoria incluso si GitHub no impide técnicamente el merge.

## Si hay 3+ equipos
Crea tantas parejas de equipos como sea posible, cada pareja con su propia copia del repositorio; de lo contrario, los conflictos pueden mezclarse y cambiar el recorrido.
