class Panelist:

    def __init__(self, name: str, phone: str, email: str, badge_number: str, panels: list):

        try:
            self.name = name
            self.phone = phone
            self.email = email
            self.badge_number = badge_number
            self.panels = panels
            self.reimbursement = self.check_reimbursement()
        except:
            print("Cannot create panelist object")

    def check_reimbursement(self):

        if len(self.get_panels()) == 1:
            return "50% Reimbursement"

        elif len(self.get_panels()) >= 2:
            return "100% Reimbursement"

        else:
            return "BUG!"


    def get_name(self):
        return self.name


    def get_phone(self):
        return self.phone


    def get_email(self):
        return self.email

    def get_badge_number(self):
        return self.badge_number

    def get_panels(self):
        return self.panels

    def get_reimbursement(self):
        return self.reimbursement

    def panels_to_string(self):

        string = ""

        for panel in self.panels:
            string = "\n" + string + panel

        return string