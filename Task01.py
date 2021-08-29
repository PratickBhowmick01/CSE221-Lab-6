f = open("task1_input.txt", "r")
fp = open("task1_output.txt", "w") 

def LCS(s1,s2):
    x = [0]     #creating string-lists
    for str in s1:
        x.append(str)
    y = [0]
    for str in s2:
        y.append(str)      
    
    m,n = len(x), len(y)    
    #initializing n*m matrix 
    c = [[0 for i in range(m)] for j in range(n)]   #lcs
    t = [[None for i in range(m)] for j in range(n)]    #to track the seq
   
    for i in range(1,m):
        for j in range(1,n):
            if(x[i] == y[j]):
                c[i][j] = c[i-1][j-1] + 1
                t[i][j] = "D"
                
            elif(c[i-1][j] >= c[i][j-1]):
                c[i][j] = c[i-1][j] 
                t[i][j] = "U"
                
            else:
                c[i][j] = c[i][j-1]
                t[i][j] = "L"

    long = c[i][j]    
    correctedness = long*100 / len(s1)

    list = []
    t1 = t[i][j]
    while (t1 != None):

        if(t1 == "D"):
            list.append(j)  
            i,j = i-1, j-1
          
        elif(t1 == "U"):
            i -= 1
        else:
            j -= 1
            
        t1 = t[i][j]

    while(list != []):
        a = list.pop()
        if(x[a] == "Y"):
            fp.write("Yasnaya ") 
        elif(x[a] == "P"):
            fp.write("Pochinki ")
        elif(x[a] == "S"):
            fp.write("School ")
        elif(x[a] == "R"):
            fp.write("Rozhok ") 
        elif(x[a] == "F"):
            fp.write("Farm ")
        elif(x[a] == "M"):
            fp.write("Mylta ")
        elif(x[a] == "H"):
            fp.write("Shelter ")
        else:
            fp.write("Prison ")
    
    fp.write("\n")
    opt = "Correctness of prediction: {}%".format(correctedness)
    fp.write(opt) 
    
#input1
num = f.readline().strip()
seq = f.readline().strip()
pred = f.readline().strip()

LCS(seq, pred)

f.close() 
fp.close() 