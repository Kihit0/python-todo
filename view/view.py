
class View:
    @staticmethod
    def view_change():
        print("===================================")
        print("Выберите из:")
        print("1 - Добавить заметку")
        print("2 - Показать заметки")
        print("3 - Показать заметку")
        print("4 - Отредактировать заметку")
        print("5 - Удалить заметки")
        print("0 - Закончить выбор")
        print("===================================")

    @staticmethod
    def view_items(items: dict):
        print("===================================")
        for item in items:
            print("{} - Заметка:".format(item["todoId"]))
            print("\tЗаголовок: {}\n\tСодержание: {}\n\tАктивна: {}".format(item["title"], item["body"], item["isActive"]))

        print("===================================\n")
