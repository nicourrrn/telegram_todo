class Todo:
    last_id = 0

    def __init__(self, title: str, description: str = "", completed: bool = False):
        self.id = Todo.last_id
        self.title = title
        self.description = description
        self.completed = completed

        Todo.last_id += 1

    def __eq__(self, other):
        return self.title == other.title and self.description == other.description

    def __str__(self) -> str:
        return f"{self.title} - {self.completed}"

    def __repr__(self) -> str:
        return f"Todo({self.id}, {self.title}, {self.completed})"


class User:
    def __init__(self, identificator: str, name: str):
        self.identificator = identificator
        self.name = name
        self.todos: list[Todo] = []

    def add_task(self, todo: Todo):
        self.todos.append(todo)

    def done_task(self, id: int):
        for todo in self.todos:
            if todo.id == id:
                todo.completed = True
                return

    def __eq__(self, other):
        return self.identificator == other.identificator

    def __str__(self) -> str:
        return f"{self.identificator} - {self.name}"

    def __repr__(self) -> str:
        return f"User({self.identificator}, {self.name})"


class Admin(User):
    def __init__(self, identificator: str, name: str):
        super().__init__(identificator, name)

    def give_task(self, user: User, todo: Todo):
        user.todos.append(todo)

    def done_user_task(self, user: User, id: int):
        user.done_task(id)
