from app import app, db


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.String(128))
    value = db.Column(db.Integer())
    status = db.Column(db.String(128))
    unit = db.Column(db.String(128))
    subject = db.Column(db.String(128))

    def __repr__(self):
        return f'{self.period} - {self.value} - {self.status} - {self.unit} - {self.subject}'
