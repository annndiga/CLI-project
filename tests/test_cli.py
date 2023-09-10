import unittest
from click.testing import CliRunner
from .lib.cli import add_user, add_task

class TestAddUser(unittest.TestCase):
    def test_add_user(self):
        runner = CliRunner()
        result = runner.invoke(add_user)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), "User added successfully!")

class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        runner = CliRunner()
        result = runner.invoke(add_task)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), "Task added successfully!")

if __name__ == '__main__':
    unittest.main()
