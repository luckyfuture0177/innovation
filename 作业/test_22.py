'''两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
程序源代码：'''
one = ['a','b','c']
two = ['x','y','z']
i = 0
j = 0
for q in two:
    if q != 'x':
        for w in two:
            if w !='x' and w != 'z' and w !=q :
                for e in two:
                    if e != q and e != w:
                        print('a---%c\tb---%c\tc---%c'%(q,e,w))

