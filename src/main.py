from src.api import HeadHunterAPIHandler
from src.db_manager import DBManager
from src.utils import save_data_to_file


def main():
    """Главная функция для взаимодействия с пользователем."""
    api_handler = HeadHunterAPIHandler()

    print("Добро пожаловать в приложение для анализа информации по вакансиям!")

    username_input = input("\nДля начала введите название для базы данных, где будет хранится вся информация: ")

    db_manager = DBManager(username_input)

    print("\nОтлично! Теперь выберете один из двух пунктов:\n")

    while True:
        print("1. Получить информацию о вакансиях, размещенных указанными в файле работодателями.")
        print("2. Работать с уже имеющейся в базе данных информацией.")

        main_input = input("\nВведите цифру нужного пункта: ")

        if main_input == "1":
            employers = api_handler.get_employers_id()
            selected_employers = {}

            for key, value in employers.items():
                i = 1
                employers_dict = {}
                print(f"\nДля указанной компании {key} найдены следующие работодатели:\n")

                for k in value.keys():
                    employers_dict[str(i)] = k

                    print(f"{i}. {k}")
                    i += 1

                while True:
                    print("\nВведите через запятую цифры нужных вам работодателей(например: 1, 2, 3):")
                    user_input = input()
                    employers_list = user_input.split(", ")

                    can_continue = True
                    for item in employers_list:
                        if not item.isdigit():
                            print("\nОшибка. Либо вы ввели не цифры, либо введенные цифры не соответствуют примеру.")
                            can_continue = False
                        elif int(item) > len(employers_dict) or int(item) < 1:
                            print("\nОшибка. Вы ввели цифру, которой не было в показанном списке работодателей.")
                            can_continue = False

                    if not can_continue:
                        continue
                    else:
                        digits = user_input.split(", ")
                        for digit in digits:
                            employer = employers_dict[digit]
                            selected_employers[employer] = value[employer]
                        break

            vacancies = api_handler.get_vacancies(selected_employers)

            db_manager.save_data_to_db(selected_employers, vacancies)

            print("\nОтлично! Данные успешно получены и записаны в базу данных.")
            break

        elif main_input == "2":
            if db_manager.is_tables_empty():
                print("\nВ базе данных нет информации, с которой можно работать.\n")
            else:
                break

    while True:
        print("\nВыберите, что вы хотите сделать:\n")

        print("1. Получить список всех компаний и количество вакансий у каждой компании.")
        print("2. Получить список всех вакансий.")
        print("3. Получить среднюю зарплату по всем вакансиям.")
        print("4. Получить список всех вакансий, у которых верхний край зарплатной вилки выше средней зарплаты.")
        print("5. Получить список всех вакансий, в названии которых содержатся определенные слова.")
        print("6. Выход.")

        user_input = input("\nВведите цифру нужного пункта: ")

        if user_input == "1":
            print("\nДанные будут записаны в файл в папку 'data', которая находится в корне проекта.")
            print("Если у вас нет такой папки, она будет создана.")
            print("Внимание! Если файл уже существует, данные перезапишутся.")

            filename = input("\nУкажите название для файла без указания расширения: ")

            data = db_manager.get_companies_and_vacancies_count()

            save_data_to_file(filename, data)

            print("\nДанные успешно получены и сохранены.")

        elif user_input == "2":
            print("\nДанные будут записаны в файл в папку 'data', которая находится в корне проекта.")
            print("Если у вас нет такой папки, она будет создана.")
            print("Внимание! Если файл уже существует, данные перезапишутся.")

            filename = input("\nУкажите название для файла без указания расширения: ")

            data = db_manager.get_all_vacancies()

            save_data_to_file(filename, data)

            print("\nДанные успешно получены и сохранены.")

        elif user_input == "3":
            average_salary = db_manager.get_avg_salary()

            print(f"\nСредняя зарплата по всем вакансиям равна {average_salary} руб.")

        elif user_input == "4":
            print("\nДанные будут записаны в файл в папку 'data', которая находится в корне проекта.")
            print("Если у вас нет такой папки, она будет создана.")
            print("Внимание! Если файл уже существует, данные перезапишутся.")

            filename = input("\nУкажите название для файла без указания расширения: ")

            data = db_manager.get_vacancies_with_higher_salary()

            save_data_to_file(filename, data)

            print("\nДанные успешно получены и сохранены.")

        elif user_input == "5":
            while True:
                print("\nВведите через запятую слова для поиска(например: Менеджер, по, продажам): ")
                inner_input = input()
                keywords = inner_input.split(", ")

                can_continue = True
                for item in keywords:
                    if not item.isalpha():
                        print("\nОшибка. Либо вы ввели не слова, либо введенные слова не соответствуют примеру.")
                        can_continue = False

                if not can_continue:
                    continue
                else:
                    break

            print("\nДанные будут записаны в файл в папку 'data', которая находится в корне проекта.")
            print("Если у вас нет такой папки, она будет создана.")
            print("Внимание! Если файл уже существует, данные перезапишутся.")

            filename = input("\nУкажите название для файла без указания расширения: ")

            data = db_manager.get_vacancies_with_keyword(keywords)

            save_data_to_file(filename, data)

            print("\nДанные успешно получены и сохранены.")

        elif user_input == "6":
            print("Завершение работы программы.")
            break

        else:
            print("\nТакого пункта нет в указанном меню.")
