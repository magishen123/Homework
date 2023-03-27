import Couch
import Payment
import time_bound

def zapros(qesttion):#основная
    opustit = qesttion.lower()
    if 'расп' in opustit:
        time_bound.schedule()
    elif 'добав' in opustit:
        time_bound.new_schedule()
    elif 'трен' in opustit:
        Couch.coach()
    elif 'оплат' in opustit:
        Payment.payment()
    else:
        print('Вам не к нам')
