-- Crear la tabla User
CREATE TABLE User (
    id TEXT PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    description TEXT
);

-- Crear la tabla Book
CREATE TABLE Book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name TEXT NOT NULL,
    author TEXT NOT NULL
);

-- Insertar registros de ejemplo en la tabla User
INSERT INTO User (id, username, password, description) VALUES 
('352f6vd32', 'alice', 'password123', 'Alice loves reading mystery novels.'),
('45g7hj89k', 'bob', 'securepass', 'Bob is a fan of historical fiction.'),
('98j4k0lmp5', 'charlie', 'charliepass', 'Charlie reads a variety of genres.'),
('6837cbcc5', 'juan', 'juanpa666', 'FLAG{ju4n_1s_th3_0wn3r_0f_th3_l1br4ry}');

-- Insertar registros de ejemplo en la tabla Book
INSERT INTO Book (book_name, author) VALUES 
('The Great Gatsby', 'F. Scott Fitzgerald'),
('To Kill a Mockingbird', 'Harper Lee'),
('1984', 'George Orwell'),
('Pride and Prejudice', 'Jane Austen'),
('The Catcher in the Rye', 'J.D. Salinger');

