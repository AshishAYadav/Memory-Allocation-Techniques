########################################## Memory Allocation - Python 3.6 #############################################################
#Hosted on GitHub																													  #
#Author: Ashish Yadav         <Email>:<ash24aniy@gmail.com>																			  #
#linkedIn <https://in.linkedin.com/in/ashishayadav>																					  #
#Version: 1.0																														  #
#Python:3.6																															  #
#Description: This program is to just demonstrate the implementation of the 3 different memory allocation techniques that are being   #
#used for allocating processes to static memory blocks. This program uses algorithms which are available under GNU public license for # #educational purpose use. 																											  #
#																																	  #
#######################################################################################################################################
class memory_allocation:
    def create_instance_memory_blocks(self,l):
#"""Display Memory to be allocated"""
        self.i=0
        self.block=l
        self.pdict ={}
        for self.y in self.block:
            print("Memory block :{0} | Size: {1}".format(self.i,self.y))
            self.i+=1
            self.pdict[self.y]=0
        print("Total {0} Memory blocks Created!".format(self.i))

    def process_to_be_allocated(self,list):
#	"""Display Processes to be allocated"""
        self.total_processlist=list
        print()
        self.i=0
        self.bdict={}
        for self.x in self.total_processlist:
            print("Process :{0} | Size: {1}".format(self.i,self.x))
            self.bdict[self.x]=0
            self.i+=1
        print("Total {0} Processes needs to be allocated".format(self.i))
        
    def first_fit(self):
#	"""First fit algorithm"""
        print()
        print("Using First Fit Algorithm")
        self.i=0
        for self.x in self.total_processlist:
            self.j=0
            for self.y in self.block:
                if (self.x <= self.y) and (self.pdict[self.y]!=1):
                    self.pdict[self.y]=1
                    self.bdict[self.x]=1
                    print("Process :{0} |Size :{1} allocated into Memory block :{2} |Size :{3}".format(self.i,self.x,self.j,self.y))
                    break
                self.j+=1
            self.i+=1

    def worst_fit(self):
	#	"""Worst fit algorithm"""
        print()
        print("Using worst Fit Algorithm")
        self.i=0
        for self.x in self.total_processlist:
            self.j=0
            for self.y in self.block:
                if (self.x <= self.y) and (self.pdict[self.y]!=1):
                    if(self.isbiggest(self.y)):
                        self.pdict[self.y]=1
                        self.bdict[self.x]=1
                        print("Process :{0} |Size :{1} allocated into Memory block :{2} |Size :{3}".format(self.i,self.x,self.j,self.y))
                        break
                self.j+=1
            self.i+=1
    def best_fit(self):
		#"""Best fit algorithm"""
        print()
        print("Using best Fit Algorithm")
        self.i=0
        for self.x in self.total_processlist:
            self.j=0
            for self.y in self.block:
                if (self.x <= self.y) and (self.pdict[self.y]!=1):
                    if(self.issmallest(self.y)):
                        self.pdict[self.y]=1
                        self.bdict[self.x]=1
                        print("Process :{0} |Size :{1} allocated into Memory block :{2} |Size :{3}".format(self.i,self.x,self.j,self.y))
                        break
                self.j+=1
            self.i+=1

    def issmallest(self,x1):
	#	"""Determine the smallest unallocated memory block for process to be allocated"""
        self.flag =True
        self.x1=x1
        for self.y1 in self.block:
            if self.y1<self.x1 and self.pdict[self.y1]!=1 and self.y1>=self.x:
                self.flag=False
        return self.flag

    def isbiggest(self,x1):
	#	"""Determine the biggest unallocated memory block for process to be allocated"""
        self.flag =True
        self.x1=x1
        for self.y1 in self.block:
            if self.y1>self.x1 and self.pdict[self.y1]!=1:
                self.flag=False
        return self.flag
    
    def unallocated_processes(self):
	#"""This Method determines processes which are not allocated to the memory blocks"""
            print()
            self.i=0
            for self.x in self.total_processlist:
                if (self.bdict[self.x]!=1):
                    print("Process :{0} |Size :{1} Unallocated! ".format(self.i,self.x))
                self.i+=1
    def unallocated_blocks(self):
	#"""This Method determines Memory blocks which are free"""
            print()
            self.j=0
            for self.y in self.block:
                if (self.pdict[self.y]!=1):
                    print("Memory block :{0} |Size :{1} Empty! ".format(self.j,self.y))
                self.j+=1
    def memory_utilization(self):
	#"""This Method calculates the percentage memory used!"""
        self.total = 0
        self.sum=0
        for self.z in self.total_processlist:
            if self.bdict[self.z]!=0:
                self.sum = self.sum + self.z
        for self.z in self.block:
            self.total = self.total + self.z
        print("Total Memory Utilization = {0:.2f}%".format(self.sum*100/self.total))
            
            
# Call the functions from main 
#take input in list    
#you can create multiple instances as many you want        
if __name__ == '__main__':
    bl = [100,500,200,300,600]
    pl = [212,417,112,426]
    print("First Fit Instance")
    obj = memory_allocation()    
    obj.create_instance_memory_blocks(bl)
    obj.process_to_be_allocated(pl)
    obj.first_fit()
    obj.unallocated_processes()
    obj.unallocated_blocks()
    obj.memory_utilization()
    print()
    print("Worst Fit Instance")
    obj1 = memory_allocation()    
    obj1.create_instance_memory_blocks(bl)
    obj1.process_to_be_allocated(pl)
    obj1.worst_fit()
    obj1.unallocated_processes()
    obj1.unallocated_blocks()
    obj1.memory_utilization()
    print()
    print("Best Fit Instance")
    obj2 = memory_allocation()    
    obj2.create_instance_memory_blocks(bl)
    obj2.process_to_be_allocated(pl)
    obj2.best_fit()
    obj2.unallocated_processes()
    obj2.unallocated_blocks()
    obj2.memory_utilization()
