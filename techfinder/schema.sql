DROP TABLE IF EXISTS techniques;

CREATE TABLE techniques (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    category TEXT,
    name TEXT UNIQUE NOT NULL,
    prerequisite TEXT,
    rank INTEGER NOT NULL,
    activation TEXT,
    effect TEXT,
    opportunity TEXT,
    ring TEXT
);