import sys
from agent import Supervisor, Agent
from utils import check_credentials
from constansts import AGENTS_FILE_PATH
from store import save_to_file, load_agents

if __name__ == '__main__':
    if check_credentials(sys.argv):
        agent = Supervisor.create_agent()
        save_to_file(AGENTS_FILE_PATH, Supervisor.agent_data())
        # agents_data = load_agents(AGENTS_FILE_PATH)
        # _ = [Agent(**d) for d in agents_data]
        #
        # agent = None
        #
        # while agent is None:
        #     username = input('Enter your username : ')
        #     agent = Supervisor.search(username)
        #
        # password = input("Enter your password : ")
        # if agent.check_password(password):
        #     print('Welcome')
        # else:
        #     print('Goodbye')

    else:
        print('wrong credential')

