# HeadHunter's Hunter

## Описание

HeadHunter's Hunter - это приложение для поиска работодателей и размещенных ими вакансий.
Вся информация сохраняется в базу данных, чтобы в дальнейшем с ней можно было работать.

Приложение поддерживает следующие функции:
- получение списка всех компаний и количества вакансий у каждой компании;
- получение списка всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию;
- получение средней зарплаты по вакансиям;
- получение списка всех вакансий, у которых верхний край зарплатной вилки выше средней зарплаты по всем вакансиям;
- получение списка всех вакансий, в названии которых содержатся переданные в метод слова.

## Установка:

1. Клонируйте репозиторий
   ```
   git clone https://github.com/TimurAgeenko/course_project
   ```
2. Установите зависимости
   ```
   poetry install
   ```

## Использование

1. Класс HeadHunterAPIHandler используется для взаимодействия с сайтом HeadHunter
   и получения данных о работодателях и вакансиях. При инициализации объекта нужно передать путь до файла
   "employers.json", если путь не передан, то будет использоваться значение по умолчанию: "../employers.json"
   ```
   api_handler = HeadHunterAPIHandler() 
   ```
   
2. У класса HeadHunterAPIHandler есть метод get_employers_list, который используется для
   записи списка работодателей в атрибут объекта класса. При использовании нужно передать путь до файла
   "employers.json", если путь не передан, то будет использоваться значение по умолчанию: "../employers.json".
   ```
   api_handler = HeadHunterAPIHandler() # При инициализации объекта метод вызывается автоматически
   ```

3. У класса HeadHunterAPIHandler есть метод get_employers_id, который используется для получения
   идентификаторов работодателей по их названиям. Список работодателей хранится в файле employers.json.
   ```
   api_handler = HeadHunterAPIHandler()
   
   employers = api_handler.get_employers_id()
   print(employers)
   
   # Выведет
   { 
     'Яндекс': {
        'Яндекс.Еда': '9694561',
        'Яндекс Крауд': '9498112',
        'Яндекс': '1740',
        'Яндекс Команда для бизнеса': '9498120',
        'Яндекс.Доставка': '10571093',
        'Яндекс.Лавка': '12346192',
        'Яндекс.Еда Казахстан': '11187865'
     }
   }
   ```

4. У класса HeadHunterAPIHandler есть метод get_vacancies, который используется для получения
   информации о вакансиях, размещенных полученными из метода get_employers_id работодателями.
   ```
   api_handler = HeadHunterAPIHandler()
   
   vacancies = api_handler.get_vacancies({'Яндекс': '1740'})
   print(vacancies)
   
   # Выведет
   {
     "Яндекс": {
       "id": "1740",
       "vacancies": [
         {"id": "131027203"...},
         {"id": "131027204"...},
         ...
       ]
     }
   }
   ```

5. Функция config используется для парсинга параметров для подключения к базе данных из файла database.ini.
   При вызове нужно передать два аргумента: filename и section. Если их не передать, будут использоваться
   значения по умолчанию: filename="../database.ini", section="postgresql".
   ```
   params = config()
   print(params)
   
   # Выведет
   
   {
     "host"="localhost"
     "port"="5432"
     "user"="postgres"
     "password"="123"
   }
   ```
   
6. Функция save_data_to_file используется для сохранения информации в файл. При вызове нужно передать имя для файла
   без указания расширения, данные и путь по которому будет лежать файл. Если путь не передан, то по умолчанию
   будет передан следующий путь: "../data/".
   ```
   data = [
        {"employer_name": "employer_name1", "count": "count2"},
        {"employer_name": "employer_name1", "count": "count2"}
    ]

    save_data_to_file("vacancies_count", data)
   ```

