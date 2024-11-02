import reflex as rx
from .styles import titulo_columna, tarjeta_tarea, columna_kanban2, boton, tablero, estilos
from .imagenes import *

class State(rx.State):
    mostrar_solo_disponibles: bool = False

    def mostrar_pendientes(self):
        self.mostrar_solo_disponibles = True

    def mostrar_todas(self):
        self.mostrar_solo_disponibles = False

def contar_tareas_por_estado(tareas):
    contadores = {}
    for tarea in tareas:
        estado = tarea["estado"]
        if estado in contadores:
            contadores[estado] += 1
        else:
            contadores[estado] = 1
    return contadores

def tarjeta_tarea2(tarea):
    fondo = estilos["fondo_tarea"].get(tarea['estado'], "#fff")
    return rx.box(
        rx.image(src=tarea['imagen'], alt=tarea['Titulo'], width="100%", height="auto"),  # Cargar la imagen
        rx.text(f"Título: {tarea['Titulo']}", font_size="18px", font_weight="bold", color="#2c3e50"),
        rx.text(f"Estado: {tarea['estado']}", font_size="16px", color="gray"),
        rx.text(f"Autor: {tarea['Autor']}", font_size="14px", color="#7f8c8d", margin_top="5px"),
        style={"background": fondo, **estilos["tarjeta_tarea"]},
        padding="10px",  # Espaciado interno
        border_radius="8px",  # Esquinas redondeadas
        box_shadow="0 2px 4px rgba(0, 0, 0, 0.1)",  # Sombra
    )



def columna_kanban(nombre, tareas):
    return rx.box(
        rx.heading(nombre, style=titulo_columna),
        rx.cond(
            State.mostrar_solo_disponibles,
            rx.vstack(
                *[tarjeta_tarea(tarea) for tarea in tareas if tarea["estado"] == "Disponible"],
                spacing="10px"
            ),
            rx.vstack(
                *[tarjeta_tarea(tarea) for tarea in tareas],
                spacing="10px"
            )
        ),
        style=columna_kanban2
    )

def form_crear_tarea():
    return

def index():
    libros = [
       {"Titulo": "Harry Potter and the Philosopher's Stone", "estado": "Agotado", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/images.jpg"},
        {"Titulo": "The Jungle Book", "estado": "Disponible", "Autor": "Rudyard Kipling", "categoria": "Fantasía", "imagen": "imagenes/libro de la selva.jpg"},
        {"Titulo": "Treasure Island", "estado": "Disponible", "Autor": "R.L. Stevenson", "categoria": "Fantasía", "imagen": "imagenes/isladel tesore.jpg"},
        {"Titulo": "From the Earth to the Moon", "estado": "Disponible", "Autor": "Jules Verne", "categoria": "Fantasía", "imagen": "imagenes/earth to the moon.jpg"},
        {"Titulo": "Around The World In Eighty Days", "estado": "Disponible", "Autor": "Jules Verne", "categoria": "Fantasía", "imagen": "imagenes/around-world.jpg"},
        {"Titulo": "The Alchemist", "estado": "Disponible", "Autor": "Paulo Coelho", "categoria": "Fantasía", "imagen": "imagenes/alchemist.jpg"},
        {"Titulo": "To Kill a Mockingbird", "estado": "Disponible", "Autor": "Harper Lee", "categoria": "Fantasía", "imagen": "imagenes/harpen lee to_.jpg"},
        {"Titulo": "Do Epic Shit", "estado": "Disponible", "Autor": "Ankur Warikoo", "categoria": "Fantasía", "imagen": "imagenes/do-epic-shit.jpg"},
        {"Titulo": "Harry Potter and the Chamber of Secrets", "estado": "Disponible", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/camara-de-los-secretos.jpg"},
        {"Titulo": "The Subtle Art of Not Giving a F*ck", "estado": "Disponible", "Autor": "Mark Manson", "categoria": "Fantasía", "imagen": "imagenes/fuck.jpg"},
        {"Titulo": "Ikigai", "estado": "Disponible", "Autor": "Héctor García", "categoria": "Fantasía", "imagen": "imagenes/the japense secret.jpg"},
        {"Titulo": "LINCHPIN", "estado": "Disponible", "Autor": "Seth Godin", "categoria": "Fantasía", "imagen": "imagenes/linchpin seth godin.jpg"},
        {"Titulo": "Harry Potter and the Prisoner of Azkaban", "estado": "Disponible", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/prisionero de azka_.jpg"},
        {"Titulo": "Harry Potter and the Goblet of Fire", "estado": "Disponible", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/calis-de-fuego.jpg"},
        {"Titulo": "Harry Potter and the Order of the Phoenix", "estado": "Agotado", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/orden fenix.jpg"},
        {"Titulo": "Harry Potter and the Half Blood Prince", "estado": "Disponible", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/principe-mestizo_.jpg"},
        {"Titulo": "Harry Potter and the Deathly Hallows", "estado": "Agotado", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/reliquias_.jpg"},
    ]

    contadores = contar_tareas_por_estado(libros)

    return rx.box(
    rx.vstack(
        # Contenedor para los botones
        rx.hstack(
            rx.button("Mostrar Pendientes", on_click=State.mostrar_pendientes, style=boton),
            rx.button("Mostrar Todas", on_click=State.mostrar_todas, style=boton),
            spacing="20px",
        ),
        
        # Espacio entre los botones y el grid
        rx.box(height="20px"),

        # Cuadrícula de libros en filas de 3 columnas
        rx.grid(
            rx.foreach(
                libros,
                lambda tarea: tarjeta_tarea2(tarea)
            ),
            columns="3",
            spacing="4",
            width="100%",
        ),
        
        # Contadores de tareas debajo del grid
        rx.hstack(
            rx.heading(f"Agotados: {contadores.get('Agotado', 0)}", color="black"),
            rx.heading(f"Disponibles: {contadores.get('Disponible', 0)}", color="black"),
            spacing="6",
        ),
    ),
    style=tablero,
    padding="20px",
)


app = rx.App()
app.add_page(index, route="/")
app._compile()
