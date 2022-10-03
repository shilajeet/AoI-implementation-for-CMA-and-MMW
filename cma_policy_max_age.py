import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#Number of users
N=2000;

# Dimension of the grid network (row (m) x column (n)) number of cells in the network
m=10;                  
n=10;

#Total number of cells in the network
M=m*n;

# Number of Monte Carlo simulations
Monte_Carlo=1;
print("The below simulation results are for ",Monte_Carlo," simulations");

user=np.arange(0,N);
cells=np.arange(0,M);

print("The number of users is:",N);
print("The number of cells is:",m*n);

#Vectors to store user cell number and user age
user_cell=np.zeros((1,N));


# Number of slots
slots=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,100,1000,2000,4000];
slotno=0;

#Array to store the total age of all the users till the end of time horizon
final_age=[];

#Creating channel probability distribution for all the users which will remain fixed throughout the simulation duration
probability=np.zeros((1,N));
for i in range(0,N):
     probability[0,i]=np.random.uniform(0,1);
     
for slotno in range(0,len(slots)):
     
     #this variable stores the sum of ages of all the users till the end of the time horizon
     sum_age_2=0;
     
     for iterate in range(0,Monte_Carlo):
          
          #Vector to store the ages of the users at a particular time, so it updates itself during each time slot
          user_age=np.ones((1,N));
          
          #Variable to store the sum of ages of the users at a particular time slot
          sum_age=0;
          
          for time in range(0,slots[slotno]):
               
               if(time==0):
                    
                    for i in range(0,N):
                         user_cell[0,i]=np.random.randint(0,M);
                         
               if(time>0):
                    
                    for i in range(0,N):
                         if(user_cell[0,i]==0):
                              moves=[1,n];
                              user_cell[0,i]=np.random.choice(moves);
                              
                         elif(user_cell[0,i]==n-1):
                              moves=[n+(n-1),n-2];
                              user_cell[0,i]=np.random.choice(moves);
                              
                         elif(user_cell[0,i]==(m-1)*n):
                              moves=[user_cell[0,i]-n,user_cell[0,i]+1];
                              user_cell[0,i]=np.random.choice(moves);
                              
                         elif(user_cell[0,i]==m*n-1):
                              moves=[user_cell[0,i]-n,user_cell[0,i]-1];
                              user_cell[0,i]=np.random.choice(moves);
                              
                         elif(user_cell[0,i]>0 and user_cell[0,i]<n-1):  
                              moves=[user_cell[0,i]+1,user_cell[0,i]-1,user_cell[0,i]+n];
                              user_cell[0,i]=np.random.choice(moves);
                              
                         elif(user_cell[0,i]>(m-1)*n and user_cell[0,i]<m*n-1): 
                              moves=[user_cell[0,i]+1,user_cell[0,i]-1,user_cell[0,i]-n];
                              user_cell[0,i]=np.random.choice(moves);
                              
                         elif(user_cell[0,i]%n==0 and i!=0 and i!=(m-1)*n):
                              moves=[user_cell[0,i]+n,user_cell[0,i]+1,user_cell[0,i]-n];
                              user_cell[0,i]=np.random.choice(moves);
                              
                         elif( (user_cell[0,i]+1)%n==0 and (user_cell[0,i]!=(n-1) or user_cell[0,i]!=m*n-1) ):
                              moves=[user_cell[0,i]-n,user_cell[0,i]-1,user_cell[0,i]+n];
                              user_cell[0,i]=np.random.choice(moves);
                              
                         else: 
                              moves=[user_cell[0,i]+1,user_cell[0,i]-1,user_cell[0,i]+n,user_cell[0,i]-n];
                              user_cell[0,i]=np.random.choice(moves);
                              
               for i in range(0,M):
                    same_cell_user=[];
                    same_cell_user_age=[];
                    
                    for j in range(0,N):
                         if(user_cell[0,j]==i):
                              same_cell_user.append(j);
                    
                    for j in range(0,len(same_cell_user)):
                         same_cell_user_age.append(user_age[0,same_cell_user[j]]);
                         
                    if(time==0 and len(same_cell_user)!=0):
                         
                         max_user=np.argmax(same_cell_user_age);
                         sendto=same_cell_user[max_user];
                         toss=np.random.binomial(1,probability[0,sendto]);
                         
                         if(toss==1):
                              user_age[0,sendto]=1;
                              for i1 in range(0,len(same_cell_user)):
                                   if(i1!=sendto):
                                        user_age[0,same_cell_user[i1]]=user_age[0,same_cell_user[i1]]+1;
                                        
                         if(toss==0):
                              for i1 in range(0,len(same_cell_user)):
                                   user_age[0,same_cell_user[i1]]=user_age[0,same_cell_user[i1]]+1;
                                   
                    if(time>0 and len(same_cell_user)!=0):
                         
                         max_user=np.argmax(same_cell_user_age);
                         sendto=same_cell_user[max_user];
                         toss=np.random.binomial(1,probability[0,sendto]);
                         
                         if(toss==1):
                              user_age[0,sendto]=1;
                              for i2 in range(0,len(same_cell_user)):
                                   if(i2!=sendto):
                                        user_age[0,same_cell_user[i2]]=user_age[0,same_cell_user[i2]]+1;
                                        
                         if(toss==0):
                              for i2 in range(0,len(same_cell_user)):
                                   user_age[0,same_cell_user[i2]]=user_age[0,same_cell_user[i2]]+1;
                        
               sum_age=sum_age+np.max(user_age);
                                             
          sum_age_2=sum_age_2+sum_age;
          
     final_age.append(sum_age_2/(Monte_Carlo*slots[slotno]));
     
# =============================================================================
# #Generating the universal lower bound for cost of any online policy
# #The universal lower bound has been given in the paper at page number 10
# sum_1=0; #Variable stores the 1/sqrt(p_i) sum over all users
# 
# for i in range(0,len(np.transpose(probability))):
#      sum_1=sum_1+(np.sqrt(1/probability[0,i]));
#      
# sum_2=math.pow(sum_1,2);
# 
# sum_3=sum_2/(2*M*N);
# sum_3=sum_3+0.5;
# 
# #List stores the lower bound for all time slots(since the lower bound is constant over all time so the list will store a constant value for all it's elements)
# constant_list=[];
# 
# for i in range(0,len(slots)):
#      constant_list.append(sum_3);
# =============================================================================
     
#Generate plots     
plt.xlabel("simulation duration(in slots)",color='blue');
plt.ylabel("Time-averaged Peak AoI(in slots)",color='blue');
plt.plot(slots,final_age,linestyle='--',color='red',linewidth=2);
# =============================================================================
# plt.plot(slots,constant_list,linestyle='-.',color='orange',linewidth=2);
# =============================================================================
plt.title("Time averaged Peak AoI for CMA policy for N=2000 users located in M=100 cells",color='magenta');
plt.grid(True,alpha=0.8);
plt.show();

#Generate .csv files for the data
resultsdf=pd.DataFrame({"time slots":slots,"time averaged peak AoI per user":final_age});
resultsdf.to_csv("Results of CMA policy for N=2000 users for peak AoI case"); 

          

                 
                         
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                        
                                        
                         
                         
                         
                         
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                         
                  
                         