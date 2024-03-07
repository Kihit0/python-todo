import os
from datetime import datetime
from json import load, dump


class Todo:
    _payload: dict = {
        "title": str,
        "body": str,
        "isActive": bool
    }

    def __init__(self):
        self._data = []
        self._scr = os.path.abspath("./db/db.json")
        self.load()

    def load(self):
        try:
            with open(self._scr) as fh:
                self._data = load(fh)
        except FileNotFoundError:
            self._data = {}

    def save(self):
        with open(self._scr, "w") as fh:
            dump(self._data, fh)

    def search_user(self, user_id: int):
        for user in self._data:
            if user["userId"] == user_id:
                return user

        return None

    # Get request many
    def getTodos(self, user_id: int):
        user = self.search_user(user_id)

        if user is not None:
            return user["todo"]

        return None

    # Get request one
    def getTodo(self, user_id: int, todo_id: int):

        user = self.search_user(user_id)

        if user is not None:
            for todo in user["todo"]:
                if todo["todoId"] == todo_id:
                    return todo

        return None

    # Post request
    def create_todo(self, payload: _payload, user_id: int):
        user = self.search_user(user_id)

        if user is not None:
            todo_id = len(user["todo"])
            user["todo"].append({"todoId": todo_id + 1, "create": "{}".format(datetime.now())} | payload)
            self.save()
        else:
            print("Error: Нет такого пользователя")

    # Put request
    def update_todo(self, user_id: int, todo_id: int, payload: dict):
        user = self.search_user(user_id)

        if user is not None:
            for todo in user["todo"]:
                if todo["todoId"] == todo_id:
                    for key in todo.keys():
                        if payload.get(key) is not None:
                            todo[key] = payload[key]
                            self.save()

    # Remove request
    def remove_todo(self, user_id: int, todo_id: int):
        user = self.search_user(user_id)

        if user is not None:
            for todo in user["todo"]:
                if todo["todoId"] == todo_id:
                    user["todo"].remove(todo)
                    self.save()
                    break
        else:
            print("Error: Нет такого пользователя")

