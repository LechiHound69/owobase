import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.database import SessionLocal, engine, Base
from src.models import Usuario, Nota

print("Creando tablas en Neon uwu")
# Base.metadata.create_all(bind=engine)
print("Tabla lista UwU")

db = SessionLocal()


def crear():
    print("--- 1. Metiendo xd ---")
    lechi = Usuario(nombre="Lechi Master", email="shawrigoberto@gmail.com", edad=19)

    nota1 = Nota(titulo="Recordatorio", contenido="Recuerda seguir siendo el mejor :)")
    nota2 = Nota(titulo="Obras maestras", contenido="Beastars, JJBA, HxH")

    lechi.notas.append(nota1)
    lechi.notas.append(nota2)

    db.add(lechi)

    db.commit()

    db.refresh(lechi)

    print("Usuario y notas creadas OwO: {lechi}")


def consultar():
    print("\n--- 2. Consultando xd ---")
    usuario_encontrado = (
        db.query(Usuario).filter(Usuario.nombre == "Lechi Master").first()
    )
    print(f"Lo encontré en la DB OwO: {usuario_encontrado.nombre}")
    print("Sus notas guardadas son:")
    for nota in usuario_encontrado.notas:
        print(f" - {nota.titulo}: {nota.contenido}")
    return usuario_encontrado


def actualizar(usuario_encontrado):
    print("\n--- 3. Actualizando xd ---")
    usuario_encontrado.edad = 20
    usuario_encontrado.nombre = "Lechi God UwU"

    db.commit()
    print("Usuario actualizado :3")


def borrar(usuario_encontrado):
    print("\n--- 4. BORRANDO ---")
    db.delete(usuario_encontrado)
    db.commit()
    print("za hando gakesu")

    check = db.query(Usuario).filter(Usuario.nombre == "Lechi God UwU").first()
    print(f"Sigues existiendo?: {check}")

    db.rollback()


def actualizar_notas():
    nota1 = (
        db.query(Nota)
        .filter(Nota.id == 1 and Nota.usuario_id == usuario_encontrado.id)
        .first()
    )
    nota1.titulo = "Recordatorio diario :3"

    nota2 = (
        db.query(Nota)
        .filter(Nota.id == 2, Nota.usuario_id == usuario_encontrado.id)
        .first()
    )
    nota2.contenido = "Beastars, JJBA, HxH, Pokémon (Los juegos)"

    db.commit()


usuario_encontrado = None

while True:
    print(
        "Ingrese una opción xdxdxddd:\n1. Crear usuario\n2. Consultar usuario\n3. Actualizar usuario\n4. Borrar usuario\n5. Actualizar notas\n6. Salir"
    )
    opcion = input()
    match opcion:
        case "1":
            crear()
        case "2":
            usuario_encontrado = consultar()
        case "3":
            if usuario_encontrado == None:
                print("Aún no hay ningún usuario encontrado para actualizar UnU")
            else:
                actualizar(usuario_encontrado)
        case "4":
            if usuario_encontrado == None:
                print("Aún no hay ningún usuario encontrado para borrar UnU")
            else:
                borrar(usuario_encontrado)
        case "5":
            if usuario_encontrado == None:
                print("Aún no hay ningún usuario para buscar notas UnU")
            else:
                actualizar_notas()
        case "6":
            db.close()
            print("Saliendo TwT")
            break
        case _:
            print("Opción incorrecta UnU, saliendo")
