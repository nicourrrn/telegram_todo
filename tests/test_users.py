import unittest

from lib.controls import load_users, save_users
from lib.models import Todo, User


class TestUsers(unittest.TestCase):
    def test_user(self):
        users = [User("user1", "password1"), User("user2", "password2")]

        save_users(users)
        loaded_users = load_users()

        self.assertEqual(users, loaded_users)

    def test_todos(self):
        users = [User("123123", "Vadym")]
        users[0].todos = [Todo("Buy milk", "Buy milk in the store")]

        save_users(users)
        loaded_users = load_users()

        self.assertEqual(users, loaded_users)


if __name__ == "__main__":
    unittest.main()
