import csv
from collections import defaultdict

# Класс единичной записи о работе комбайна
class HarvesterRecord:
    def __init__(self, number, date, area, driver):
        self.number = number
        self.date = date
        self.area = area
        self.driver = driver

    def __repr__(self):
        return f"HarvesterRecord({self.number}, {self.date}, {self.area:.2f}, {self.driver})"

    def __setattr__(self, name, value):
        if name == "area" and value <= 0:
            raise ValueError("Площадь должна быть положительной")
        super().__setattr__(name, value)

# Базовый класс коллекции
class BaseCollection:
    def __init__(self, items=None):
        self.items = items or []

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

# Коллекция записей о работе комбайна
class HarvesterRecords(BaseCollection):
    @staticmethod
    def validate_area(area):
        return area > 0

    def add_record(self, number, date, area, driver):
        if not self.validate_area(area):
            raise ValueError("Площадь должна быть положительной")
        self.items.append(HarvesterRecord(number, date, area, driver))

    def iterate_areas(self):
        for record in self.items:
            yield record.area

# Пример использования
if __name__ == "__main__":
    # Создание коллекции записей
    records = HarvesterRecords()

    # Интерактивный ввод данных пользователем
    while True:
        answer = input("Хотите добавить новую запись? (yes/no): ").lower()
        if answer != "yes":
            break
        
        number = int(input("Введите номер записи: "))
        date = input("Введите дату (в формате YYYY-MM-DD): ")
        area = float(input("Введите площадь (га): "))
        driver = input("Введите ФИО водителя: ")
        
        try:
            records.add_record(number, date, area, driver)
            print("Запись успешно добавлена!\n")
        except ValueError as e:
            print(f"Ошибка: {e}\n")

    # Проход по записям
    print("\nВсе записи:")
    for record in records:
        print(record)

    # Доступ по индексу
    first_record = records[0]
    print(f"\nПервая запись: {first_record}")

    # Генератор площадей
    areas = list(records.iterate_areas())
    print(f"\nПлощади: {areas}")
