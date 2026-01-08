-- Tabel untuk menyimpan data pengguna
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

-- Tabel untuk menyimpan data pertanyaan voting
CREATE TABLE polls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    creator_id INTEGER,
    FOREIGN KEY (creator_id) REFERENCES users (id)
);

-- Tabel untuk menyimpan suara (voting)
CREATE TABLE votes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    poll_id INTEGER,
    choice TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (poll_id) REFERENCES polls (id),
    UNIQUE(user_id, poll_id) -- Supaya 1 user cuma bisa vote 1 kali di poll yang sama
);