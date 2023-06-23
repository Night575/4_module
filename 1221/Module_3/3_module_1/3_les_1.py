name = "Давид"
salary = 200
age = 15

print("У " + name + " зарплата составляет " + str(salary) + " рублей.")
print(f"У {name} зарплата составляет {salary} рублей.")
print("У {employee_name} зарплата составляет {employee_salary} рублей.".format(
    employee_name=name, employee_salary=salary
))

employee = {
    'name': 'Вадим',
    'salary': 199,
    'age': 16,
}

print(f"У {employee['name']} зарплата составляет {employee['salary']} рублей.")

employees_list = [
    {
        'name': 'Вадим',
        'salary': 199
    },
    {
        'name': 'Сева',
        'salary': 200_000,
    },
    {
        'name': 'Nikiton',
        'salary': 1,
    }
]

for employee in employees_list:
    print(f'У {employee["name"]} зарплата составляет {employee["salary"]}.')


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_hi(self):
        print('Hi')


employee = Employee(name='Я не знаю кто я', salary=120)
print(f"У {employee.name} зарплата составляет {employee.salary} биткоинов.")
