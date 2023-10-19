CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );


CREATE TABLE posts (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );

INSERT INTO users (username, password) VALUES ('alice', '5f4dcc3b5aa765d61d8327deb882cf99'); -- Password: password (en MD5)
INSERT INTO users (username, password) VALUES ('bob', 'e9eb1f08a1293e97b6276cdbc0575046');   -- Password: P@$$w0rd_Pwn3d (en MD5)
INSERT INTO users (username, password) VALUES ('charlie', '9f9d51bc70ef21ca5c14f307980a29d8'); -- Password: bob (en MD5)

-- Alice crea dos publicaciones
INSERT INTO posts (title, content, user_id) VALUES ('My First Post', 'This is the content of my first post!', 1);
INSERT INTO posts (title, content, user_id) VALUES ('Vacation Pics', 'La contraseña es: P@$$w0rd_Pwn3d', 1);

-- Bob crea una publicación
INSERT INTO posts (title, content, user_id) VALUES ('My Favorite Games', 'FLAG{s3arch_fl4g_1n_th3_d1ff3r3nt_us3rs}', 2);

-- Charlie crea una publicación
INSERT INTO posts (title, content, user_id) VALUES ('Cooking Tips', 'Always season your food!', 3);
