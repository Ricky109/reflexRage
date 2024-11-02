import reflex as rx
from .EstadoLibros import EstadoLibros

def detalles_libro(libro_id: int):
    libro = EstadoLibros.libros[libro_id]  # Suponiendo que el ID es el índice
    return rx.column(
        [
            rx.heading(libro["Titulo"]),
            rx.text(f"Autor: {libro['Autor']}"),
            rx.text(f"Precio: ${libro['estado']}"),  # Suponiendo que 'estado' es un placeholder para el precio
            rx.text(libro["descripcion"]),
            rx.button("Agregar al carrito", on_click=lambda: EstadoLibros.agregar_al_carrito(libro)),
        ]
    )
