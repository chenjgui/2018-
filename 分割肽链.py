#!/usr/bin/python
# A0M8Q6
K='P06702';
a="MTCKMSQLERNIETIINTFHQYSVKLGHPDTLNQGEFKELVRKDLQNFLKKENKNEKVIEHIMEDLDTNADKQLSFEEFIMLMARLTWASHEKMHEGDEGPGHHHKPGLGEGTPXXX"
sequence=list(a);
for i in range(len(a)):
    if sequence[i] == 'K':
        print("'"+sequence[i-11]+sequence[i-10]+sequence[i-9]+sequence[i-8]+sequence[i-7]+
        	sequence[i-6]+sequence[i-5]+sequence[i-4]+sequence[i-3]+sequence[i-2]+sequence[i-1]+
        	sequence[i]+sequence[i+1]+sequence[i+2]+sequence[i+3]+sequence[i+4]+sequence[i+5]+
        	sequence[i+6]+sequence[i+7]+sequence[i+8]+sequence[i+9]+sequence[i+10]+
        	sequence[i+11]+"'",i+1,K)
        #print('\n')
        #print(i)
