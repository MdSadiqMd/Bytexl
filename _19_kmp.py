def kmp(pat,txt):
    m=len(pat)
    n=len(txt)
    lps=[0]*m