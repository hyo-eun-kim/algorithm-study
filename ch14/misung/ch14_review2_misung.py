def solution(n, results):
    wins, loses ={} , {}
    
    for i in range(1,n+1):
        wins[i], loses[i]= set(), set()
    
    for win , lose in results:
        wins[win].add(lose)  # 승리 : win 이 이긴 사람들
        loses[lose].add(win)  # 패배 : lose 가 진 사람들
    
    for i in range(1,n+1):
        # i를 이긴사람들(loses[i]) => i 에게 진 사람은(wins[i]) 반드시 이긴다.
        for winner in loses[i] : 
            wins[winner].update(wins[i])
        # i 에게 진 사람들(wins[i]) => i를 이긴 사람들(loses[i]) 에게는 반드시 진다.
        for loser in wins[i]:
            loses[loser].update(loses[i])

    cnt = 0
    for i in range(1,n+1):
        if len(wins[i]) + len(loses[i]) ==n-1:
            cnt +=1
    return cnt
        