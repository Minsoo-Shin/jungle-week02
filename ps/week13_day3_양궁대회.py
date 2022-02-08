# 큰 점수에서 최대한 많은 화살을 맞히게 한다. 
# 가능한 경우 천천히 큰 점수를 제외하고 맞힌다. 
# appeach의 점수간 갯수보다 1크게 한다. 

from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff, max_comb_cnt = 0, {}

    for comb in combinations_with_replacement(range(11), n):
        cnt = Counter(comb)
        print(cnt[1])
        score1, score2 = 0, 0
        for i in range(1, 11):
            if info[10-i] < cnt[i]:
                score1 += i
            elif info[10-i] > 0:
                score2 += i
                
        diff = score1 - score2
        if diff > max_diff:
            max_comb_cnt = cnt
            max_diff = diff
            
    if max_diff > 0:
        answer = [0]*11
        for n in max_comb_cnt:
            answer[10-n] = max_comb_cnt[n] 
        return answer 
    else:
        return [-1]
print(solution(5,	[2,1,1,1,0,0,0,0,0,0,0]))