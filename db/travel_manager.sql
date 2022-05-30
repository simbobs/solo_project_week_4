PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    visited BOOLEAN DEFAULT FALSE
);

CREATE TABLE cities (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    visited BOOLEAN DEFAULT FALSE,
    country_id INTEGER NOT NULL,
        FOREIGN KEY (country_id)
            REFERENCES countries(id)
        
);

-- extension stuff
CREATE TABLE sights (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    comment TEXT,
    city_id INTEGER NOT NULL,
        FOREIGN KEY (city_id)
            REFERENCES cities (id)
)

