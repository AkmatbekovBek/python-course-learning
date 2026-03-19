class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value


    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value


    def make_computations(self):
        print(f'CPU is bigger than MEMORY: {self.__cpu > self.__memory}')

    def __eq__(self, other):
        return self.__memory == other.__cpu

    def __ne__(self, other):
        return self.__memory != other.__cpu

    def __lt__(self, other):
        return self.__memory < other.__cpu

    def __gt__(self, other):
        return self.__memory > other.__cpu

    def __le__(self, other):
        return self.__memory <= other.__cpu

    def __ge__(self, other):
        return self.__memory >= other.__cpu

    def __str__(self):
        return f'{Computer.make_computations}'


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def __str__(self):
        return f'{self.__sim_cards_list}'

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, Sim_cards_list):
        self.__sim_cards_list = Sim_cards_list

    def call(self, sim_card_numder, call_to_numder):
        self.sim_card_numder = sim_card_numder
        self.call_to_numder = call_to_numder
        print(f'Идет звонок на номер: "{self.sim_card_numder}" с Сим-карты: {self.call_to_numder}')

s1 = '1 - Beeline'
s2 = '2 - Oshka'
s3 = '3 - Megakom'
list_sim = [s1, s2, s3]




class SmartPhone(Computer, Phone):
    def __init__(self):
        Computer.__init__(self, self.cpu, self.memory)
        Phone.__init__(self, self.sim_cards_list)

    def use_gps(location):

        print(f'Прокладывается маршрут с вашего местоположения до: "{location}"')

    def __str__(self):
        return f'Прокладывается маршрут с вашего местоположения до: "{SmartPhone.use_gps}."'


mac_ios = Computer(128, 540)
nokia = Phone(list_sim)
iphone = SmartPhone
samsung = SmartPhone

mac_ios.make_computations()
nokia.call('+996 709 618 550', s2)
iphone.use_gps('Молодая Гвардия')
samsung.call(samsung, '+996 704 317 722',s3)
