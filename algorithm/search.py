import collections

# Breadth-First Search
def person_is_mongo_seller(name):
    return name[-1] == 'm'
def bfs(name, graph):
    search_queue = collections.deque()
    search_queue += graph[name]
    searched = list()
    while search_queue:
        person = search_queue.popleft()
        if person not in search_queue:
            if person_is_mongo_seller(person):
                print(person + " is mongo seller!")
                return True
            else:
                print(person + " is not mongo seller.")
                search_queue += graph[person]
                searched.append(person)
    return False
## test data
graph = {}
graph["you"] = ["alice","bob","claire"]
graph["alice"] = ["anuj","peggy"]
graph["bob"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

if(__name__ == "__main__"):
    bfs("you", graph)