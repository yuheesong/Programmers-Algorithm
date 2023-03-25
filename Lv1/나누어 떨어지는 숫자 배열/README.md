# 알게된점  
## sort  vs  sorted 함수 비교  
<br/>
sort는 리스트의 원본을 수정하며 "리스트.sorted()"의 형식으로 사용한다.  
<br/><br/>
sorted는 리스트 원본은 그대로이고, 정렬한 값을 반환한다. "sorted(리스트명)"의 형식으로 사용한다.  
<br/><br/>  
예를 들어, 리스트 a=[4,3,5]를 오름차순 정렬하여 반환하고 싶을 때,  
sort -> return a.sort()를 한다.  
sorted -> b = sorted(a) 하여 return b를 한다.  
