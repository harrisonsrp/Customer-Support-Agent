from Database import db


class Admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    @classmethod
    def create(cls,username, email, password):
        new_admin = cls(username=username, email=email, password=password)
        db.session.add(new_admin)
        db.session.commit()

    @classmethod
    def read(cls, email):
        return cls.query.filter_by(email=email).first()


    # def update(self, username=None, email=None, password=None):
    #     if username:
    #         self.username = username
    #     if email:
    #         self.email = email
    #     if password:
    #         self.password = password
    #     db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()




