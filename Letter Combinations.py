def combination(digit):
    if len(digit) ==0:
        return []
    digittoletter=[' ',' ','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    ans=[]
    def dfs(i,path):
        if i==len(digit):
            ans.append("".join(path))
            return 
        for letter in digittoletter[int(digit[i])]:
            path.append(letter)
            dfs(i+1,path)
            path.pop()
    dfs(0,[])
    print(len(ans))
    return ans
x=combination('234')
print(x)