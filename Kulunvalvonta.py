
DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}


class Accesscard:

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: card holders personal id (str)
        :param name: card holders name (str)
        """

        self.id = id
        self.name = name
        self.access = []

    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        """

        info = f'{self.id}, {self.name}, access: '
        self.access.sort()
        for codes in self.access:
            info = f'{info} {codes}, '
        print(info[:-2])

    def add_access(self, new_access_code):
        """
        Adds new access code to user, if user doesn't already have access.
        
        :param new_access_code: The accesscode to be added in the card.
        """

        if new_access_code not in self.access:
            if new_access_code not in DOORCODES:
                for door, area in DOORCODES.items():
                    if new_access_code in area:
                        if door in self.access:
                            self.access.remove(door)
                self.access.append(new_access_code)
            else:
                to_add = True
                for area_code in DOORCODES[new_access_code]:
                    if area_code in self.access:
                        to_add = False
                if to_add:
                    self.access.append(new_access_code)

    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.
        """

        if door in self.access:
            return True
        for code in self.access:
            if code in DOORCODES[door]:
                return True
        return False

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: The accesscard whose access rights are added to this card.
        """
        if card.access[0] == '':
            return
        for code in card.access:
            self.add_access(code)
        

def command_info(data, card_id):
    
    for user in data:
        if user.id == card_id:
            user.info()
            return
    print('Error: unknown id.')


def command_access(data, card_id, door_id):
    
    count = len(data)
    for user in data:
        if user.id == card_id:
            try:
                if door_id in DOORCODES[door_id] or door_id in DOORCODES:
                    if user.check_access(door_id):
                        print(
                            f'Card {user.id} ( {user.name} ) has access to door {door_id}')
                        break
                    else:
                        print(
                            f'Card {user.id} ( {user.name} ) has no access to door {door_id}')
                        break
                else:
                    print('Error: unknown doorcode.')
                    break
            except:
                print('Error: unknown doorcode.')
                break
        count -= 1
        if count == 0:
            print('Error: unknown id.')


def command_add(data, card_id, access_code):
    
    count = len(data)
    for user in data:
        if user.id == card_id:
            for door, area in DOORCODES.items():
                if access_code == door or access_code in area:
                    user.add_access(access_code)
                    break
            else:
                print('Error: unknown accesscode.')
            break
        count -= 1
        if count == 0:
            print('Error: unknown id.')


def command_merge(data, card_id_to, card_id_from):
    
    first_found, second_found = False, False
    for user in data:
        if user.id == card_id_to:
            card_id_to = user
            first_found = True
        if user.id == card_id_from:
            card_id_from = user
            second_found = True
    if first_found and second_found:
        card_id_to.merge(card_id_from)
    else:
        print('Error: unknown id.')


def get_data():

    data = []
    file = open('accessinfo.txt', 'r')
    count = 0

    for line in file.readlines():
        data.append(Accesscard(line.split(';')[0], line.split(';')[1]))
        for codes in line.split(';')[2].split(','):
            data[count].add_access(codes.strip("\n"))

        data[count].access.sort()
        count += 1

    data.sort(key=lambda y: y.id)
    file.close
    return data


def main():

    data = get_data()

    while True:
        line = input('command> ')

        if line == '':
            break

        strings = line.split()
        command = strings[0]

        if command == 'list' and len(strings) == 1:

            for user in data:
                user.info()

        elif command == 'info' and len(strings) == 2:

            card_id = strings[1]

            command_info(data, card_id)

        elif command == 'access' and len(strings) == 3:

            card_id = strings[1]
            door_id = strings[2]

            command_access(data, card_id, door_id)

        elif command == 'add' and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]

            command_add(data, card_id, access_code)

        elif command == 'merge' and len(strings) == 3:

            card_id_to = strings[1]
            card_id_from = strings[2]

            command_merge(data, card_id_to, card_id_from)

        elif command == 'quit':
            print('Bye!')
            return
        else:
            print('Error: unknown command.')


main()
