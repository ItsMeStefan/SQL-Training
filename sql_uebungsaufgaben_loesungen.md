
# SQL Übungsaufgaben - Lösungen

Hier sind die Lösungen für die SQL Übungsaufgaben mit ausklappbaren Lösungen.

### Übung 1: Grundlegende Abfragen

<details>
<summary>a. Liste alle Mitarbeiter und ihre Gehälter auf.</summary>

```sql
SELECT Name, Gehalt FROM Mitarbeiter;
```
</details>

<details>
<summary>b. Zeige alle Projektnamen an.</summary>

```sql
SELECT Name FROM Projekte;
```
</details>

<details>
<summary>c. Finde alle Abteilungen und wie viele Mitarbeiter in jeder Abteilung arbeiten.</summary>

```sql
SELECT a.Name, COUNT(m.ID) AS AnzahlMitarbeiter 
FROM Abteilungen a
LEFT JOIN Mitarbeiter m ON a.ID = m.AbteilungsID
GROUP BY a.ID;
```
</details>

### Übung 2: JOIN-Operationen

<details>
<summary>a. Zeige den Namen, die Position und die Abteilung jedes Mitarbeiters an.</summary>

```sql
SELECT m.Name, p.Titel AS Position, a.Name AS Abteilung 
FROM Mitarbeiter m
JOIN Positionen p ON m.PositionID = p.ID
JOIN Abteilungen a ON m.AbteilungsID = a.ID;
```
</details>

<details>
<summary>b. Liste alle Mitarbeiter und die Projekte, an denen sie arbeiten, auf.</summary>

```sql
SELECT m.Name, pr.Name AS Projekt 
FROM Mitarbeiter_Projekte mp
JOIN Mitarbeiter m ON mp.MitarbeiterID = m.ID
JOIN Projekte pr ON mp.ProjektID = pr.ID;
```
</details>

### Übung 3: Aggregationsfunktionen und Gruppierung

<details>
<summary>a. Berechne das durchschnittliche Gehalt in jeder Abteilung.</summary>

```sql
SELECT a.Name, AVG(m.Gehalt) AS DurchschnittlichesGehalt 
FROM Mitarbeiter m
JOIN Abteilungen a ON m.AbteilungsID = a.ID
GROUP BY a.ID;
```
</details>

<details>
<summary>b. Zähle, wie viele Mitarbeiter an jedem Projekt arbeiten.</summary>

```sql
SELECT p.Name, COUNT(mp.MitarbeiterID) AS AnzahlMitarbeiter 
FROM Mitarbeiter_Projekte mp
JOIN Projekte p ON mp.ProjektID = p.ID
GROUP BY p.ID;
```
</details>

### Übung 4: Unterabfragen

<details>
<summary>a. Finde die Mitarbeiter, die ein höheres Gehalt haben als der Durchschnitt der Gehälter aller Mitarbeiter.</summary>

```sql
SELECT Name, Gehalt 
FROM Mitarbeiter 
WHERE Gehalt > (SELECT AVG(Gehalt) FROM Mitarbeiter);
```
</details>

<details>
<summary>b. Zeige die Abteilung mit der höchsten Anzahl von Mitarbeitern an.</summary>

```sql
SELECT a.Name 
FROM Abteilungen a
JOIN Mitarbeiter m ON a.ID = m.AbteilungsID
GROUP BY a.ID
ORDER BY COUNT(m.ID) DESC
LIMIT 1;
```
</details>

### Übung 5: Datenmanipulation

<details>
<summary>a. Füge einen neuen Mitarbeiter in die Datenbank ein.</summary>

```sql
INSERT INTO Mitarbeiter (Name, PositionID, AbteilungsID, Gehalt) 
VALUES ('Neuer Mitarbeiter', 1, 1, 75000);
```
</details>

<details>
<summary>b. Erhöhe das Gehalt aller Mitarbeiter in der Entwicklungsabteilung um 10%.</summary>

```sql
UPDATE Mitarbeiter 
SET Gehalt = Gehalt * 1.1 
WHERE AbteilungsID = (SELECT ID FROM Abteilungen WHERE Name = 'Entwicklung');
```
</details>

### Bonus: Komplexere Abfragen

<details>
<summary>a. Liste die Namen der Mitarbeiter, die an mehr als einem Projekt arbeiten, und die Anzahl der Projekte, an denen sie beteiligt sind.</summary>

```sql
SELECT m.Name, COUNT(mp.ProjektID) AS AnzahlProjekte 
FROM Mitarbeiter_Projekte mp
JOIN Mitarbeiter m ON mp.MitarbeiterID = m.ID
GROUP BY m.ID
HAVING COUNT(mp.ProjektID) > 1;
```
</details>

<details>
<summary>b. Finde die Abteilung, die die meisten Projekte abgeschlossen hat, basierend auf der Anzahl der Mitarbeiter, die an Projekten beteiligt sind.</summary>

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
</details>
