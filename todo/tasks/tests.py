from django.test import TestCase

from .models import *
# Create your tests here.


class TaskTests(TestCase):
    def test_create_task(self):
        """updates the task if the task is not marked as completed"""
        # task = Task(title="a task is here")
        # self.assertIs(task.completed, False)

        task = Task(title="a task")
        self.assertIs(task.completed, False)