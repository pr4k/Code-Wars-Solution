'''Complete the  function `scramble(str1, str2)` that returns `true` if a portion of ```str1``` characters can be rearranged to match ```str2```, otherwise returns ```false```.

**Notes:**
* Only lower case letters will be used (a-z). No punctuation or digits will be included.
* Performance needs to be considered

```c
Input strings s1 and s2 are null terminated.
```

## Examples

```python
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
```'''
from collections import Counter
def scramble(s1, s2):
    a=Counter(list(s1))
    b=Counter(list(s2))
    print(b.keys(),a.keys())
    try:
        c=list(a.keys())
        s=list(b.keys())
        for i in s:
            print(0)
            c.remove(i)
        for i in s:
            if a[i]-b[i]<0:
                print (a[i],b[i])
                raise ValueError()
        return True
        
    except:
        return False
        
''''
    list(s1)
    b=list(s2)
    [b.remove(x) for x in a if x in b]
    if len(b)==0:
        return True
    else: return False
    for i in s2:
        if i in a:
            a.remove(i)
        else:
            return False
    return True'''