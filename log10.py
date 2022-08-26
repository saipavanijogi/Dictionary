a = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
s=0
for i,j in a.items():
    s=s+len(j)
print(s)

