"""
Customer repository module
"""
from app.models.database.customer import Customer
from app.schemas.customer import CustomerSchema


class CustomerRepository:
    """
    Class with manipulate Customer model
    """

    @staticmethod
    def create(customer: CustomerSchema) -> CustomerSchema:
        """
        This method save item in Customer

        :params:
            item: Dict

        :return:
            CustomerSchema
        """
        return Customer(**customer.dict()).save_safe()

