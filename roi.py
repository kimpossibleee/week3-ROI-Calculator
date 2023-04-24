class RoiCalculator:
    def __init__(self):
        self.initial_investment = None
        self.yt_inflow = 0
        self.expenses = None
        self.roi = 0
        self.views = None
        self.display = {
            'Inflow': {'YOUTUBE': 0},
            'Expenses': {},
        }
        self.dollar_per_thousand_view_gross = 0

    def add_initial_investment(self):
        try:
            self.initial_investment = float(input('What is your total initial investment? ie) cameras, video editing software: '))
        except ValueError as e:
            print(f'{e}: Please enter digits only.')
        if self.initial_investment == None:
            self.add_initial_investment()



    def add_inflow(self):
        try:
            inflow_amount = float(input('Input the total $$$ you cashed out from Youtube: '))
        except ValueError as e:
            print(e)
        try:
            self.views = int(input('Input your total # of channel views: '))
        except ValueError as e:
            print(f'{e}: Please enter digits only.')
        if self.views == None:
            self.add_inflow()
        self.yt_inflow += inflow_amount
        self.display['Inflow']['YOUTUBE'] = self.display['Inflow']['YOUTUBE'] + inflow_amount

    def add_expenses(self):
        try:
            expense_source = input('Input the name of your expense: ').upper()
            expense_amount = float(input(f'Input the amount of "{expense_source}" expense: '))
        except ValueError as e:
            print(f'{e}: Please enter digits only.')
        if expense_amount == None:
            self.add_expenses()
        self.expenses += expense_amount
        with open('day5/expenses.txt', 'w') as expenses:
            expenses.write(f'{expense_source}: {expense_amount:.2f}')
        self.display['Expenses'][expense_source] = self.display['Expenses'].get(
            expense_source, 0) + expense_amount

    def calculate_roi(self):
        self.roi = ((self.yt_inflow - self.expenses) /
            self.initial_investment) * 100
    def print_display(self):
        for key, value in self.display.items():
            print(f'{key}:')
            for k, v in value.items():
                print(f'     {k}: {v}')
        print(f'ROI = {self.roi:.2f}%')
        self.dollar_per_thousand_view_gross = (self.yt_inflow / self.views) * 1000
        print(f'$ per 1000 view (GROSS): ${self.dollar_per_thousand_view_gross:.2f}')