7. Класс DBManager используется для взаимодействия с базой данных. При инициализации объекта нужно передать
   название для базы данных и путь к файлу database.ini, если путь не передан, то по умолчанию будет передан
   следующий путь: "../database.ini". При инициализации объекта создаются база данных и две таблицы: employers и
   vacancies, если база данных с переданным названием существует, в консоль выведется сообщение:
   "База данных с таким именем уже существует."
   ```
   db_manager = DBManager("test")
   ```
   
8. У класса DBManager есть метод is_tables_empty, который используется для проверки заполненности
   таблиц в базе данных.
   ```
   db_manager = DBManager("test")
   
   print(db_manager.is_tables_empty()) # Выведет True
   
   # Заполняем таблицы данными
   
   print(db_manager.is_tables_empty()) # Выведет False
   ```
   
9. У класса DBManager есть метод create_database, который используется для создания базы данных.
   ```
   db_manager = DBManager("test") # При инициализации метод вызывается автоматически
   
   db_manager.create_database("test") # Выведет "База данных с таким именем уже существует."
   
   db_manager.create_database("test1") # Создание новой базы данных
   ```
   
10. У класса DBManager есть метод drop_database, который используется для удаления базы данных.
   ```
   db_manager = DBManager("test")
   
   db_manager.drop_database("test")
   ```
   
11. У класса DBManager есть метод create_tables, который используется для создания двух таблиц: employers и vacancies.
    ```
    db_manager = DBManager("test") # При инициализации метод вызывается автоматически
    ```
   
12. У класса DBManager есть метод save_data_to_db, который используется для сохранения данных о работодателях
    и вакансиях в соответствующие таблицы в базе данных.
    ```
    db_manager = DBManager("test")
   
    employers = dict_got_from_api_handler
    vacancies = dict_got_from_api_handler
   
    db_manager.save_data_to_db(employers, vacancies)
    ```
   
13. У класса DBManager есть метод get_companies_and_vacancies_count, который используется
    для получения списка всех компаний и количества вакансий у каждой компании.
    ```
    db_manager = DBManager("test")
    
    data = db_manager.get_companies_and_vacancies_count()
    print(data)
    
    # Выведет
    [("company_name1", "vacancy_count1"), ("company_name2", "vacancy_count2"), ...]
    ```
    
14. У класса DBManager есть метод get_all_vacancies, который используется для получения списка всех вакансий
    с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию.
    ```
    db_manager = DBManager("test")
    
    data = db_manager.get_all_vacancies()
    print(data)
    
    # Выведет
    [("company_name1", "vacancy_name1", "salary1", "url1"), ...]
    ```
    
15. У класса DBManager есть метод get_avg_salary, который используется для получения средней зарплаты по всем вакансиям.
    ```
    db_manager = DBManager("test")
    
    average_salary = db_manager.get_avg_salary()
    print(average_salary) # Выведет число
    ```
    
16. У класса DBManager есть метод get_vacancies_with_higher_salary, используемый для получения
    списка всех вакансий, у которых верхний край зарплатной вилки выше средней зарплаты по всем вакансиям.
    ```
    db_manager = DBManager("test")
    
    data = db_manager.get_vacancies_with_higher_salary()
    print(data)
    
    # Выведет
    [("vacancy_id1", "vacancy_name1", "department1", "employer_name1", ...), ...]
    ```
    
17. У класса DBManager есть метод get_vacancies_with_keyword, используемый для получения списка всех вакансий,
    в названии которых содержатся переданные в метод слова.
    ```
    db_manager = DBManager("test")
    
    data = db_manager.get_vacancies_with_keyword("keywords")
    print(data)
    
    # Выведет
    [("vacancy_id1", "vacancy_name1", "department1", "employer_name1", ...), ...]
    ```

## Тестирование

Для запуска тестов выполните следующие шаги:

1. Убедитесь, что у вас установлен `pytest`
2. В терминале наберите `pytest`, чтобы запустить тестирование
3. Проверьте результаты в консоли

При тестировании используются юнит-тесты, их результаты выводятся в консоль.

Подробные отчеты о тестировании можно найти в директории `/htmlcov/`