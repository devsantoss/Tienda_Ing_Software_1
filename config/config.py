from typing import Dict, List

urls: dict[str, list[str]] = {
    "pedidos-estado/": ["http://tienda:5000/pedidos/cambiarestado/"],
    "pedidos-update/": ["http://tienda:5000/pedidos/update/"],
    "carrito/": ["http://tienda:5000/carrito/"],
    "carrito-add/": ["http://tienda:5000/carrito/add/"],
    "carrito-empty/": ["http://tienda:5000/carrito/empty/"],
    "carrito-delete/": ["http://tienda:5000/carrito/delete/"],
    "productos/": ["http://tienda:5000/"],
    "productos-delete/": ["http://tienda:5000/productos/eliminar/"]
}

origin = ["http://tienda:5000/"]
