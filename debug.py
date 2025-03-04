from models import session, Company, Dev, Freebie

# Start an interactive session
import ipdb; ipdb.set_trace()

# Example commands to test the methods
# company = session.query(Company).first()
# dev = session.query(Dev).first()
# freebie = session.query(Freebie).first()

# Test Company methods
# company.give_freebie(dev, 'Notebook', 15)
# print(Company.oldest_company().name)

# Test Dev methods
# print(dev.received_one('T-shirt'))
# dev.give_away(session.query(Dev).filter_by(name='Kate').first(), freebie)

# Test Freebie methods
# print(freebie.print_details())