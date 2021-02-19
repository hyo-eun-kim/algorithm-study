# UTF-8 검증
# 입력값이 utf-8 문자열이 맞는지 확인하라.

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def check(size): # 문자 바이트 만큼 10으로 시작
            for i in range(start+1, start+size+1):
                if i>=len(data) or (data[i]>>6) !=0b10: # data 의 시작이 10이 아니면 false +(size만큼 데이터가 없어도 false)
                    return False
            return True 
        
        start =0

        while start < len(data):
            first=data[start]
            if(first>>3 ) ==0b11110 and check(3):
                start +=4
            elif(first >>4) ==0b1110 and check(2):
                start +=3
            elif (first >>5) ==0b110 and check(1):
                start +=2 
            elif(first >>7) ==0:  # 1바이트 체크
                start +=1
            else :
                return False

        return True