from collections import deque

graph = {'me': ['alice', 'bob', 'claire'], 'alice': ['anuj', 'peggy'], 'claire': ['thom', 'jenny']}

search_queue = deque()
search_queue += graph['me']


def person_is_seller(name):
    return name[-1] == 'm'


def search(queue):
    searched = []
    while queue:
        person = queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is seller!')
                return True
            else:
                if person in graph:
                    queue += graph[person]
                    searched.append(person)
    return False
