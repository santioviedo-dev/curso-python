def cargar_eventos() -> list[tuple[str, str]]:
    try:
        with open("../eventos.txt", "r") as f:
            return [linea.strip().split(",") for linea in f.readlines()]
    except FileNotFoundError:
        return []

def guardar_evento(nombre: str, fecha_str: str) -> None:
    with open("../eventos.txt", "a") as f:
        f.write(f"{nombre},{fecha_str}\n")