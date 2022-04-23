"""
A Customer service module
"""
from app.repository.customer import CustomerRepository
from app.schemas.customer import CustomerSchema


class CustomerService:
    def create_new_customer(self, customer: CustomerSchema) -> CustomerSchema:
        return CustomerRepository().create(customer)
