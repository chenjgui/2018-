# 'A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','X'
sequence=(
'XXXXXXXXXXGKITFYEDRGFQG'
'XXASDHQTQAGKPQPLNPKIIIF'
'PCPNLKETGVEKAGSVLVQAGPW'
'GPWVGYEQANCKGEQFVFEKGEY'
'ANCKGEQFVFEKGEYPRWDSWTS'
'RTDSLSSLRPIKVDSQEHKITLY'
'LRPIKVDSQEHKITLYENPNFTG'
	)
# 1
count=0
iteri=1
for i in sequence:
    dic={"A":"1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ","R":"0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ","N":"0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ","D":"0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ","C":"0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ","X":"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ",
        "Q":"0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ","E":"0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ","G":"0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ","H":"0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ","I":"0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ",
        "L":"0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 ","K":"0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 ","M":"0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ","F":"0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 ","P":"0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 ",
        "S":"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 ","T":"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 ","W":"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 ","Y":"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ","V":"0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 ",}
    count=count+1

    if count <=23*iteri:
        print(dic[i],end='')
#print('\n')
#print(iteri)
print('\n')