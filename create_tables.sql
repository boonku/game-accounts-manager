CREATE TABLE IF NOT EXISTS Games (
    GameId INTEGER PRIMARY KEY AUTOINCREMENT,
    GameName VARCHAR(100) NOT NULL UNIQUE
);
DROP TABLE IF EXISTS Platforms;
CREATE TABLE IF NOT EXISTS Platforms (
    PlatformId INTEGER PRIMARY KEY AUTOINCREMENT,
    platformName VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS Accounts (
    AccountId INTEGER PRIMARY KEY AUTOINCREMENT,
    Login VARCHAR(50) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Game INTEGER NOT NULL,
    Platform INTEGER NOT NULL,
    AdditionalInformation TEXT,
    AddedDate DATE,
    FOREIGN KEY(Game) REFERENCES Games(GameId),
    FOREIGN KEY(Platform) REFERENCES Platforms(PlatformId)
);
INSERT INTO Platforms (platformName)
VALUES
    ("Steam"),
    ("Origin"),
    ("UPLAY"),
    ("Epic Games Store"),
    ("GOG Galaxy"),
    ("Microsoft Store"),
    ("Other");
