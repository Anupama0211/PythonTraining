from Assignment6.TechnicalException import TechnicalException
from Assignment6.InvalidOrderAmountException import InvalidOrderAmountException
from Assignment6.NoOrdersSubmittedException import NoOrdersSubmittedException
from Assignment6.UserNotFoundException import UserNotFoundException


class UserReportController:

    def __init__(self):
        self._user_report_builder = None

    @property
    def user_report_builder(self):
        return self._user_report_builder

    @user_report_builder.setter
    def user_report_builder(self, value):
        self._user_report_builder = value

    def get_user_total_order_amount_view(self, user_id, model):
        total_message = self.get_user_total_message(user_id)
        if total_message != "Technical Error":
            model.add_attribute("userTotalMessage", total_message)
            total_message = "userTotal"
        return total_message

    def get_user_total_message(self, user_id):
        try:
            amount = self._user_report_builder.get_user_total_order_amount(user_id)
            return "User Total: {0}$".format(amount)
        except (
                TechnicalException, UserNotFoundException, NoOrdersSubmittedException,
                InvalidOrderAmountException) as e:
            return e
