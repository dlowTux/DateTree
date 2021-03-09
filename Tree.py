class Search:
    def Convert(self,number):
        try:
            return int(number)
        except:
            return number
    def BinarySearch(self,array,objetive):
        for x in array:
            if str(x)==str(objetive):
                return True
        return False
    def Searching(self,array,objetive):
        if array[0]=='/':
            if objetive=='/':
                return True
            else:
                return False
        else:
            return self.BinarySearch(array,self.Convert(objetive))

class Node:
    def __init__(self,data,tokens):
        self.left=None
        self.right=None
        self.data=data
        self.tokens=tokens


class Tree:
    def __init__(self):
        self.root=None

    def insert(self,leaf,data,tokens):
        if leaf==None:
            leaf=Node(data,tokens)
        else:
            aux=leaf.data
            if data<aux:
                leaf.left=self.insert(leaf.left,data,tokens)
            else:
                leaf.right=self.insert(leaf.right,data,tokens)
        return leaf
    def PostOrder(self,leaf,objetive):
        if leaf==None:
            return False
        else:
            self.PostOrder(leaf.left,objetive)
            self.PostOrder(leaf.right,objetive)
            #Here is where we have to search
            if Search().Searching(leaf.tokens,objetive[0])==True:
                objetive.pop(0)
            else:
                return objetive
            if len(objetive)==0:
                return True
def Convert(number):
    try:
        int(number)
        return True
    except:
        return False
def HasBars(data):
    num_bars=0
    for  x in data:
        if x=='/':
            num_bars+=1
    return num_bars==2
def IsNotFake(data):
    if Convert(data[0:2]) ==True and  Convert(data[0:2]) ==True and  Convert(data[3:5])==True:
        if int(data[0:2])>29 and int(data[0:2])<31 and int(data[3:5])==2:
            return False
    else:
        return False
    return True

def is_not_blank(s):
    if bool(s and s.strip())==False:
        print('Empty String :(')
        return False
    else:
        if len(s)==10 and HasBars(s):
            if IsNotFake(s)==False:
                print('This date does not exist')
                return False
            return True
        else:
            print('Incorrect format the correct format must be AA/MM/YYYY')
            return False
    return True
def ErrorManagement(result):
    if len(result)==5:
        print('Error in the day')
    if len(result)==3:
        print('Error in the month')
    if len(result)==1:
        print('Error in the year')
thunk=Tree()
datas=[
        10,
        9,
        8,
        7,
        8.5
        ]
tokens=[
        [int(x) for x in range(2002,2021)],
        ['/'],
        [int(x) for x in range(1,13)],
        [int(x) for x in range(1,32)],
        ['/']
        ]
for x in range(len(datas)):
    thunk.root=thunk.insert(thunk.root,datas[x],tokens[x])

date=input('Write a date ')

if is_not_blank(date):
    result=thunk.PostOrder(
            thunk.root,
            [
                date[0:2],
                date[2:3],
                date[3:5],
                date[5:6],
                date[6:10]
                ]
            )
    if result==True:
        print('Correct')
    else:
        ErrorManagement(result)




