CREATE TABLE urls (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL UNIQUE,
    created_at DATE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE url_checks (
    id SERIAL PRIMARY KEY,
    url_id INTEGER REFERENCES urls(id) ON DELETE CASCADE,
    status_code INTEGER,
    h1 varchar(255),
    title varchar(255),
    description varchar(255),
    created_at DATE DEFAULT CURRENT_TIMESTAMP
);