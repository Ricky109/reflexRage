"""import reflex as rx
from .styles import titulo_columna, tarjeta_tarea, columna_kanban2, boton, tablero, estilos
from .imagenes import *
from .componentes.EstadoLibros import EstadoLibros
from .componentes.Carrito import carrito

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
        rx.image(src=tarea['imagen'], alt=tarea['Titulo'], width="100%", height="auto"),
        rx.text(f"Título: {tarea['Titulo']}", font_size="18px", font_weight="bold", color="#2c3e50"),
        rx.text(f"Estado: {tarea['estado']}", font_size="16px", color="gray"),
        rx.text(f"Autor: {tarea['Autor']}", font_size="14px", color="#7f8c8d", margin_top="5px"),
        style={"background": fondo, **estilos["tarjeta_tarea"]},
        padding="10px",
        border_radius="8px",
        box_shadow="0 2px 4px rgba(0, 0, 0, 0.1)",
    )

def index():
    libros = EstadoLibros.libros()  # Llamamos a la variable Var para obtener su contenido
    contadores = contar_tareas_por_estado(libros)

    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.button("Mostrar Pendientes", on_click=State.mostrar_pendientes, style=boton),
                rx.button("Mostrar Todas", on_click=State.mostrar_todas, style=boton),
                spacing="20px",
            ),
            rx.box(height="20px"),
            rx.grid(
                rx.foreach(
                    libros,
                    lambda tarea: tarjeta_tarea2(tarea)
                ),
                columns="3",
                spacing="4",
                width="100%",
            ),
            spacing="20px",
            padding="20px",
            style={"background": "#f8f9fa", "border-radius": "10px", "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)"},
        ),
        carrito()
    )

app = rx.App()
app.add_page(index, route="/")
app._compile()"""
