groupmates = [
 {
 "name": u"Василий",
 "group": "912-2",
 "age": 19,
 "marks": [4, 3, 5, 5, 4]
 },
 {
 "name": u"Анна",
 "group": "912-1",
 "age": 18,
 "marks": [3, 2, 3, 4, 3]
 },
 {
 "name": u"Георгий",
 "group": "912-2",
 "age": 19,
 "marks": [3, 5, 4, 3, 5]
 },
 {
 "name": u"Валентина",
 "group": "912-1",
 "age": 18,
 "marks": [5, 5, 5, 4, 5]
 }
]
def print_studs(students):
    #Вывод списка с данными всех внесенных студентов
    t = '{:<16}{:<8}{:<8}{}'
    print(t.format('Имя студента', 'Группа', 'Возраст', 'Оценки'))
    print('\n'.join([t.format(s['name'], s['group'], s['age'], s['marks']) for s in students]))
def all_students(students):
    #Возвращаем список всх внесенных студентов
    #Вызываем print_studs(groupmates) 
    return students
def students_avg(students, n):
    #Возвращаем студентов со средней оценкой выше n
    return [s for s in students if sum(s['marks'])/len(s['marks']) > n]
print_studs(all_students(groupmates))
print()
print_studs(students_avg(groupmates, 4))
