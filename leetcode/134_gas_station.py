class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_gas = 0
        current_gas = 0
        starting_index = 0

        for index in range(len(gas)):
            # if current gas is < 0, all stations from starting index until now are bad
            if current_gas < 0:
                starting_index = index
                current_gas = 0

            # fill up and drain for the upcoming ride
            current_gas += gas[index] - cost[index]

            # update total gas
            total_gas += gas[index] - cost[index]
        
        return starting_index if total_gas >= 0 else -1











            
            