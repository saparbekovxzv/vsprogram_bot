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
        CREATE TABLE IF NOT EXISTS dish_categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        )
           """
       
       )
       self.cursor.execute(
           """ 
        CREATE TABLE IF NOT EXISTS dishes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        price INTEGER,
        picture TEXT,
        category_id INTEGER,
        FOREIGN KEY(category_id)REFERENCES dish_categories(id)
       )
           """
       )
       self.cursor.execute(
           """
           CREATE TABLE IF NOT EXISTS survey(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT,
           phone_number TEXT
           )
           """
       )
       self.db.commit()
    
    def populate_tables(self):
        self.cursor.execute(
            """
        INSERT INTO dish_categories (name)
        VALUES('Пицца 25 см'),('Пицца 30 см'),('Пицца 35 см'),
               ('Закуски'),('Кофе'),('Коктейли'),('Напитки'),
              ('Десерты'),('Соусы'),('Другие товары'),('Комбо')
            """
        ) 
    
        self.cursor.execute(
            """
        INSERT INTO dishes (name, description , price , picture, category_id) 
        VALUES ('Додстер','Горячая закуска с цыплёнком, моцареллой, томатами и соусом ранч в тонкой пшеничной лепешке','189','dodster.jpeg',4),
        ('Додстер с ветчиной','Горячая закуска с ветчиной из цыпленка, томатами, моцареллой, соусом ранч в тонкой пшеничной лепешке','189','dodster with ham.jpeg',4),
        ('Острый додстер','Горячая закуска с цыпленком, перцем халапеньо, солеными огурчиками, томатами, моцареллой и соусом барбекю в тонкой пшеничной лепешке','199','hot dodster.jpeg',4),
        ('Дэнвич Ветчина и сыр','Поджаристая чиабатта и знакомое сочетание ветчины из цыпленка, цыпленка, моцареллы со свежими томатами и соусом ранч','199','denwich.jpeg',4),
        ('Дэнвич Чоризо-Барбекю','Насыщенный вкус колбасок чоризо и пепперони с соусами бургер и барбекю, свежими томатами, маринованными огурчиками, моцареллой и луком в румяной чиабатте!','199','danwich chorizo bbq.jpeg',4),
        ('Грибной Стартер','Горячая закуска с шампиньонами, моцареллой и соусом ранч в тонкой пшеничной лепешке','169','mushroom starter.jpeg',4)
            """       
            
        )
        self.db.commit()
        
#запрос на получение всех блюд
    def get_all_dishes(self):
        self.cursor.execute("SELECT * FROM  dishes")
        return self.cursor.fetchall()
#запрос  на получение  одного блюда
   # def get_one_dishes(self, id: int):
   #     self.cursor.execute("SELECT * FROM  dishes WHERE  id=?",(id,))

#запрос на получение блюд по категории 
    def get_dishes_by_category(self, category_id: int):
        self.cursor.execute("SELECT * FROM dishes WHERE category_id  =   :categoryId",{"categoryId" : category_id},)
        return self.cursor.fetchall()
    
#запрос на получение блюд по названию категории
    def get_dishes_by_cat_name(self, cat_name: str):
        self.cursor.execute(
            """
        SELECT d.* , dc.name FROM dishes AS d
        JOIN dish_categories AS dc ON d.category_id = dc.id
        WHERE dc.name = :catName
            """,
            {"catName": cat_name},
        )
        return self.cursor.fetchall()
# bd
    def insert_survey(self, data: dict):
        self.cursor.execute(
            """
        INSERT INTO survey (name, phone_number)
        VALUES (:name, :phone_number)
            """, data,
        )
        self.db.commit()
    
    
    

if __name__ == "__main__":
    db = Database()
    db.drop_tables()
    db.create_tables()
    db.populate_tables()
   #принты запросов  
   # print(db.get_all_dishes()) #поиск всех блюд
   # print(db.get_dishes_by_category(4)) # поиск по категории 
    print(db.get_dishes_by_cat_name("Закуски"))
   
   # для распечатывания куска информации
   # for dish in db.get_all_dishes():
        
   # print("Название:",dish[1],"Описание:", dish[2])
   # print(db.get_one_dishes("2; DROP TABLE  dishes;"))