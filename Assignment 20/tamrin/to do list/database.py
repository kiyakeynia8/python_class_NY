import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("todo_list.db")
        self.cursor = self.con.cursor()
        self.tasks = []

    def get_tasks(self):
        query = "SELECT * FROM tasks ORDER BY is_done"
        result = self.cursor.execute(query)
        self.tasks = result.fetchall()
        return self.tasks

    def add_new_task(self,new_title,new_description,new_date,new_time,i_o_n):
        try:
            query = f"INSERT INTO tasks(title, description, date, time, i_o_n)VALUES('{new_title}', '{new_description}', '{new_date}', '{new_time}', '{i_o_n}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        
        except:
            return False

    def remove_task(self,id):
        try:
            self.cursor.execute(f"DELETE FROM tasks WHERE id = '{id}'")
            self.con.commit()
            return True

        except:
            return False
    
    def task_done(self,id):
        try:
            self.cursor.execute(f'SELECT * FROM tasks WHERE id = "{id}"')
            task = self.cursor.fetchall()
            if task != None:
                new_id = len(self.tasks) + id
                self.cursor.execute(f'UPDATE tasks SET is_done = 1 WHERE id = {id}')
                self.con.commit()
                self.cursor.execute(f'UPDATE tasks SET id = {new_id} WHERE is_done = 1')
                self.con.commit()
                return True
        
        except:
            return False