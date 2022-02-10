from application.salary import calculate_salary
from application.db.get_employees import get_employees
from datetime import date
from pprint import pprint


if __name__ == '__main__':
 
 pprint (f'Current date - {date.today()}')
 print('Modul MAIN')   
 calculate_salary()
 get_employees()