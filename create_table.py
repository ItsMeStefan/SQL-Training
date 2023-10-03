import sqlite3

# Daten für die Tabellen erstellen
mitarbeiter_data = [
    (1, "Alice", 1, 1, 70000),
    (2, "Bob", 2, 1, 75000),
    (3, "Charlie", 3, 2, 65000),
    (4, "David", 4, 3, 80000),
    (5, "Emma", 1, 1, 72000)
]

abteilungen_data = [
    (1, "Entwicklung"),
    (2, "Design"),
    (3, "Management")
]

positionen_data = [
    (1, "Entwickler"),
    (2, "Designer"),
    (3, "Manager"),
    (4, "Projektmanager")
]

projekte_data = [
    (1, "Website-Redesign"),
    (2, "Mobile App Entwicklung"),
    (3, "Datenmigration"),
    (4, "Sicherheitsaudit")
]

mitarbeiter_projekte_data = [
    (1, 1),
    (1, 2),
    (2, 1),
    (3, 4),
    (4, 3),
    (5, 2)
]

# SQLite-Datenbank erstellen und mit ihr verbinden
db_path = 'unternehmensdatenbank.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Tabellen erstellen
cursor.execute('''
CREATE TABLE Mitarbeiter (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    PositionID INTEGER,
    AbteilungsID INTEGER,
    Gehalt REAL,
    FOREIGN KEY (PositionID) REFERENCES Positionen (ID),
    FOREIGN KEY (AbteilungsID) REFERENCES Abteilungen (ID)
)
''')

cursor.execute('''
CREATE TABLE Abteilungen (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE Positionen (
    ID INTEGER PRIMARY KEY,
    Titel TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE Projekte (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE Mitarbeiter_Projekte (
    MitarbeiterID INTEGER,
    ProjektID INTEGER,
    PRIMARY KEY (MitarbeiterID, ProjektID),
    FOREIGN KEY (MitarbeiterID) REFERENCES Mitarbeiter (ID),
    FOREIGN KEY (ProjektID) REFERENCES Projekte (ID)
)
''')

# Daten in die Tabellen einfügen
cursor.executemany('INSERT INTO Mitarbeiter VALUES (?,?,?,?,?)', mitarbeiter_data)
cursor.executemany('INSERT INTO Abteilungen VALUES (?,?)', abteilungen_data)
cursor.executemany('INSERT INTO Positionen VALUES (?,?)', positionen_data)
cursor.executemany('INSERT INTO Projekte VALUES (?,?)', projekte_data)
cursor.executemany('INSERT INTO Mitarbeiter_Projekte VALUES (?,?)', mitarbeiter_projekte_data)

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

# Pfad zur Datenbankdatei zurückgeben, damit der Benutzer sie herunterladen kann
# db_path
