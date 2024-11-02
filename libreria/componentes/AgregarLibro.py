import reflex as rx
from .EstadoLibros import EstadoLibros

def agregar_libro():
    return rx.fragment(
        rx.input(placeholder="Nombre del libro", on_change=EstadoLibros.set_nuevo_libro_nombre),
        rx.input(placeholder="Autor", on_change=EstadoLibros.set_nuevo_libro_autor),
        rx.input(placeholder="Precio", on_change=EstadoLibros.set_nuevo_libro_precio),
        rx.input(placeholder="Descripción", on_change=EstadoLibros.set_nuevo_libro_descripcion),
        rx.button("Agregar Libro", on_click=EstadoLibros.agregar_libro),
    )
