'''
134. Gas Station
https://leetcode.com/problems/gas-station/
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
otherwise return -1. If there exists a solution, it is guaranteed to be unique
'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # 해 X
        if sum(gas) - sum(cost) < 0:
            return -1

        # 이 부분 이해 .. ?
        # 옳은 출발지점이라면 -> 특정 지점에서 멈추지 않는다 (순환한다)
        # 특정 지점에서 멈추면 -> 그 지점은 출발지점이 아니다. 이것을 이용한 것!
        cum_gas = 0
        start = 0
        for i in range(len(gas)):
            # 특정 지점에서 멈추면 그 지점은 출발지점이 아니다.
            if cum_gas + gas[i] < cost[i]:
                # 새로운 출발지점 설정
                start = i + 1
                cum_gas = 0
            else:
                cum_gas = cum_gas + gas[i] - cost[i]

        return start