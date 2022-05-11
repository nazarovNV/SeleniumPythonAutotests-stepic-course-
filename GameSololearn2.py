# Класс GameObject  которого есть атирибуты class_name, desc, objects
class GameObject:
    class_name = ""
    desc = ""
    objects = {}

# Конструктор класса GameObject в который вводится name

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

# Метод вывода описания обьекта при использовании
# которого выводится название класса self.class_name и описание self.desc

    def get_desc(self):
        return self.class_name + "\n" + self.desc

# Класс Goblin который наследуется от GameObject#
# и которого есть атрибуты class_name и desc они перезаписывают атрибуты класса GameObject


class Goblin(GameObject):
    class_name = "goblin"
    desc = "A foul creature"

# создаем экземпляр класса Goblin с name="Gobbly"

goblin = Goblin("Gobbly")


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)

def say(noun):
    return 'You said "{}"'.format(noun)


verb_dict = {
    "say": say,
    "examine": examine
}

def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb())

#while True:
#    get_input()
print(GameObject.objects["goblin"].get_desc())



