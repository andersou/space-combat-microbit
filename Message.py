class Message:
    def __init__(self,user,**kwargs):
        self.user = user;
        self.acc_x = kwargs.get('acc_x')
        self.acc_y = kwargs.get('acc_y')
        self.orientation = kwargs.get('orientation')
        self.a_press = kwargs.get('a_press')
        self.b_press = kwargs.get('b_press')


