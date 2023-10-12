CREATE Table Classes (
    class TEXT NOT NULL, 
    type TEXT NOT NULL,
    country TEXT NOT NULL,
    numGuns INT NOT NULL,
    bore INT NOT NULL,
    displacement INT NOT NULL
);


CREATE TABLE Ships(
    name text NOTNULL,
    class text NOTNULL,
    launched text NOTNULL,
);

INSERT INTO ships(name,class,launched)
VALUES
("California","Tennessee",1915),
("Haruma","Kongo",1915);

CREATE TABLE Battles(
    name TEXT NOTNULL
    date TEXT NOTNULL
);

INSERT Into Battles(name,date)
VALUES
("denmark Strait","05/24/41");

INSERT INTO Classes (class, type, country, numGuns, bore, displacement)
VALUES
("Bismarck", "bb", "Germany", 8, 15, 42000),
("Iowa", "bb", "USA", 9, 16, 46000),
("Kongo", "bc", "Japan", 8, 14, 32000),
("North Carolina", "bb", "USA", 9, 16, 37000),
("Renown", "bc", "Britain", 6, 15, 32000),
("Revenge", "bb", "Britain", 8, 15, 29000),
("Tennessee", "bb", "USA", 12, 14, 32000),
("Yamato", "bb", "Japan", 9, 18, 65000);

Create Table Ships (
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    launched INT NOT NULL
);

INSERT INTO Ships (name, class, launched)
VALUES
("California", "Tennessee", 1915),
("Haruna", "Kongo", 1915),
("Hiei", "Kongo", 1915),
("Iowa", "Iowa", 1933),
("Kirishima", "Kongo", 1915),
("Kongo", "Kongo", 1913),
("Missouri", "Iowa", 1935),
("Musashi", "Yamato", 1942),
("New Jersey", "Iowa", 1936),
("North Carolina", "North Carolina", 1941),
("Ramillies", "Revenge", 1917),
("Renown", "Renown", 1916),
("Repulse", "Renown", 1916),
("Resolution", "Revenge", 1916),
("Revenge", "Revenge", 1916),
("Royal Oak", "Revenge", 1916),
("Royal Sovereign", "Revenge", 1916),
("Tennessee", "Tennessee", 1915),
("Washington", "North Carolina", 1941),
("Wisconsin", "Iowa", 1940),
("Yamato", "Yamato", 1941);

CREATE TABLE Battle (
    name TEXT NOT NULL,
    date TEXT NOT NULL
);

INSERT INTO Battle (name, date) 
VALUES
("Denmark Strait", "05/24/41"),
("Guadalcanal", "11/15/42"),
("North Cape", "12/26/43"),
("Surigao Strait", "10/25/44");

CREATE Table Outcomes (
    ship Text NOT NULL,
    battle TEXT NOT NULL,
    result TEXT NOT NULL
);

INSERT INTO Outcomes (ship, battle, result) 
VALUES
("California", "Surigao Strait", "ok"),
("Kirishima", "Guadalcanal", "sunk"),
("Resolution", "Denmark Strait", "ok"),
("Wisconsin", "Guadalcanal", "damaged"),
("Tennessee", "Surigao Strait", "ok"),
("Washington", "Guadalcanal", "ok"),
("New Jersey", "Surigao Strait", "ok"),
("Yamato", "Surigao Strait", "sunk"),
("Wisconsin", "Surigao Strait", "damaged");

SELECT class,country
    FROM Classes
    WHERE bore>=15;

--Find the class name and the country of the classes that carry guns of at least 15-inch bore
SELECT class, country
FROM Classes
WHERE bore >= 15


SELECT launched
    FROM Ships
    WHERE launched <=1918;

--Find the ships launched prior to 1918
SELECT name
FROM Ships
WHERE launched < 1918


SELECT ship
    FROM Outcomes
    Where (battle="Surigao Strait" AND result="sunk");
    

--Find the ships sunk in the battle of Surigao Strait
SELECT ship
FROM Outcomes
WHERE battle = "Surigao Strait"
    AND result = "sunk"


    

--List the ships with a displacement larger than 40,000 tons built after 1921
SELECT Ships.name
FROM Classes, Ships
WHERE Classes.class = Ships.class
    AND (Classes.displacement > 40000 AND Ships.launched > 1921)

--List the name, displacement, and number of guns of the ships engaged in the battle of Surigao Strait
SELECT O.ship, C.displacement, C.numGuns
FROM Classes C, Ships S, Outcomes O
WHERE O.battle = "Surigao Strait"
    AND (O.ship = S.name AND S.class = C.class)

--List the name of all the ships from the database. Ships appear in Ships, Classes, and Outcomes tables. All of them have to be printed.
SELECT C.class, S.name, O.ship
FROM Classes C, Ships S, Outcomes O

--Find the classes that have exactly two ships in the class.
SELECT class
FROM Ships
GROUP BY class
HAVING Count(*) = 2

--Find the countries that have both bb and bc ships
SELECT DISTINCT C1.country
FROM Classes C1
INNER JOIN Classes C2 ON C1.country = C2.country
WHERE C1.type = "bb" AND C2.type = "bc"

--Find the ships that survived a battle in which they were damaged and then fought in another battle.
SELECT DISTINCT O1.ship
FROM Outcomes O1
INNER JOIN Outcomes O2 ON O1.ship = O2.ship
WHERE O1.result = "damaged" 
    AND (O2.result = "sunk" 
        OR O2.result = "damaged" 
        OR O2.result = "ok")
