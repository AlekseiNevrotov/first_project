"Разработчик Elazar"

import datetime as dt
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'



def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    expiration_date = dt.datetime.strptime(expiration_date, DATE_FORMAT).date() if expiration_date else expiration_date       
    
    list.append(items[title], {'amount': amount, 'expiration_date': expiration_date })    
    
goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': dt.date(2024, 5, 11)},
        {'amount': Decimal('2'), 'expiration_date': dt.date(2024, 5, 12)}
    ],
    'Вода': [{'amount': Decimal('1.5'), 'expiration_date': None}]
}     

add(goods, 'Апельсины', Decimal('3'), '2024-5-13')
add(goods, 'Киви', Decimal('22'), '2024-5-11')
add(goods, 'Апельсины', Decimal('9'), '2024-5-14')

def add_by_note(items, note):
    for line in str.split(note, '\n'):
        parts = str.split(line, ' ')
        
        if len(str.split(parts[-1], '-')) == 3:
            expiration_date = parts[-1]
            title = ' '.join(parts[:-2])
            good_amount = Decimal((parts[-2]))
        else:
            title = ' '.join(parts[:1])
            good_amount = Decimal((parts[1]))
            expiration_date = None           
            
        add(items, title, Decimal(good_amount), expiration_date=expiration_date)

add_by_note(goods, 'Мясо 4 2024-05-13')
add_by_note(goods, 'Рыба 88')

def find(items, needle):
    search = []
    for k in items.keys():
        if len(needle) > 1:
            stroka = str.lower(k)
            x = stroka.find(str.lower(needle), 0, len(k))
            if x != -1:
                search.append(k)
        else:
            break
    return search            
           
def amount(items, needle):
    search = []
    amount = Decimal('0')
    for k in items.keys():
        if len(needle) > 1:
            stroka = str.lower(k)
            x = stroka.find(str.lower(needle), 0, len(k))
            if x != -1:
                for d in items[k]:
                    amount += d['amount']
        else:
            break
    return amount

def expire(items, in_advance_days=0):
    now = dt.date.today()
    exp_items = []
    sum_of_quantity = Decimal(0)
    
def expire(items, in_advance_days=0):
    days_remane = dt.timedelta(days = in_advance_days + 1)
    find_products = []
    if in_advance_days > 0:
        for keys in items.keys():
            sum_by_same_product = Decimal(0.0)
            for i in range(0, len(items[keys])):
                if items[keys][i]['expiration_date'] is not None:
                    difference_days = items[keys][i]['expiration_date'] - dt.datetime.now().date()
                    if days_remane > difference_days:
                        sum_by_same_product += items[keys][i]['amount']
            if sum_by_same_product > 0:
                find_products.append((keys, sum_by_same_product))
    else:
        for keys in items.keys():
            sum_by_same_product = Decimal(0.0)
            for i in range(0, len(items[keys])):
                if items[keys][i]['expiration_date'] is not None:
                    if items[keys][i]['expiration_date'] <= dt.datetime.now().date():
                        sum_by_same_product += items[keys][i]['amount']
            if sum_by_same_product > 0:
                find_products.append((keys, sum_by_same_product))
    return find_products   

print(goods)
print(find(goods, 'ль'))
print(amount(goods, 'Апельсины'))
print(expire(goods))
