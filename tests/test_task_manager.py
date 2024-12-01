import os
import json
import pytest
from task_manager_class import TaskManager


@pytest.fixture
def manager():
    manager = TaskManager('data/test_tasks.json')
    yield manager
    os.remove('data/test_tasks.json')


def test_add_task(manager):
    manager.add_task("Test Task", "Test Description",
                     "Test Category", "2024-11-30", "Высокий")
    tasks = manager.view_tasks()
    assert len(tasks) == 1
    assert tasks[0]['title'] == "Test Task"


def test_edit_task(manager):
    manager.add_task("Test Task", "Test Description",
                     "Test Category", "2024-11-30", "Высокий")
    task_id = manager.view_tasks()[0]['id']
    manager.edit_task(task_id, title="Updated Task")
    tasks = manager.view_tasks()
    assert tasks[0]['title'] == "Updated Task"


def test_delete_task(manager):
    manager.add_task("Test Task", "Test Description",
                     "Test Category", "2024-11-30", "Высокий")
    task_id = manager.view_tasks()[0]['id']
    manager.delete_task(task_id)
    tasks = manager.view_tasks()
    assert len(tasks) == 0


def test_search_tasks(manager):
    manager.add_task("Test Task", "Test Description",
                     "Test Category", "2024-11-30", "Высокий")
    tasks = manager.search_tasks(keyword="Test")
    assert len(tasks) == 1


def test_invalid_add_task(manager):
    with pytest.raises(ValueError):
        manager.add_task("", "Test Description",
                         "Test Category", "2024-11-30", "Высокий")


def test_invalid_edit_task(manager):
    with pytest.raises(ValueError):
        manager.edit_task("invalid-uuid", title="Updated Task")


def test_invalid_delete_task(manager):
    with pytest.raises(ValueError):
        manager.delete_task("invalid-uuid")
