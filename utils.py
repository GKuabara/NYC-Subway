import csv

def load_gtfs(filename:str, col_idx:set) -> list:
    data = []
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        print(header)
        for row in reader:
            line = row
            row_data = []
            for idx, cell in enumerate(line):
                if idx in col_idx:
                    row_data.append(cell)
            data.append(row_data)
    return data

def create_graph(stops:list, trips:list, transfers:list) -> dict:
    graph = {}

    # Create stops node with names
    for stop in stops:
        stop_id = stop[0].rstrip('SN')
        graph[stop_id] = {
            'name': stop[1],
            'edges': dict(),
            'latitude': float(stop[2]),
            'longitude': float(stop[3])
        }

    # Populate connections
    for idx in range(1,len(trips)):
        last = trips[idx-1]
        cur = trips[idx]
        
        # Checks Trip Id
        if cur[0] != last[0]: continue
        
        last_id = last[1].rstrip('SN')
        cur_id = cur[1].rstrip('SN')

        h1, m1, s1 = map(int, last[3].split(':'))
        h2, m2, s2 = map(int, cur[2].split(':'))
        diff_time = abs((h1*3600 + m1*60 + s1) - (h2*3600 + m2*60 + s2))

        cur_time = graph[last_id]['edges'].get(cur_id, 1_000_000)
        graph[last_id]['edges'][cur_id] = min(cur_time, diff_time)

    for last_id, cur_id in transfers:
        if last_id != cur_id:
            graph[last_id]['edges'][cur_id] = 0

    return graph

# Usage
# stops = load_gtfs("data/stops.txt", set([0,1]))
# trips = load_gtfs("data/stop_times.txt", set([0,1,2,3]))
# transfers = load_gtfs("data/transfers.txt", set([0,1]))
# graph = create_graph(stops, trips, transfers)
# print(list(graph.items())[:10])