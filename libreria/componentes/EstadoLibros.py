import reflex as rx

class EstadoLibros(rx.State):
    libros: list[dict[str, str | float]] = [
        {"id": 1, "Titulo": "Harry Potter and the Philosopher's Stone", "estado": "Agotado", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/images.jpg"},
        {"id": 2, "Titulo": "The Jungle Book", "estado": "Disponible", "Autor": "Rudyard Kipling", "categoria": "Fantasía", "imagen": "imagenes/libro de la selva.jpg"},
        {"id": 3, "Titulo": "Treasure Island", "estado": "Disponible", "Autor": "R.L. Stevenson", "categoria": "Fantasía", "imagen": "imagenes/isladel tesore.jpg"},
        {"id": 4, "Titulo": "From the Earth to the Moon", "estado": "Disponible", "Autor": "Jules Verne", "categoria": "Fantasía", "imagen": "imagenes/earth to the moon.jpg"},
        {"id": 5, "Titulo": "Around The World In Eighty Days", "estado": "Disponible", "Autor": "Jules Verne", "categoria": "Fantasía", "imagen": "imagenes/around-world.jpg"},
        {"id": 6, "Titulo": "The Alchemist", "estado": "Disponible", "Autor": "Paulo Coelho", "categoria": "Fantasía", "imagen": "imagenes/alchemist.jpg"},
        {"id": 7, "Titulo": "To Kill a Mockingbird", "estado": "Disponible", "Autor": "Harper Lee", "categoria": "Fantasía", "imagen": "imagenes/harpen lee to_.jpg"},
        {"id": 8, "Titulo": "Do Epic Shit", "estado": "Disponible", "Autor": "Ankur Warikoo", "categoria": "Fantasía", "imagen": "imagenes/do-epic-shit.jpg"},
        {"id": 9, "Titulo": "Harry Potter and the Chamber of Secrets", "estado": "Disponible", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/camara-de-los-secretos.jpg"},
        {"id": 10, "Titulo": "The Subtle Art of Not Giving a F*ck", "estado": "Disponible", "Autor": "Mark Manson", "categoria": "Fantasía", "imagen": "imagenes/fuck.jpg"},
        {"id": 11, "Titulo": "Ikigai", "estado": "Disponible", "Autor": "Héctor García", "categoria": "Fantasía", "imagen": "imagenes/the japense secret.jpg"},
        {"id": 12, "Titulo": "LINCHPIN", "estado": "Disponible", "Autor": "Seth Godin", "categoria": "Fantasía", "imagen": "imagenes/linchpin seth godin.jpg"},
        {"id": 13, "Titulo": "Harry Potter and the Prisoner of Azkaban", "estado": "Disponible", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/prisionero de azka_.jpg"},
        {"id": 14, "Titulo": "Harry Potter and the Goblet of Fire", "estado": "Disponible", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/calis-de-fuego.jpg"},
        {"id": 15, "Titulo": "Harry Potter and the Order of the Phoenix", "estado": "Agotado", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/orden fenix.jpg"},
        {"id": 16, "Titulo": "Harry Potter and the Half Blood Prince", "estado": "Disponible", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/principe-mestizo_.jpg"},
        {"id": 17, "Titulo": "Harry Potter and the Deathly Hallows", "estado": "Agotado", "Autor": "J.K. Rowling", "categoria": "Fantasía", "imagen": "imagenes/reliquias_.jpg"},
    ]
    
    carrito: list[dict[str, str | float]] = []

    def agregar_al_carrito(cls, libro: dict[str, str | float]):
        cls.carrito.append(libro)

    def vaciar_carrito(cls):
        cls.carrito.clear()
