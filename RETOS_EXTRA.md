# Cartas sorpresa: desbloquea comandos útiles

No entreguen esta hoja: deben demostrar cada descubrimiento en pantalla y explicarlo al otro equipo.

## Reto 1 — Detective del historial
- `git log --oneline --graph --decorate --all` muestra las ramas como un mapa.
- `git show HEAD` revela el último commit.
- `git diff` enseña cambios aún no preparados y `git diff --staged` los ya preparados.
- `git blame panel/estado.md` identifica quién modificó cada línea (úsalo sin culpar personas).

## Reto 2 — Saltos y rescates
- `git switch -` regresa a la rama anterior.
- `git restore -- manual/comandos.md` descarta SOLO cambios sin commit en ese archivo: ¡primero asegúrate de que no los necesitas!
- `git stash push -m "pausa de mision"` guarda temporalmente cambios sin commit; `git stash list` los muestra y `git stash pop` los recupera. Hazlo solo en un cambio de prueba.
- `git reflog` sirve para encontrar dónde apuntaba HEAD. **Solo mirar** en este taller.

## Reto 3 — Cambio de último minuto (opcional)
- Después de abrir el PR, haz otro commit y push a **la misma rama**: el PR se actualiza solo.
- `git fetch origin` descarga referencias sin fusionar tus archivos.
- `git diff origin/develop...HEAD` muestra la diferencia relevante desde el punto de separación de tu feature.
- `git cherry-pick <hash>` permite aplicar un commit de otra rama: solo demostrarlo en una rama de ensayo, nunca sobre main.

## Poderes prohibidos durante el taller
No usar `git reset --hard`, `git clean -fd`, `git push --force` ni `git rebase` en ramas compartidas. Si algo parece perdido, levantar la mano y mostrar `git status` y `git reflog`.
