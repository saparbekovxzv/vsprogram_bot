--Создание таблицы для меню
CREATE TABLE IF NOT EXISTS dishes(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       description TEXT,
       price INTEGER,
       picture TEXT

)
--Заполнение таблицы
INSERT INTO dishes (name, description , price , picture)
VALUES('Додстер','Горячая закуска с цыплёнком, моцареллой, томатами и соусом ранч в тонкой пшеничной лепешке','189','dodster.jpeg'),
VALUES('Додстер с ветчиной','Горячая закуска с ветчиной из цыпленка, томатами, моцареллой, соусом ранч в тонкой пшеничной лепешке','189','dodster with ham.jpeg'),
VALUES('Острый додстер','Горячая закуска с цыпленком, перцем халапеньо, солеными огурчиками, томатами, моцареллой и соусом барбекю в тонкой пшеничной лепешке','199','hot dodster.jpeg'),
VALUES('Дэнвич Ветчина и сыр','Поджаристая чиабатта и знакомое сочетание ветчины из цыпленка, цыпленка, моцареллы со свежими томатами и соусом ранч','199','denwich.jpeg'),
VALUES('Дэнвич Чоризо-Барбекю','Насыщенный вкус колбасок чоризо и пепперони с соусами бургер и барбекю, свежими томатами, маринованными огурчиками, моцареллой и луком в румяной чиабатте!','199','danwich chorizo bbq.jpeg'),
VALUES('Грибной Стартер','Горячая закуска с шампиньонами, моцареллой и соусом ранч в тонкой пшеничной лепешке','169','mushroom starter.jpeg')
--Получение запроса всего меню
SELECT *  FROM dishes
--Получение одного блюда
SELECT * FROM  dishes  WHERE id= 2
--Получение блюд по категории 
SELECT * FROM  dishes  WHERRE  category_id = 3
--Получение блюд по названию категории 
SELECT d.name, d.price,  dc.name FROM dishes AS d
    JOIN dish_categories AS dc ON d.category_id=dc.id
    WHERE dc.name ='Закуски'