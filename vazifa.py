import sqlite3 as sql
boglanish = sql.connect("sevara.db")

malumot = boglanish.cursor()
malumot.execute("""
CREATE TABLE IF NOT EXISTS Flower(
    turi TEXT,
    rangi TEXT

) 
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Animal(
    turi TEXT,
    laqabi TEXT

)
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Fruit(
    turi TEXT,
    tami TEXT
)
""")

malumot.execute("""
CREATE TABLE IF NOT EXISTS Windows(
    nomi TEXT,
    narxi INTEGER
)
""")
