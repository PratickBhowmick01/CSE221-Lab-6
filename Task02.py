f = open("task2_input.txt", "r")
fp = open("task2_output.txt", "w") 
                     
def LCS(s1,s2,s3):

    x = [0]     #creating string-lists
    for char in s1:
        x.append(char)
    y = [0]
    for char in s2:
        y.append(char)   
    z = [0]
    for char in s3:
        z.append(char) 
    m,n,o = len(x), len(y), len(z) 

    #initializing n*m matrix 
    c = [[[0 for i in range(o)] for j in range(n)]for k in range(m)]    
    t = [[[None for i in range(o)] for j in range(n)]for k in range(m)]   
    
    for i in range(m):
        for j in range(n):
            for k in range(o): 
                if (i == 0 or j == 0 or k == 0):
                    c[i][j][k] = 0
                    t[i][j][k] = None
                
                else:
                    if(x[i-1] == y[j-1] and x[i-1] == z[k-1]):
                        c[i][j][k] = c[i-1][j-1][k-1] + 1
                        t[i][j][k] = "D"
                        
                    else:
                        if(c[i-1][j][k] >= c[i][j-1][k]):
                            max = c[i-1][j][k]
                            if(max >= c[i][j][k-1]):
                                c[i][j][k] = max
                                t[i][j][k] = "UUL"
                            
                            else:
                                max = c[i][j][k-1]
                                c[i][j][k] = max
                                t[i][j][k] = "LUU"
                          
                        else:
                            max = c[i][j-1][k]
                            if (max >= c[i][j][k-1]):
                                c[i][j][k] = max
                                t[i][j][k] = "ULU"
                            else:
                                max = c[i][j][k-1]
                                c[i][j][k] = max
                                t[i][j][k] = "LUU" 

    fp.write(str(c[i][j][k]))
    fp.write("\n")

#input1
x1 = f.readline().strip()
y1 = f.readline().strip()
z1 = f.readline().strip()
LCS(x1,y1,z1)

#input2
x2 = f.readline().strip()
y2 = f.readline().strip()
z2 = f.readline().strip()
LCS(x2,y2,z2)

f.close() 
fp.close() 
