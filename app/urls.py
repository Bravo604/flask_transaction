from app import views
from app import app

app.add_url_rule('/', view_func=views.index, methods=['GET'], endpoint='index')
app.add_url_rule('/add/transaction', view_func=views.add_transaction, methods=['GET', 'POST'], endpoint='add_transaction')
