class profile:
    def __init__(self, name):
        self.name       = name
        self.chat_log   = []
        self.room       = None

    def receive(self, sender, message):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)
    
    def send_message(self, message):
        self.room.broadcast(self.name, message)

    def send_message_private(self, who, message):
        self.room.message(self.name, who, message)


class Discord:
    """Mediator"""
    def __init__(self):
        self.people = []
    
    def broadcast(self, source, message):
        """send to all people except self."""
        for p in self.people:
            if p.name != source:
                p.receive(source, message)
    
    def join(self, person):
        join_msg = f'{person.name} joins the discord.'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)
        return self
    
    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)
        


if __name__ == '__main__':
    dcd  = Discord()
    zach = profile('zach')
    kamj = profile('kamaji')
    
    dcd\
        .join(zach)\
        .join(kamj)
    
    zach.send_message('Bonjour!')
    kamj.send_message('Ça va!')

    garc = profile('garçon')
    dcd.join(garc)
    garc.send_message('ciao!!')
    zach.send_message_private('kamaji', 'aghh oui, le garçon...')