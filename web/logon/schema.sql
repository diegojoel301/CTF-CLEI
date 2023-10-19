CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

-- -P@$$w0rd777_666
INSERT INTO users (username, password) VALUES ('rodrigo', '9982baea1823c1c239e1f5bcbd4f424a');
INSERT INTO users (username, password) VALUES ('maria', '9982baea1823c1c239e1f5bcbd4f424a');
INSERT INTO users (username, password) VALUES ('jose', '9982baea1823c1c239e1f5bcbd4f424a');
INSERT INTO users (username, password) VALUES ('admin', '9982baea1823c1c239e1f5bcbd4f424a');
INSERT INTO users (username, password) VALUES ('isabel', '9982baea1823c1c239e1f5bcbd4f424a');



