CREATE TABLE "Usuario" (
	"id_usuario"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"apellido"	TEXT NOT NULL,
	"tipo_usuario"	INTEGER NOT NULL,
	"esta_activo"	INTEGER NOT NULL,
	"fecha_creacion"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("id_usuario" AUTOINCREMENT)
);

CREATE TABLE "Estado_Pedido" (
	"id_estado"	INTEGER NOT NULL,
	"descripcion"	TEXT,
	PRIMARY KEY("id_estado" AUTOINCREMENT)
);

CREATE TABLE "Articulos" (
	"id_articulo"	INTEGER NOT NULL,
	"descripcion"	TEXT NOT NULL,
	"descuento"	REAL NOT NULL,
	PRIMARY KEY("id_articulo" AUTOINCREMENT)
);

CREATE TABLE "Tipo_Pago" (
	"id_tipo_pago"	INTEGER NOT NULL,
	"descripcion"	TEXT NOT NULL,
	PRIMARY KEY("id_tipo_pago" AUTOINCREMENT)
);

CREATE TABLE "Pedido" (
	"id_pedido"	INTEGER NOT NULL,
	"cliente"	INTEGER NOT NULL,
	"usuario_atiende"	INTEGER NOT NULL,
	"estado"	INTEGER NOT NULL,
	"tipo_pago"	INTEGER NOT NULL,
	PRIMARY KEY("id_pedido" AUTOINCREMENT),
	FOREIGN KEY (cliente) REFERENCES Usuario(id_usuario),
	FOREIGN KEY (usuario_atiende) REFERENCES Usuario(id_usuario),
	FOREIGN KEY (estado) REFERENCES Estado_Pedido(id_estado),
	FOREIGN KEY (tipo_pago) REFERENCES Tipo_Pago(id_tipo_pago)
);

CREATE TABLE "Articulos_Pedido" (
	"id_pedido"	INTEGER NOT NULL,
	"id_articulo"	INTEGER NOT NULL,
	FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
	FOREIGN KEY (id_articulo) REFERENCES Articulos(id_articulo)
);