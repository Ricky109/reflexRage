import reflex as rx
from .EstadoLibros import EstadoLibros

def lista_libros():
    return rx.fragment(
        rx.heading("Lista de Libros"),
        rx.vstack(
            rx.foreach(
                EstadoLibros.libros,
                lambda libro: rx.list_item(
                    rx.heading(libro["Titulo"]),
                    rx.text(f"Autor: {libro['Autor']}"),
                    rx.text(f"Estado: {libro['estado']}"),
                    rx.text(libro["descripcion"]),
                    rx.button("Agregar al Carrito", on_click=lambda libro=libro: EstadoLibros.agregar_al_carrito(libro))
                )
            ),
        ),
        rx.link("Ver Carrito", href="/carrito")
    )

