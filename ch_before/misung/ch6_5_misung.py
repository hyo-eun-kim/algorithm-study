# 문자열 배열을 입력받아 애너그램 단위로 그룹핑
# idea : 정렬해서 비교하자. 
import collections
strs = ['eat','tea','tan','ate','nat','bat']

def groupAnagrams(strs):

    anagrams = collections.defaultdict(list)    # 존재하지 않는 키를 삽입하려고 할때 에러가 나지 않음...
                                                # list 로 지정하지 않으면 error...

    for i in strs:
        anagrams[''.join(sorted(i))].append(i)   # 문자열은 .sort() 안됨. 왜냐 문자열은 바뀔수 없는 애니까
                                                 # sorted 는 list 형태로 return 해주기 때문에 , join이 필요하다.
    
    return print(anagrams.values())

groupAnagrams(strs)
