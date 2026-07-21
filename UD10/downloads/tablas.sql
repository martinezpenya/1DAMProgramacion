
/*
 * tabla proveedores
 */

CREATE TABLE proveedores (
  id int(11) AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(100) NOT NULL,
  fecha_ingreso date,
  salario decimal(10,2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

INSERT INTO proveedores (id, nombre, fecha_ingreso, salario) VALUES
(1, 'Juan Pérez', '2023-01-15', '3500.00'),
(2, 'María García', '2022-03-22', '4200.50'),
(3, 'Carlos López', '2021-07-10', '3100.75'),
(4, 'Ana Martínez', '2020-11-05', '2800.00'),
(5, 'Luis Rodríguez', '2022-05-18', '4500.00'),
(6, 'Marta Sánchez', '2023-04-27', '3300.60'),
(7, 'Pedro Fernández', '2021-12-30', '3700.40'),
(8, 'Laura Gómez', '2022-09-14', '2900.20'),
(9, 'Jorge Díaz', NULL, NULL),
(10, 'Isabel Morales', NULL, NULL);

/*
 * tabla empleados
 */

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    salario DECIMAL(10, 2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

INSERT INTO empleados (nombre, salario) VALUES
    ('Juan Perez', 2500.00),
    ('María García', 2800.00),
    ('Luis Hernández', 3000.00),
    ('Ana Martínez', 2700.00),
    ('Carlos Rodríguez', 3200.00),
    ('Laura Sánchez', 2900.00),
    ('Pedro López', 2600.00),
    ('Sofía Ramirez', 3100.00),
    ('Diego Gonzalez', 3300.00),
    ('Elena Fernandez', 2800.00),
    ('Javier Torres', 2950.00),
    ('Isabel Diaz', 2750.00),
    ('Miguel Ruiz', 2850.00),
    ('Paula Gomez', 2650.00),
    ('Antonio Sanchez', 3000.00);


/*
 * tabla productos
 */

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10, 2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;


INSERT INTO productos (nombre, precio) VALUES
    ('Camiseta', 15.99),
    ('Pantalón', 29.99),
    ('Zapatos', 49.99),
    ('Gorra', 9.99),
    ('Bufanda', 12.50),
    ('Calcetines', 5.99),
    ('Cinturón', 14.99),
    ('Sudadera', 24.99),
    ('Chaquetón', 79.99),
    ('Vestido', 39.99),
    ('Falda', 27.50),
    ('Chaqueta', 54.99),
    ('Bolso', 35.00),
    ('Bufanda', 12.50),
    ('Botas', 59.99),
    ('Sandalias', 34.99),
    ('Guantes', 8.99),
    ('Gafas de sol', 19.99),
    ('Paraguas', 17.50),
    ('Sombrero', 22.99);


/*
 * tabla alumnos
 */
CREATE TABLE alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;


INSERT INTO alumnos (nombre, edad) VALUES
    ('Juan', 20),
    ('María', 22),
    ('Luis', 21),
    ('Ana', 19),
    ('Carlos', 20),
    ('Laura', 23),
    ('Pedro', 21),
    ('Sofía', 20),
    ('Diego', 22),
    ('Elena', 19),
    ('Javier', 21),
    ('Isabel', 20);

/*
 * tabla libros
 */
CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    anio_publicacion INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

INSERT INTO libros (titulo, autor, anio_publicacion) VALUES
    ('El señor de los anillos', 'J.R.R. Tolkien', 1954),
    ('Cien años de soledad', 'Gabriel García Márquez', 1967),
    ('1984', 'George Orwell', 1949),
    ('Harry Potter y la piedra filosofal', 'J.K. Rowling', 1997),
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605),
    ('Orgullo y prejuicio', 'Jane Austen', 1813),
    ('Matar a un ruiseñor', 'Harper Lee', 1960),
    ('Crónica de una muerte anunciada', 'Gabriel García Márquez', 1981),
    ('El principito', 'Antoine de Saint-Exupéry', 1943),
    ('Rebelión en la granja', 'George Orwell', 1945),
    ('Rayuela', 'Julio Cortázar', 1963),
    ('Las aventuras de Tom Sawyer', 'Mark Twain', 1876),
    ('La sombra del viento', 'Carlos Ruiz Zafón', 2001),
    ('El alquimista', 'Paulo Coelho', 1988),
    ('Los juegos del hambre', 'Suzanne Collins', 2008);


/*
 * tabla ventas
 */
CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto VARCHAR(100),
    cantidad INT,
    total DECIMAL(10, 2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

INSERT INTO ventas (producto, cantidad, total) VALUES
    ('Camisa', 3, 45.00),
    ('Pantalón', 2, 60.00),
    ('Zapatos', 1, 35.00),
    ('Gorra', 5, 25.00),
    ('Bufanda', 2, 15.00),
    ('Calcetines', 4, 10.00),
    ('Cinturón', 3, 30.00),
    ('Sudadera', 2, 50.00),
    ('Chaquetón', 1, 80.00),
    ('Vestido', 2, 70.00),
    ('Falda', 3, 45.00),
    ('Chaqueta', 1, 60.00),
    ('Bolso', 2, 40.00),
    ('Botas', 1, 55.00),
    ('Sandalias', 3, 45.00),
    ('Guantes', 4, 20.00),
    ('Gafas de sol', 2, 30.00),
    ('Paraguas', 1, 15.00),
    ('Sombrero', 3, 25.00),
    ('Chaqueta de cuero', 1, 100.00);



/*
 * tabla pedidos
 */
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100),
    producto VARCHAR(100),
    cantidad INT,
    fecha DATE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

INSERT INTO pedidos (cliente, producto, cantidad, fecha) VALUES
    ('Juan Pérez', 'Camisa', 3, '2024-04-01'),
    ('María García', 'Pantalón', 2, '2024-04-02'),
    ('Luis Hernández', 'Zapatos', 1, '2024-04-03'),
    ('Ana Martínez', 'Gorra', 5, '2024-04-04'),
    ('Carlos Rodríguez', 'Bufanda', 2, '2024-04-05'),
    ('Laura Sánchez', 'Calcetines', 4, '2024-04-06'),
    ('Pedro López', 'Cinturón', 3, '2024-04-07'),
    ('Sofía Ramirez', 'Sudadera', 2, '2024-04-08'),
    ('Diego Gonzalez', 'Chaquetón', 1, '2024-04-09'),
    ('Elena Fernandez', 'Vestido', 2, '2024-04-10'),
    ('Javier Torres', 'Falda', 3, '2024-04-11'),
    ('Isabel Diaz', 'Chaqueta', 1, '2024-04-12'),
    ('Miguel Ruiz', 'Bolso', 2, '2024-04-13'),
    ('Paula Gomez', 'Botas', 1, '2024-04-14'),
    ('Antonio Sanchez', 'Sandalias', 3, '2024-04-15');


/*
 * tabla estudiantes
 */
CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    promedio DECIMAL(5, 2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

INSERT INTO estudiantes (nombre, edad, promedio) VALUES
    ('Juan', 20, 8.5),
    ('María', 21, 9.2),
    ('Luis', 19, 7.8),
    ('Ana', 22, 8.9),
    ('Carlos', 20, 7.5),
    ('Laura', 23, 9.8),
    ('Pedro', 21, 8.2),
    ('Sofía', 20, 8.7),
    ('Diego', 22, 8.4),
    ('Elena', 19, 9.0),
    ('Javier', 21, 7.9),
    ('Isabel', 20, 9.3);


/*
 * tabla vendedores
 */
CREATE TABLE vendedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    fecha_ingreso DATE,
    salario DECIMAL(10, 2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

INSERT INTO vendedores (nombre, fecha_ingreso, salario) VALUES
    ('Juan Pérez', '2023-05-15', 2500.00),
    ('María García', '2023-06-20', 2800.00),
    ('Luis Hernández', '2023-07-10', 3000.00),
    ('Ana Martínez', '2023-08-05', 2700.00),
    ('Carlos Rodríguez', '2023-09-12', 3200.00),
    ('Laura Sánchez', '2023-10-18', 2900.00),
    ('Pedro López', '2023-11-25', 2600.00),
    ('Sofía Ramirez', '2023-12-02', 3100.00),
    ('Diego Gonzalez', '2024-01-08', 3300.00),
    ('Elena Fernandez', '2024-02-14', 2800.00),
    ('Javier Torres', '2024-03-20', 2950.00),
    ('Isabel Diaz', '2024-04-01', 2750.00),
    ('Miguel Ruiz', '2024-05-05', 2850.00),
    ('Paula Gomez', '2024-06-10', 2650.00),
    ('Antonio Sanchez', '2024-07-15', 3000.00),
    ('Lucía Martín', '2024-08-20', 2700.00),
    ('Marcos Rodriguez', '2024-09-25', 3200.00),
    ('Carmen Gutiérrez', '2024-10-30', 2900.00),
    ('Jorge Navarro', '2024-11-05', 2600.00),
    ('Marina Suarez', '2024-12-10', 3100.00),
    ('Pablo Lopez', '2025-01-15', 3300.00),
    ('Sara González', '2025-02-20', 2800.00),
    ('Daniel García', '2025-03-25', 2950.00),
    ('Laura Fernández', '2025-04-30', 2750.00),
    ('Alejandro Martínez', '2025-05-05', 2850.00),
    ('Cristina Sánchez', '2025-06-10', 2650.00),
    ('David Pérez', '2025-07-15', 3000.00),
    ('Eva Martín', '2025-08-20', 2700.00),
    ('Gonzalo Rodríguez', '2025-09-25', 3200.00),
    ('Beatriz López', '2025-10-30', 2900.00);
