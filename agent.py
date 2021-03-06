from decorator import check_access


class BaseUser:
    def __init__(self, username, password, first_name, last_name, email, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @classmethod
    def prompt(cls):
        username = input('Please enter username : ')
        password = input('Please enter password : ')
        first_name = input('Please enter first_name : ')
        last_name = input('Please enter last_name : ')
        email = input('Please enter email : ')
        result = {
            'username': username, 'password': password, 'first_name': first_name,
            'last_name': last_name, 'email': email
        }
        return result


class Supervisor(BaseUser):
    agents_list = list()
    properties_list = dict()
    deal_list = list()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def create_agent():
        agent_data = Agent.prompt()
        agent = Agent(**agent_data)
        return agent

    @classmethod
    def agent_data(cls):
        temp = []
        for agent in cls.agents_list:
            temp.append(agent.serializer())
        return temp

    @classmethod
    def search(cls, username):
        for agent in cls.agents_list:
            if agent.username == username:
                return agent
            return None


class Agent(BaseUser):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Supervisor.agents_list.append(self)
        self.properties_list = list()
        self.deal_list = list()
        self.__has_access = False

    def __str__(self):
        return f'agent instance {self.username}'

    def __repr__(self):
        return f'{self.__class__.__name__}(username={self.username},email={self.email})'

    def create_property(self, **kwargs):
        instance = None
        self.properties_list.append(instance)

    @classmethod
    def prompt(cls):
        return BaseUser.prompt()

    def serializer(self):
        data = self.__dict__
        print(data)
        data.pop('properties_list')
        data.pop('deal_list')
        data.pop('_Agent__has_access', None)
        return data

    def check_password(self, password):
        check = bool(self.password == password)
        if check:
            self.__has_access = True
        return check

    def has_access(self):
        return self.__has_access

    @check_access
    def create_deal(self):
        print('HI')
