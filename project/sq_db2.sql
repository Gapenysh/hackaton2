CREATE TABLE teams (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    size INTEGER NOT NULL,
    roles TEXT NOT NULL,
    members TEXT,
    status TEXT NOT NULL DEFAULT 'pending'
);
