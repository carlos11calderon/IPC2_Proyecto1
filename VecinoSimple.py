class VecinoSimple:

    def __init__(self, v,p) :
        self.v= v
        self.p=p
        self.padre= None
        self.visitado= False
        self.siguiente = None