from flask_table import Table, Col, LinkCol

class Results(Table):
	user_id=Col('Id', show=False)
	first_name=Col('First Name')
	age=Col('Age')
	edit=LinkCol('Update', 'edit', url_kwargs=dict(user_id='user_id'))
	delete = LinkCol('Delete', 'delete', url_kwargs=dict(user_id='user_id'))