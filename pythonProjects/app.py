class Human_Matrix_Universe:
    '''
        A class with methods to wake up, get training, enter matrix,
        battle agents, leave matrix, decide to stay
        class attributes:
            name, fighting styles (list), awake
    '''

    def __init__(self, name, fighting_styles=[], awake=False):
        self.name = name
        self.fighting_styles = fighting_styles
        self.awake = awake

    def pill_decision(self, pill):
        #         updating a class attribute
        if pill == 'red':
            self.awake = True
        else:
            self.awake = False
            print('Stays hooked to the machine')

    def get_training(self):
        self.fighting_styles += ['kung fu', 'taekwando', 'aikido', 'druken monk', 'winghun']
        print(f'\n You know {self.fighting_styles}')

    #     Dynamically adjust class attribute
    def specific_training(self, fighting_style):
        self.fighting_styles.append(fighting_style)
        print(f'\n You know {fighting_style}')

    def enter_matrix(self):
        print('\n Plug in, Enter the Matrix')
        self.location = 1

    def exit_matrix(self):
        print('\n Pick up the Phone, Exit the Matrix')
        self.location = 0

    def dodge_bullets(self):
        if self.location:
            print('Agents are coming, slow down time, do crazy backbends')
        else:
            print('Run')