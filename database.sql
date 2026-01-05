CREATE DATABASE varahi_db;

\c varahi_db;

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    arrival_time TIME,
    members INT,
    trips INT,
    total_cost INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
