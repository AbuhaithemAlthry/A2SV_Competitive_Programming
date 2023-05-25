class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_five=0
        dic = defaultdict(int)
        for e in bills:
            if e==5:
                dic[e]+=1
            elif e == 10:
                if dic[5]:
                    dic[5]-=1
                    dic[10]+=1
                else:
                    return False
            elif e == 20:
                dic[20]+=1
                if dic[10]>0 and dic[5]>0:
                    dic[10]-=1
                    dic[5]-=1
                elif dic[5]>2:
                    dic[5]-=3
                else:
                    return False
        return True
                
                