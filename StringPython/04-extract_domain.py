data = 'hasdadouahndias@prc.ac.th ybalasjdahoisda'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)