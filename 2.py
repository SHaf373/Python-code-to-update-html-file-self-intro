def reader():
    f=open('scores.txt','r')
    firstname=''
    lastname=''
    score=''
    
    topper=''
    looser=''
    maxim=0
    minim=100
    counter=0
    accum=0
    line=f.readline()
    while(line !=''):
        firstname , lastname , score= line.split()
        counter+=1
        score=(int)(score)
        accum+=score

        if(score>maxim):
            maxim=score
            topper=firstname+" "+lastname
        if (score<minim):
            minim=score
            looser=firstname+" "+lastname
        
        line=f.readline()
    f.close()

    print('toper:',topper,'with',maxim,'marks')
    print('looser:',looser,'with',minim,'marks')
    avg=accum/counter
    print('the class average:',avg)
reader()
