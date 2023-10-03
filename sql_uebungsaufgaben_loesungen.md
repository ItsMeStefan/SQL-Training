
# SQL Übungsaufgaben - Lösungen

Hier sind die Lösungen für die SQL Übungsaufgaben.

### Übung 1: Grundlegende Abfragen
#### a. Liste alle Mitarbeiter und ihre Gehälter auf.
```sql
SELECT Name, Gehalt FROM Mitarbeiter;
```
#### b. Zeige alle Projektnamen an.
```sql
SELECT Name FROM Projekte;
```
#### c. Finde alle Abteilungen und wie viele Mitarbeiter in jeder Abteilung arbeiten.
```sql
SELECT a.Name, COUNT(m.ID) AS AnzahlMitarbeiter 
FROM Abteilungen a
LEFT JOIN Mitarbeiter m ON a.ID = m.AbteilungsID
GROUP BY a.ID;
```

### Übung 2: JOIN-Operationen
#### a. Zeige den Namen, die Position und die Abteilung jedes Mitarbeiters an.
```sql
SELECT m.Name, p.Titel AS Position, a.Name AS Abteilung 
FROM Mitarbeiter m
JOIN Positionen p ON m.PositionID = p.ID
JOIN Abteilungen a ON m.AbteilungsID = a.ID;
```
#### b. Liste alle Mitarbeiter und die Projekte, an denen sie arbeiten, auf.
```sql
SELECT m.Name, pr.Name AS Projekt 
FROM Mitarbeiter_Projekte mp
JOIN Mitarbeiter m ON mp.MitarbeiterID = m.ID
JOIN Projekte pr ON mp.ProjektID = pr.ID;
```

### Übung 3: Aggregationsfunktionen und Gruppierung
#### a. Berechne das durchschnittliche Gehalt in jeder Abteilung.
```sql
SELECT a.Name, AVG(m.Gehalt) AS DurchschnittlichesGehalt 
FROM Mitarbeiter m
JOIN Abteilungen a ON m.AbteilungsID = a.ID
GROUP BY a.ID;
```
#### b. Zähle, wie viele Mitarbeiter an jedem Projekt arbeiten.
```sql
SELECT p.Name, COUNT(mp.MitarbeiterID) AS AnzahlMitarbeiter 
FROM Mitarbeiter_Projekte mp
JOIN Projekte p ON mp.ProjektID = p.ID
GROUP BY p.ID;
```

### Übung 4: Unterabfragen
#### a. Finde die Mitarbeiter, die ein höheres Gehalt haben als der Durchschnitt der Gehälter aller Mitarbeiter.
```sql
SELECT Name, Gehalt 
FROM Mitarbeiter 
WHERE Gehalt > (SELECT AVG(Gehalt) FROM Mitarbeiter);
```
#### b. Zeige die Abteilung mit der höchsten Anzahl von Mitarbeitern an.
```sql
SELECT a.Name 
FROM Abteilungen a
JOIN Mitarbeiter m ON a.ID = m.AbteilungsID
GROUP BY a.ID
ORDER BY COUNT(m.ID) DESC
LIMIT 1;
```

### Übung 5: Datenmanipulation
#### a. Füge einen neuen Mitarbeiter in die Datenbank ein.
```sql
INSERT INTO Mitarbeiter (Name, PositionID, AbteilungsID, Gehalt) 
VALUES ('Neuer Mitarbeiter', 1, 1, 75000);
```
#### b. Erhöhe das Gehalt aller Mitarbeiter in der Entwicklungsabteilung um 10%.
```sql
UPDATE Mitarbeiter 
SET Gehalt = Gehalt * 1.1 
WHERE AbteilungsID = (SELECT ID FROM Abteilungen WHERE Name = 'Entwicklung');
```

### Bonus: Komplexere Abfragen
#### a. Liste die Namen der Mitarbeiter, die an mehr als einem Projekt arbeiten, und die Anzahl der Projekte, an denen sie beteiligt sind.
```sql
SELECT m.Name, COUNT(mp.ProjektID) AS AnzahlProjekte 
FROM Mitarbeiter_Projekte mp
JOIN Mitarbeiter m ON mp.MitarbeiterID = m.ID
GROUP BY m.ID
HAVING COUNT(mp.ProjektID) > 1;
```
#### b. Finde die Abteilung, die die meisten Projekte abgeschlossen hat, basierend auf der Anzahl der Mitarbeiter, die an Projekten beteiligt sind.
```sql
-- Dies ist eine fortgeschrittene Abfrage, die mehrere JOINs und Aggregationsfunktionen verwendet
SELECT a.Name, COUNT(DISTINCT mp.ProjektID) AS AnzahlProjekte 
FROM Mitarbeiter m
JOIN Abteilungen a ON m.AbteilungsID = a.ID
JOIN Mitarbeiter_Projekte mp ON m.ID = mp.MitarbeiterID
GROUP BY a.ID
ORDER BY AnzahlProjekte DESC
LIMIT 1;
```
