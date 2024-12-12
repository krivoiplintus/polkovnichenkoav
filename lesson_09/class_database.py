from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Database:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_subjects(self):
        return self.db.execute(text("select * from subject s")).fetchall()

    def add_subject(self):
        return self.db.execute(text("insert into subject(subject_id, subject_title) values (16, 'Python')"))

    def delete_subject(self, id):
        self.db.execute(text("delete from subject where subject_id = :id_to_delete"), id_to_delete=id)

    def update_subject(self, id, title):
        self.db.execute(text("update subject set subject_title = :new_title where subject_id = :id_to_update"), new_title=title, id_to_update=id)

    def get_max_id_subject(self):
        return self.db.execute("select max(subject_id) from subject").fetchall()[0][0]
