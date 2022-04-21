"""
Customer repository module
"""
from typing import List

from app.exceptions.exceptions import CannotUpdateNotFoundCustomer
from app.models.database.customer import Customer
from app.schemas.customer import CustomerBase, CustomerSchema


class CustomerRepository:
    """
    Class with manipulate Customer model
    """

    @staticmethod
    def save(data: CustomerBase) -> CustomerSchema:
        """
        This method save item in Customer

        :params:
            item: Dict

        :return:
            Customer
        """
        return Customer(**data.dict()).save_safe()

    @staticmethod
    def update(data: CustomerBase) -> CustomerSchema:
        """
        This method save item in Customer

        :params:
            data: CustomerBase

        :return:
            Customer
        """
        user = Customer.objects(id=data.id).first()
        if not user:
            raise CannotUpdateNotFoundCustomer
        user.email = data.email
        user.name = data.name
        user.updated_at = data.updated_at
        return user.save_safe()

    @staticmethod
    def get_all_users() -> List[CustomerSchema]:
        """
        This method get last token in Customer

        """
        return Customer.objects().all()
