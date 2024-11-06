class UndergroundSystem:

    def __init__(self):
        self.id_to_startinfo = {} #id -> (startstation, starttime)
        self.route_to_info = {} # (startstation, endstation) -> [time, total]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_to_startinfo[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, starttime = self.id_to_startinfo[id]
        total = t - starttime 
        if (startStation, stationName) not in self.route_to_info:
            self.route_to_info[(startStation, stationName)] = [0,0]

        self.route_to_info[(startStation, stationName)][0] += 1
        self.route_to_info[(startStation, stationName)][1] += total
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.route_to_info[(startStation, endStation)][0]
        total = self.route_to_info[(startStation, endStation)][1]

        return (total / time)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)