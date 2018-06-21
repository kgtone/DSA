def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    l=[]
    i=0
    t=''
    while i<len(strs[0]):
        t=strs[0][i]
        flag=True
        for n in strs:
            print(n[i])
            if t!=n[i] or i>=len(n):
                flag=False
        if flag==True:
            l.append(t)
        else:
            break
        i+=1
    return l
strs=['Hala','Hello']
print(longestCommonPrefix(strs))