from src.utils import create_database, create_tables, save_data_to_database
from src.db_manager import DBManager


def user_interaction():

    dbm = DBManager()
    create_database('db_name')
    create_tables('db_name')
    save_data_to_database('db_name')

    while True:

        new = input(
            '1 - список всех компаний и кол-во вакансий у каждой компании\n'
            '2 - список всех вакансий с указанием названия компании, вакансии, зарплаты и ссылки на вакансию\n'
            '3 - средняя зарплата по вакансиям\n'
            '4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям\n'
            '5 - список вакансий, в названии которых содержится ключевое слово\n'
            'Выход - закончить\n'
        )

        if new == '1':
            print(dbm.get_companies_and_vacancies_count())
        elif new == '2':
            print(dbm.get_all_vacancies())
        elif new == '3':
            print(dbm.get_avg_salary())
        elif new == '4':
            print(dbm.get_vacancies_with_higher_salary())
        elif new == '5':
            keyword = str(input('Найти: '))
            print(dbm.get_vacancies_with_keyword(keyword))
        elif new == 'Выход':
            break


if __name__ == "__main__":
    user_interaction()

