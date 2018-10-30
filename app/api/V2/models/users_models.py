from app.db_config import init_db

class User():
    def __init__(self):
        self.db = init_db()


    def save_user(self, email, name, password, role):
        user = {
            "email": email,
            "name":name,
            "password": password,
            "role": role
        }
        query = """INSERT INTO users (name, email, role, password) VALUES
                (%(name)s, %(email)s, %(role)s,  %(password)s)"""
        curr = self.db.cursor()
        curr.execute(query, user)
        self.db.commit()
        return user

    def get_user_by_email(self, email):
        """return user from the db given a username"""
        db = self.db
        curr = db.cursor()
        curr.execute(
            """SELECT user_id, name, email, password \
            FROM users WHERE email = '%s'""" % (email))
        data = curr.fetchone()
        curr.close()
        return data
