def decorator():
        try:
            self.account += 0
        except Exception:
            raise NameError('Exception: "No username defined!"')


@decorator()
class User():
    def _init_(self, account):
        self.account = account
    
    def get_account_ballance(self):
        self.account += 0


u = User()
u.get_account_balance()


