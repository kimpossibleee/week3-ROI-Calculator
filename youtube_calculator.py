from user import User
from roi import RoiCalculator
from youtube_api import CompareWithYoutuber
from ascii import youtube, roi_art, scale
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class YoutubeCalculator():
    def __init__(self):
        self.is_on = True

    def run_application(self):
        print(youtube)
        my_user = User()
        my_user.sign_up()
        while self.is_on == True:
            user_input = input('\nWhat would you like to do? 1) ROI calculator 2) Compare with another Youtuber 3) Quit [Enter the number] ')
            clear()
            if user_input == '1':
                print(roi_art)
                roi_is_on = True
                while roi_is_on:
                    user_calc = RoiCalculator()
                    user_calc.add_initial_investment()
                    user_calc.add_inflow()
                    more_expenses = True
                    while more_expenses == True:
                        input_expenses = input('Would you like to add expenses? (y or n): ')
                        if input_expenses == 'y':
                            user_calc.add_expenses()
                        elif input_expenses == 'n':
                            user_calc.print_display()
                            more_expenses = False
                            roi_is_on = False
                        else:
                            print('Enter a valid input.')
            elif user_input == '2':
                print(scale)
                user_compare = CompareWithYoutuber()
                user_compare.grab_channel_views()
                user_compare.comparison()
            elif user_input == '3':
                print(youtube)
                print('Have a nice day!')
                self.is_on = False
            else:
                print('You have not entered a valid option. Please try again.')
