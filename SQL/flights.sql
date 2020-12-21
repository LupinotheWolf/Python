CREATE TABLE flights (
  id INTEGER PRIMARY KEY,
  origin TEXT NOT NULL,
  destination TEXT NOT NULL,
  duration INTEGER NOT NULL
);

INSERT INTO flights
  (origin, destination, duration)
  VALUES
  ("New York", "London", 415),
  ("Paris", "Milano", 350);

CREATE TABLE test (
  id INTEGER PRIMARY KEY,
  test TEXT NOT NULL
);

INSERT INTO test
  (test)
  VALUES
  ("Test");
