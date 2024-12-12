from class_database import Database

db = Database("postgresql://postgres:qwerty12@localhost:5432/QA")


def test_get_subject():
    result = db.get_subjects()
    assert len(result) == 15


def test_insert_subject():
    result_before = db.get_subjects()
    db.add_subject()
    result_after = db.get_subjects()
    row_end = result_after[-1]
    db.delete_subject(16)
    assert row_end["subject_id"] == 16
    assert row_end["subject_title"] == "Python"
    assert len(result_after) - len(result_before) == 1


def test_update_subject():
    db.add_subject()
    db.update_subject(16, 'Java')
    result_after = db.get_subjects()
    row_end = result_after[-1]
    db.delete_subject(16)
    assert row_end['subject_title'] == 'Java'


def test_delete_subject():
    db.add_subject()
    result_before = db.get_subjects()
    db.delete_subject(16)
    result_after = db.get_subjects()
    max_id = db.get_max_id_subject()
    assert max_id == 15
    assert len(result_before) - len(result_after) == 1
