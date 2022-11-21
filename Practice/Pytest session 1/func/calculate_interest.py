
class SimpleInterest:
    MAX_PRINCIPAL = 100000
    MIN_PRINCIPAL = 1000
    MIN_ROI = 5
    MAX_ROI = 15
    
    def __init__(self,principal, months, roi):
        self.principal = principal
        self.months = months
        self.roi = roi

    def calculate_interest(self):
        year = self.months_to_years()
        principal = self.validate_principal()
        roi = self.validate_rate_of_interest()
        interest = (principal*year*roi)//100
        return interest
    
    def months_to_years(self):
        years = self.months//12
        if years >= 1:
            return years
        raise ValueError('Months cannot be less than 12')
    
    def validate_principal(self):
        if SimpleInterest.MIN_PRINCIPAL <= self.principal <= SimpleInterest.MAX_PRINCIPAL:
            return self.principal
        raise ValueError(f"Principal amount has to be between \
                            {SimpleInterest.MIN_PRINCIPAL} and {SimpleInterest.MAX_PRINCIPAL}")
    
    def validate_rate_of_interest(self):
        if SimpleInterest.MIN_ROI <= self.roi <= SimpleInterest.MAX_ROI:
            return self.roi
        raise ValueError(f"Rate of interest has to be between \
                            {SimpleInterest.MIN_ROI} and {SimpleInterest.MAX_ROI}")