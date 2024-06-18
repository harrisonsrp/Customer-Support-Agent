from Database import db


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"<Category {self.name}>"
    
    
    @classmethod
    def read(cls):
        return cls.query.all()
    
