# 广度优先算法
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def find_mogo(name):
    return name[-1] == 'm'


def dicstl(name):
    search_name = deque()
    search_name += graph[name]
    searchd = []
    while search_name:
        if search_name not in searchd:
            person = search_name.popleft()
            if find_mogo(person):
                print('he is the mongo:{}'.format(person))
                return
            else:
                searchd.append(person)
                print(searchd)
                search_name += graph[person]


dicstl('you')
