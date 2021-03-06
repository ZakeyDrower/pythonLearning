# 集合覆盖问题
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])
stations = {}
stations["knoe"] = set(["id","nv","ut"])
stations["ktwo"] = set(["id","wa","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])
final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station,states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            states_needed -= states_covered
            final_stations.add(station)
print(final_stations)

def f():
    return

print(f())
print(f())