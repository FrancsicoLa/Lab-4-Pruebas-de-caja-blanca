import process_grades
import pytest


@pytest.mark.parametrize(
    "students, expected",
    [
        (
            [{"name": "Ana", "grades": [55, 55, 55]}],
            {"passed": ["Ana"]},
        ),
    ],
)
@pytest.mark.system
def test_process_grades_pass(students, expected):
    result = process_grades.process_grades(students)
    assert result["passed"] == expected["passed"]


@pytest.mark.parametrize(
    "students, expected",
    [
        (
            [{"name": "Ana", "grades": [55, 55, 55]}],
            "is in recovery"
        ),
    ],
)
@pytest.mark.system
def test_process_grades_recovery(students, expected, capsys):
    result = process_grades.process_grades(students)
    captured = capsys.readouterr()
    assert expected in captured.out

@pytest.mark.parametrize(
    "students, expected",
    [
        (
            [{"name": "Ana", "grades": [40, 40, 40]}],
            {"failed": ["Ana"]}
        ),
    ],
)

@pytest.mark.wip
def test_process_grades_failed(students, expected):
    result = process_grades.process_grades(students)
    assert result["failed"] == expected["failed"]






