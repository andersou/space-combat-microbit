class Message:
    def __init__(self,user,**kwargs):
        self.user = user;
        self.acc_x = float(kwargs.get('acc_x'))
        self.acc_y = float(kwargs.get('acc_y'))
        self.orientation = float(kwargs.get('orientation'))
        self.a_press = kwargs.get('a_press') == 'True'
        self.b_press = kwargs.get('b_press')== 'True'




