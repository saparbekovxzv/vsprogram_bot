import sqlite3
from pathlib import Path

class Database:
    def __init__(self) -> None:
        db_path = Path(__file__).parent.parent / "database.sqlite"
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
         
    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS dishes")
        self.db.commit()

               
    def create_tables(self):
       self.cursor.execute(
           """ 
        CREATE TABLE IF NOT EXISTS dishes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        price INTEGER,
        picture TEXT
       )
           """
       )
       self.db.commit()
    
    def populate_tables(self):
        self.cursor.execute(
            """
        INSERT INTO dishes (name, description , price , picture) 
        VALUES ('Додстер','Горячая закуска с цыплёнком, моцареллой, томатами и соусом ранч в тонкой пшеничной лепешке','189','dodster.jpeg'),
        ('Додстер с ветчиной','Горячая закуска с ветчиной из цыпленка, томатами, моцареллой, соусом ранч в тонкой пшеничной лепешке','189','dodster with ham.jpeg'),
        ('Острый додстер','Горячая закуска с цыпленком, перцем халапеньо, солеными огурчиками, томатами, моцареллой и соусом барбекю в тонкой пшеничной лепешке','199','hot dodster.jpeg'),
        ('Дэнвич Ветчина и сыр','Поджаристая чиабатта и знакомое сочетание ветчины из цыпленка, цыпленка, моцареллы со свежими томатами и соусом ранч','199','denwich.jpeg'),
        ('Дэнвич Чоризо-Барбекю','Насыщенный вкус колбасок чоризо и пепперони с соусами бургер и барбекю, свежими томатами, маринованными огурчиками, моцареллой и луком в румяной чиабатте!','199','danwich chorizo bbq.jpeg'),
        ('Грибной Стартер','Горячая закуска с шампиньонами, моцареллой и соусом ранч в тонкой пшеничной лепешке','169','mushroom starter.jpeg')

            """
        
        )
        self.db.commit()
        
    def get_all_dishes(self):
        self.cursor.execute("SELECT * FROM  dishes")
        return self.cursor.fetchall()
        
if __name__ == "__main__":
    db = Database()
    db.drop_tables()
    db.create_tables()
    db.populate_tables()
   # print(db.get_all_dishes())
   # для распечатывания куска информации
    for dish in db.get_all_dishes():
        print("Название:",dish[1],"Описание:", dish[2])