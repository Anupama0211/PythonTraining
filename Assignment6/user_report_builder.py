from Assignment6.InvalidOrderAmountException import InvalidOrderAmountException
from Assignment6.NoOrdersSubmittedException import NoOrdersSubmittedException
from Assignment6.TechnicalException import TechnicalException
from Assignment6.UserNotFoundException import UserNotFoundException


class UserReportBuilder:

    def __init__(self):
        self._user_dao = None

    @property
    def user_dao(self):
        return self._user_dao

    @user_dao.setter
    def user_dao(self, value):
        self._user_dao = value

    def get_user_total_order_amount(self, user_id):

        if self.user_dao is None:
            raise TechnicalException()

        user = self.user_dao.get_user(user_id)
        if user is None:
            raise UserNotFoundException()

        orders = user.get_all_orders()

        if len(orders) == 0:
            raise NoOrdersSubmittedException()

        result = 0.0
        for order in orders:
            if order.is_submitted():
                total = order.total()
                if total < 0:
                    raise InvalidOrderAmountException()
                result += total

        return result
