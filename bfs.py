from collections import deque
import heapq
import math

EARTH_RADIUS = 6371 # In kilometers

def station_distance(station_from, station_to):
    p = math.pi / 180
    stf_lat, stf_lon = station_from
    stt_lat, stt_lon = station_to

    lat_angle = (stt_lat - stf_lat) * p
    lat_haversine = (1 - math.cos(lat_angle)) / 2

    lon_angle = (stt_lon - stf_lon) * p
    lon_haversine = (1 - math.cos(lon_angle)/2)

    haversine = lat_haversine + math.cos(stf_lat * p)*math.cos(stt_lat * p)*lon_haversine

    haversine_distance = 2 * EARTH_RADIUS * math.asin(math.sqrt(haversine))

    return haversine_distance

def visited_to_path(visited, target):
    path = [target]
    cur = target
    total_weight = 0
    while visited[cur]:
        next_node, weight = visited[cur]
        path.append(next_node)
        cur = next_node
        total_weight += weight

    path.reverse()
    return total_weight, path

def bfs(graph:dict, source:str, target:str):
    visited = dict()
    visited[source] = None
    to_visit = deque([source])

    while to_visit:
        cur = to_visit.popleft()

        if cur == target: break

        for neigh, weight in graph[cur]['edges'].items():

            if neigh in visited: continue
            visited[neigh] = (cur, weight)
            to_visit.append(neigh)

    return visited_to_path(visited, target)

def a_star(graph: dict, source: str, target: str):
    visited = {source: None}
    cost_so_far = {source: 0}

    target_pos = (graph[target]['latitude'], graph[target]['longitude'])

    to_visit = [(0, source)]
    while to_visit:
        cost, cur = heapq.heappop(to_visit)

        if cur == target:
            break

        for neigh, weight in graph[cur]['edges'].items():
            new_cost = cost_so_far[cur] + weight
            if new_cost < cost_so_far.get(neigh, 1_000_000_000):
                cost_so_far[neigh] = new_cost

                neigh_pos = (graph[neigh]['latitude'], graph[neigh]['longitude'])
                priority = new_cost + station_distance(neigh_pos, target_pos)

                heapq.heappush(to_visit, (priority, neigh))
                visited[neigh] = (cur, weight)

    return visited_to_path(visited, target)