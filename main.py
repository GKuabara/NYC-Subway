import utils
from bfs import bfs, a_star

stops = utils.load_gtfs("data/stops.txt", set([0,1,2,3]))
trips = utils.load_gtfs("data/stop_times.txt", set([0,1,2,3]))
transfers = utils.load_gtfs("data/transfers.txt", set([0,1]))
graph = utils.create_graph(stops, trips, transfers)

path = bfs(graph, '101', 'F24')
print(f"bfs: {' '.join(list(map(lambda x: str(x), path)))}")

path = a_star(graph, '101', 'F24')
print(f"a_star: {' '.join(list(map(lambda x: str(x), path)))}")