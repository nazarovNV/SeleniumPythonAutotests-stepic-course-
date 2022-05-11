class Entity():
    name=""
    def __init__(self, name):
        self.name=name
        print("Создано существо "+ name)
    @staticmethod
    def staticmethod():
        print('Привет, я ' + Entity.name)

Men = Entity("Борис")
Entity.name = Men.name
Men.staticmethod()
#Myclass.staticmethod()
