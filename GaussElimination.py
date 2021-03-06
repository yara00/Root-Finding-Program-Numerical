import numpy as np
import time
def gauss_pivot(A,f,numberofunknowns,noofdecimal):
    startTime=time.time()
    l=f.reshape(-1,1)
    Aug=np.append(A,l,axis=1) 
    print(Aug)
    
    noofdecimal=int(noofdecimal)
    
    rankA = np.linalg.matrix_rank(A) 
    rankAug=np.linalg.matrix_rank(Aug) 
    n = len(f)
    
    if(rankA!=rankAug):
        return(1,"System is inconsistent and there is no solution")
    elif(rankA==rankAug<numberofunknowns):
        return(1,"system has infinite number of solution")
    else:
        for i in range(int(0),int(n-1)):     # Loop through the columns of the matrix
            maxelement=max(A[:,i],key=abs)  #max element in col#i
            if (A[i,i])!=maxelement: #max element of col #i is not the one in the diagonal,pivoting is needed
                for k in range(i+1,n):
                    if np.abs(A[k,i])>np.abs(A[i,i]):
                        A[[i,k]]=A[[k,i]]             # Swaps ith and kth rows to each other
                        f[[i,k]]=f[[k,i]] 
                    
             #now elimination    
            for j in range(i+1,n):     # Loop through rows below diagonal for each column
                m = A[j,i]/A[i,i]      #get the multiply
                roundm=round(m,noofdecimal)
                A[j,:] =A[j,:] - roundm*A[i,:]
                f[j] = f[j] - roundm*f[i]
           
        return Back_Subs(A,f,noofdecimal,startTime) 
def Back_Subs(A,f,noofdecimal,startTime):
    
    
    n = f.size
    x = np.zeros(n)             # Initialize the solution vector, x, to zero
    x[n-1] = round(f[n-1]/A[n-1,n-1],noofdecimal)    # Solve for last entry first
    
    for i in range(n-2,-1,-1):      # Loop from the end to the beginning
        sum_ = 0
        for j in range(i+1,n):         
            sum_ = round(sum_ + A[i,j]*x[j],noofdecimal)
        x[i] = round((f[i] - sum_)/A[i,i],noofdecimal)  
    end = time.time()    
    runtime = end - startTime
    return 0,x,A,runtime
