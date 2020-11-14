from manager.Database_Managers import DatabaseManager
from app import db

db_manager = DatabaseManager(db)

db_manager.add_item_to_Schedule(day =  "Вторник", chet = True, group_id = 1, interval_id = 1, subject_id = 1, lecturer_id = 1)


db_manager.add_group(name = 'БФИ1801')
db_manager.add_group(name = 'БИБ1702')


db_manager.add_interval(name="9:30 - 11:05")
db_manager.add_interval(name="11:15 - 12:50")
db_manager.add_interval(name="13:10 - 14:45")
db_manager.add_interval(name="15:15 - 16:45")
db_manager.add_interval(name="16:50 - 18:20")


db_manager.add_subject(name="АВС")
db_manager.add_subject(name="РКПО")
db_manager.add_subject(name="РиСПСиИТ")


db_manager.add_lecturer(first_name='Леонид', last_name='Воробейчиков', patronymic='Александрович')
db_manager.add_lecturer(first_name='Тимур', last_name='Фатхулин', patronymic='Джалиевич')
db_manager.add_lecturer(first_name='Сергей', last_name='Гуриков', patronymic='Растиславович')
db_manager.add_lecturer(first_name="Андрей", last_name="Волков",patronymic="Иванович")




