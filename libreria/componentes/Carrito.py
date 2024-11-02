import reflex as rx
from .EstadoLibros import EstadoLibros

def carrito():
    return rx.fragment(
        rx.heading("Carrito"),
        rx.list.unordered(
            rx.foreach(EstadoLibros.carrito, lambda libro: rx.list_item(libro["Titulo"]))
        ),
        rx.button("Vaciar Carrito", on_click=EstadoLibros.vaciar_carrito)
    )

