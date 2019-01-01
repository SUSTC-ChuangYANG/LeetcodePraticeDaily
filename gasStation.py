class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        return self.solution_2(gas,cost)
    def solution_2(self,gas,cost):
        total = 0
        start = 0
        debt = 0
        for i in range(len(gas)):
            total += gas[i]-cost[i]
            if total < 0:
                debt += total
                total = 0
                start = i+1
        return start if total + debt >=0 else -1



    def solution_1(self,gas,cost):
        remnant = list(map(lambda x: x[0] - x[1], zip(gas, cost)))
        if sum(remnant) < 0:
            return -1
        candidates = dict()
        for i in range(len(remnant)):
            if remnant[i] >= 0:
                candidates[i] = remnant[i]

        i = 0
        while candidates and i < len(gas):
            i += 1
            remove = list()
            for idx, value in candidates.items():
                new_value = value + remnant[(idx + i) % len(gas)]
                if new_value < 0:
                    remove.append(idx)
                else:
                    candidates[idx] = new_value
            for idx in remove:
                del candidates[idx]
        if candidates:
            return candidates.popitem()[0]
        else:
            return -1
