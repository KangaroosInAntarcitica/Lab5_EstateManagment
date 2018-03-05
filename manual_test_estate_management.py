from estate_management import *

prompt = '''Please enter a possible option what you would like to do:
1. Display properties
2. Add property
3. Remove property
4. Buy property
5. exit
'''

def run():
    """ Run the test version of program """
    agent = Agent()

    put = input(prompt)
    while put not in ('5', 'exit', ''):
        if put[0] in ('1', 'D', 'd'):
            agent.display_properties()
        elif put[0] in ('2', 'A', 'a'):
            agent.add_property()
        elif put[0] in ('3', 'R', 'r'):
            agent.remove_property()
        elif put[0] in ('4', 'B', 'b'):
            agent.buy_property()
        else:
            print('Nothing could be selected!')

        put = input(prompt)

    print('\nYou exited the application!')


if __name__ == '__main__':
    run()
