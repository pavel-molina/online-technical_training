from xmlrpc import client

url = 'https://pavel-molina-online-technical-training-dev-academy-2441282.dev.odoo.com'
db = 'pavel-molina-online-technical-training-dev-academy-2441282'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url)) 
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url)) 

model_access = models.execute_kw(db, uid, password, 'sale.order', 'check_access_rights', ['write'], {'raise_exception':False})
print(model_access)

draft_quotes = models.execute_kw(db, uid, password, 'sale.order', 'search', [[['state', '=', 'draft']]])
print(draft_quotes)

if_confirmed = models.execute_kw(db, uid, password, 'sale.order', 'action_confirm', [draft_quotes])
print(if_confirmed)