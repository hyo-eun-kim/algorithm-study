# 금지된 단어를 제외한, 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자는 구분을 하지 않으며, 구두점또한 무시한다. 
import re
import collections

paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned =['hit']

# def mostCommonWord(paragraph, banned):

#     paragraph = re.sub('[.,]','',paragraph) # 구두점 삭제
#     paragraph = paragraph.lower().split() # 소문자로 바꾸고 띄어쓰기 단위로 띄어서 리스트로
#     paragraph = [word for word in paragraph if word not in banned]
#     #print(paragraph)

#     counts = collections.defaultdict(int)
#     for word in paragraph:
#         counts[word] +=1
#                                         # counts가 큰 값의 key 를 얻고 싶다.
#     return print(max(counts,key=counts.get))   # max 에 key를 지정해서 어떤값을 비교할지(?) 정해주는 느낌
# mostCommonWord(paragraph,banned)

def mostCommonWord1(paragraph, banned):

    paragraph = [word for word in re.sub(r'[^\w]',' ',paragraph) 
                    .lower().split()
                    if word not in banned] 
    #print(paragraph)

    counts = collections.Counter(paragraph)
    #return print(counts.most_common(1))   # 딕셔너리 형태로 return 하게 된다.
    return print(counts.most_common(1)[0][0])

mostCommonWord1(paragraph,banned)

