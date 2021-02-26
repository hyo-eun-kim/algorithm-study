# 주유소
# 원형으로 경로가 연결된 주유소 목록이 있따.
# 각 주유소는 gas[i] 만큼의 기름을 갖고 있으며, 다음 주유소로 이동하는데 cost[i] 가 필요하다.
# 기름이 부족하면 이동할수 없다고 할때 모든 주유소를 방문할수 있는 출발점의 인덱스를 출력하라.
# 출발점이 존재하지 않을경우 -1 을 리턴하며, 출발점은 유일하다.


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost) :  # 비용이 가스보다 많으면 출발점이 존재하지 않는 경우!
            return -1 
        
        start, fuel =0,0
        for i in range(len(gas)):
            # 출발점이 안되는 지점 판별
            if gas[i]+fuel < cost[i]:    # 기름의 양이 비용보다 작으면 
                start = i+1              # start 점 옮기고 기름 초기화
                fuel=0
            else :                       # 기름의 양이 비용보다 크면
                fuel+= gas[i]-cost[i]    # 연료에 사용하고 남은기름 더해주기
        return start
