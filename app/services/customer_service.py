from app.models.customer import Customer, db

class CustomerService:
    @staticmethod
    def add_customer(name, email):
        customer = Customer(name=name, email=email)
        db.session.add(customer)
        db.session.commit()

    @staticmethod
    def get_all_customers():
        return Customer.query.all()