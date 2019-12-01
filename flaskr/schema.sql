CREATE TABLE
IF NOT EXISTS users
(
  unqiueId INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  homeAddress TEXT,
  workAddress TEXT,
  newsPreference TEXT
);