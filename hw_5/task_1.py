# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.

from collections import namedtuple

company_count = int(input('Введите количество компаний:'))
Company = namedtuple('Company', ['name', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4', 'total_profit'])
companies = []
all_companies_profit = 0

for _ in range(company_count):
    name = str(input('Введите название компании:'))
    quarter_1 = float(input('Введите прибыль за 1-й квартал:'))
    quarter_2 = float(input('Введите прибыль за 2-й квартал:'))
    quarter_3 = float(input('Введите прибыль за 3-й квартал:'))
    quarter_4 = float(input('Введите прибыль за 4-й квартал:'))
    total_profit = quarter_1 + quarter_2 + quarter_3 + quarter_4

    all_companies_profit += total_profit

    companies.append(
        Company(name, quarter_1, quarter_2, quarter_3, quarter_4, total_profit)
    )

profit_avg = all_companies_profit / company_count

companies_above_avg = []  # выше
companies_below_avg = []  # ниже

print(profit_avg)

for company in companies:
    if company.total_profit > profit_avg:
        companies_above_avg.append(company)
    elif company.total_profit < profit_avg:
        companies_below_avg.append(company)

print('Компании, чей доход выше среднего:')
for company in companies_above_avg:
    print(company.name)

print('Компании, чей доход ниже среднего:')
for company in companies_below_avg:
    print(company.name)