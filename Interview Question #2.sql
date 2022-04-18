
-- Create tables guests, rooms, reservations

CREATE TABLE guests(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE
);

CREATE TABLE rooms(
    id SERIAL PRIMARY KEY NOT NULL,
    price INTEGER NOT NULL,
    bed_number INTEGER NOT NULL,
    availble BOOLEAN DEFAULT TRUE
);

CREATE TABLE reservations(
    id SERIAL PRIMARY KEY NOT NULL,
    nights INTEGER NOT NULL,
    package VARCHAR(50) NOT NULL,
    roomID INTEGER NOT NULL,
    guestID INTEGER NOT NULL,
    FOREIGN KEY (roomID) REFERENCES rooms(id),
    FOREIGN KEY (guestID) REFERENCES guests(id)
);


-- Insert values in to the tables

INSERT INTO guests (name, email) VALUES
('Jhon Doe',  'john.doe@gmail.com'),
('Max Thomas', 'max.thomas@gmail.com'),
('Will Smith', 'will.smith@gmail.com'),
('Bob Clark', 'bob.clark@gmail.com'),
('Tom Allen', 'tom.allen@gmail.com');

INSERT INTO rooms (price, bed_number, availble) VALUES
(45, 2, FALSE),
(150, 1, TRUE),
(60, 1, FALSE),
(80, 3, TRUE),
(40, 2, TRUE);

INSERT INTO reservations (nights, package, roomID, guestID) VALUES
(3, 'GOLD', 1, 3),
(1, 'STUDENT', 3, 5);

-- Query for avaliable rooms 

SELECT *
FROM rooms
WHERE rooms.availble = TRUE;


-- pull up guest information in a room

SELECT guests.name, roomID
FROM reservations
INNER JOIN guests ON (reservations.guestID = guests.id)
ORDER BY guest.name;


-- guest checkout

UPDATE rooms
SET availble = TRUE
WHERE id = 3;

DELETE
FROM reservations
WHERE roomID = 3;
