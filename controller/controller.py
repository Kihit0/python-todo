from service.todo import Todo
from view.view import View


class Controller:
    def __init__(self):
        self.todo = Todo()
        self.view = View()

    @staticmethod
    def input_data():
        print("===================================")
        print("Введите заметку")
        print("Заголовок: ", end="")
        title = input()
        print("Содержание: ", end="")
        body = input()
        print("Активна (Да/нет): ", end="")
        isActive = input()

        while True:
            if isActive.lower().replace(" ", "") == "да":
                isActive = True
                break
            elif isActive.lower().replace(" ", "") == "нет":
                isActive = False
                break
            else:
                print("Вы ввели неправильный вариант")
                print("Активна (Да/нет): ", end="")
                isActive = input()

        return [title, body, isActive]

    @staticmethod
    def validate_data(data):
        for item in data:
            if not item:
                return False

        return True

    def print_item(self):
        items = self.todo.getTodos(1)
        if items is None:
            print("Нет записей")

        else:
            self.view.view_items(items)

    def get_data(self):
        data = self.input_data()

        if not self.validate_data(data):
            print("===================================")
            print("Вы ввели пустые строчки")
            while True:
                data = self.input_data()
                if self.validate_data(data):
                    break

        return data

    def run(self):
        isRun = True
        while isRun:
            self.view.view_change()
            print("Введите ваш выбор: ", end="")
            change = int(input())

            match change:
                case 1:
                    data = self.get_data()
                    print(data)

                    self.todo.create_todo(user_id=1, payload={
                        "title": data[0],
                        "body": data[1],
                        "isActive": data[2]
                    })
                    print("Заметка создана")
                case 2:
                    self.print_item()
                case 3:
                    self.print_item()
                    print("Введите номер заметки: ", end="")
                    todo_id = int(input())
                    todo = self.todo.getTodo(user_id=1, todo_id=todo_id)
                    self.view.view_items([todo])
                case 4:
                    self.print_item()
                    print("Выберите номер заметки, которую хотите отредактировать: ", end="")
                    todo_id = int(input())
                    data = self.get_data()
                    self.todo.update_todo(user_id=1, todo_id=todo_id, payload={
                        "title": data[0],
                        "body": data[1],
                        "isActive": data[2]
                    })
                    print("Заметка обновлена")
                case 5:
                    self.print_item()
                    print("Выберите номер заметки, которую хотите удалить: ", end="")
                    todo_id = int(input())
                    self.todo.remove_todo(user_id=1, todo_id=todo_id)
                    print("Заметка удалена")
                case 0:
                    isRun = False
                case _:
                    print("Такого варианта нет")



