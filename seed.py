from models import session, Company, Dev, Freebie

# Create some companies
afia = Company(name='Afia', founding_year=2018)
movit = Company(name='Movit', founding_year=2019)
kasuku = Company(name='Kasuku', founding_year=2020)

# Create some devs
helen = Dev(name='Helen')
kate = Dev(name='Kate')

# Add companies and devs to the session
session.add_all([afia, movit, kasuku, helen, kate])
session.commit()

# Create some freebies
freebie1 = Freebie(item_name='T-shirt', value=10, dev=helen, company=afia)
freebie2 = Freebie(item_name='Sticker', value=1, dev=kate, company=movit)
freebie3 = Freebie(item_name='Mug', value=5, dev=helen, company=kasuku)

# Add freebies to the session
session.add_all([freebie1, freebie2, freebie3])
session.commit()