from re import match
from datetime import date
import pytest
from task_manager import Priority, Task, TaskManager, TaskNotFoundError, search_tasks, sort_tasks

@pytest.fixture
def tm() -> TaskManager:
    return TaskManager()

def test_add_task_assigns_incrementing_ids(tm: TaskManager) -> None:
    t1 = tm.add_task("a")
    t2 = tm.add_task("b")
    assert (t1.id, t2.id) == (1,2)

def test_new_task_has_defaults(tm: TaskManager) -> None:
    t = tm.add_task("x")
    assert t.done is False
    assert t.priority is Priority.MEDIUM
    assert t.tags == []

def test_tags_list_is_not_shared(tm: TaskManager) -> None:
    # default_factory=list işe yarıyor mu? Kodundaki yorumu test ediyoruz.
    t1, t2 = tm.add_task("a"), tm.add_task("b")
    t1.tags.append("Is")
    assert t2.tags == []

def test_get_task_missing_returns_none(tm: TaskManager) -> None:
    assert tm.get_task(99) is None

def test_complete_unknown_task_raises(tm: TaskManager) -> None:
    with pytest.raises(TaskNotFoundError, match="99"):
        tm.complete_task(99)

def test_complete_task_marks_done(tm: TaskManager) -> None:
    t = tm.add_task("x")
    tm.complete_task(t.id)
    task = tm.get_task(t.id)
    assert task is not None
    assert task.done is True
    

@pytest.mark.parametrize(
    ("filter_done", "expected"),
    [(None, {"a", "b"}), (True, "b"), (False, {"a"})],
)

def test_list_Tasks_filter(tm: TaskManager, filter_done: bool | None, expected: set[str]) -> None:
    tm.add_task("a")
    tm.add_task("b").done = True
    assert {t.title for t in tm.list_tasks(filter_done)} == expected

def test_sort_by_due_date(tm: TaskManager) -> None:
    late = tm.add_task("gec", due=date(2026, 12, 1))
    early = tm.add_task("erken", due=date(2026, 1, 1))
    assert sort_tasks([late, early], key= lambda t: t.due_date) == [early, late]

def test_search_by_title(tm: TaskManager) -> None:
    tm.add_task("alisveris")
    tm.add_task("spor")
    assert [t.title for t in search_tasks(tm.list_tasks(), key=lambda t: "spor" in t.title)] == ["spor"]