
#THIS ASSIGNMENT WAS DONE BY ONE PERSON
#NAME:Mahdi Afarideh
#Student Number:9731131


import gc
gc.disable()




class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class SinglyLinkedList:

    def __init__(self,limit):

        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None
        self.size=0
        self.limit=limit




    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        self.size+=1
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        if(self.size>self.limit):
            temp=self.head
            self.head=self.head.next
            self.remove(temp.data)
            self.size-=1

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node


def validBitChecker(cacheVaDiTa,  taIn):

    if (blsize_arch_ass[2] > 1):
        if (cacheVaDiTa[taIn[1]].size < 6 and cacheVaDiTa[taIn[1]].find([0,0,taIn[0]]==None)):
            return True

    else:
        return (cacheVaDiTa[taIn[1]][0] == 0 and cacheVaDiTa[taIn[1]][2] == -1)
    return False

def misschecker(cacheVaDiTa, taIn):
    if (blsize_arch_ass[2]>1):
        if (cacheVaDiTa[taIn[1]].find([1, 0, taIn[0]])==None): return True
        elif(cacheVaDiTa[taIn[1]].find([1, 1, taIn[0]]) == None):return True
    else:
        return (cacheVaDiTa[taIn[1]][2] != taIn[0] and cacheVaDiTa[taIn[1]][2]!=-1)

def wbFinisher():
    print("went inside webfinisher")
    if(blsize_arch_ass[2]==1):
     for i in range(len(d_iCacheVaDiTa[0])):
          if (d_iCacheVaDiTa[0][i][1] == 1): misCopRepFet[1] += int(blsize_arch_ass[0] / 4)
     for i in range(len(d_iCacheVaDiTa[1])):
          if (d_iCacheVaDiTa[1][i][1] == 1): misCopRepFet[1] += int(blsize_arch_ass[0] / 4)
    else:
         for i in range(len(d_iCacheVaDiTa[0])):
             cachelinkedlist=d_iCacheVaDiTa[0][i]
             current=cachelinkedlist.head
             while(current!=None):
                 if(current.data[1]==1):misCopRepFet[1] += int(blsize_arch_ass[0] / 4)
                 current=current.next
         for i in range(len(d_iCacheVaDiTa[1])):
             cachelinkedlist=d_iCacheVaDiTa[1][i]
             current=cachelinkedlist.head
             while(current!=None):
                 if(current.data[1]==1):misCopRepFet[1] += int(blsize_arch_ass[0] / 4)
                 current = current.next



def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def accessCalculator(requests,diAccesses):
    for i in range(len(requests)):
     if(requests[i][0]==0 or requests[i][0]==1 ):diAccesses[0]+=1
     elif(requests[i][0]==2 ):diAccesses[1]+=1

def blockFiller(cacheVaDiTa, taIn, readOrWrite,writemode):



    #read=0 and write=1


    if(not readOrWrite):
        #print("went inside not readorwrite in blockfiller")
        if(blsize_arch_ass[2]==1):
         cacheVaDiTa[taIn[1]][1] = 0

    if((readOrWrite)and(writemode=="wb")):
        #print("went inside wb in blockfiller")
        if (blsize_arch_ass[2] == 1):
         cacheVaDiTa[taIn[1]][1] = 1

    if(blsize_arch_ass[2] == 1):
     cacheVaDiTa[taIn[1]][0] = 1
     cacheVaDiTa[taIn[1]][2] = taIn[0]
     print("a block was field in " + str(taIn[1]) + "of cache with tag" + str(taIn[0]))
     print("the filled block is")
     print(cacheVaDiTa[taIn[1]])
    else:
     print("a block was field in set " + str(taIn[1]) + "of cache with tag" + str(taIn[0]))
     print("the filled block is")
     if((readOrWrite)and(writemode=="wb")):
        cacheVaDiTa[taIn[1]].append([1,1,taIn[0]])
        print([1,1,taIn[0]])
     else:
        cacheVaDiTa[taIn[1]].append([1,0,taIn[0]])
        print([1, 0, taIn[0]])


    #forIndex  cache[taInOf[1]][3] = taInOf[1]
    #forOffset  cache[taInOf[1]][4] = taInOf[2]


def cacheReader(cacheVaDiTa, request):
   #we do this to understand which block is the refrence going to since it is an address of a byte
    temp=request[1]//blsize_arch_ass[0]
    # tag index
    taIn=[0,0]
    taIn[1] = temp% len(cacheVaDiTa)
    taIn[0] = temp // len(cacheVaDiTa)

    #Wprint("inside cachewriter and the lenght of cache is" + str(len(cacheVaDiTa)))

    print("the tag is" + str(taIn[0]))
    print("the index is" + str(taIn[1]))

    if (validBitChecker(cacheVaDiTa,taIn) ):
        #print("a compulsary read miss has happended and valid bit is equal to "+str(cacheVaDiTa[taIn[1]][0]) +"and tag is equal to "+str(cacheVaDiTa[taIn[1]][2]))
        #print("for checking" + str(cacheVaDiTa[taIn[1]][2]) + " is not equal to " + str(taIn[0]))
        print("a compulsary read miss has happended ")
        if( request[0] == 0 ):misCopRepFet[0][0]+=1
        if(request[0] == 2 ):misCopRepFet[0][1]+=1

        misCopRepFet[3]+=1

        blockFiller(cacheVaDiTa, taIn, 0,wriAllMode[0])

    elif(misschecker(cacheVaDiTa,taIn)):

            #print("a non-compulsary read miss has happended and "+str(cacheVaDiTa[taIn[1]][2])+" is not equal to "+str(taIn[0]))
            print("a non-compulsary read miss has happended  ")


            if (request[0] == 0 ):
                misCopRepFet[0][0] += 1
                misCopRepFet[2][0] += 1
                print("a data replacement has accured in cachereader")
            elif(request[0] == 2 ):
                misCopRepFet[0][1] += 1
                misCopRepFet[2][1] += 1
                print("a instruction replacement has accured in cachereader")

            misCopRepFet[3] += 1

            if(blsize_arch_ass[2]>1):
                if (cacheVaDiTa[taIn[1]].head!=None and cacheVaDiTa[taIn[1]].head.data[1]==1 and wriAllMode[0] == "wb"):
                    misCopRepFet[1] += int(blsize_arch_ass[0] / 4)
                    print("a wb copy to memory has accured in cachereader")

            elif(cacheVaDiTa[taIn[1]][1]==1 and wriAllMode[0]=="wb"):
                misCopRepFet[1] += int(blsize_arch_ass[0] / 4)
                print("a wb copy to memory has accured in cachereader")

            blockFiller(cacheVaDiTa, taIn, 0,wriAllMode[0])
    else:
        #print("a non-compulsary read hit has happended and " + str(cacheVaDiTa[taIn[1]][2]) + " is  equal to " + str(taIn[0]))
        print("a non-compulsary read hit has happended " )



def cacheWriter(cacheVaDiTa, request):

    # we do this to understand which block is the refrence going to since it is an address of a byte
    temp = request[1] // blsize_arch_ass[0]
    # tag index
    taIn = [0, 0]
    taIn[1] = temp % len(cacheVaDiTa)
    taIn[0] = temp // len(cacheVaDiTa)

    #forOffset taIn[2]= requests[i][2]
    print("the tag is" + str(taIn[0]))
    print("the index is" + str(taIn[1]))
    #forOffset print("the offest is" + str(taIn[0]))
    if (request[0] == 0): print("the request kind is correct in cachewriter")

    if ( validBitChecker(cacheVaDiTa,taIn) ):
        #print("a non-compulsary write miss has happended and " + str(cacheVaDiTa[taIn[1]][2]) + " is not equal to " + str(taIn[0]))
        #print("for checking  valid bit is equal to " + str(cacheVaDiTa[taIn[1]][0]) + "and tag is equal to " + str(cacheVaDiTa[taIn[1]][2]))
        misCopRepFet[0][0] += 1

        if(wriAllMode[1]== "wa"):

            print("went inside wa in compulsary miss")
            if(wriAllMode[0]== "wt"):
                misCopRepFet[1]+=1
                print("the compulsary miss with wa is wt")

            else: print("the compulsary miss with wa is wb")
            misCopRepFet[3] += 1
            blockFiller(cacheVaDiTa, taIn, 1,wriAllMode[0])
        else:
            print("a compulsary write miss with na has happended and " + str(cacheVaDiTa[taIn[1]][2]) + " is not equal to " + str(taIn[0]))
            misCopRepFet[1]+=1
            misCopRepFet[3]=+1


    elif(misschecker(cacheVaDiTa,taIn)):


            #print("a non-compulsary write miss has happended and " + str(cacheVaDiTa[taIn[1]][2]) + " is not equal to " + str(taIn[0]))
            misCopRepFet[0][0] += 1
            if (wriAllMode[1] == "wa"):
                print("went inside wa in non-compulsary miss")

                if (wriAllMode[0] == "wt"):
                    misCopRepFet[1] += 1

                if (blsize_arch_ass[2] > 1):
                    if (cacheVaDiTa[taIn[1]].head[1] == 1 and wriAllMode[0] == "wb"):
                        misCopRepFet[1] += int(blsize_arch_ass[0] / 4)
                        print("a non compulsary wb miss has caused a replacement")


                elif (cacheVaDiTa[taIn[1]][1] == 1 and wriAllMode[0] == "wb"):
                    misCopRepFet[1] += int(blsize_arch_ass[0] / 4)
                    print("a non compulsary wb miss has caused a replacement")

                misCopRepFet[2][0] += 1

                misCopRepFet[3] += 1
                print("a write with replacment has aqquired has happended")
                blockFiller(cacheVaDiTa, taIn, 1,wriAllMode[0])

            else:
                print("a non-compulsary write miss with na has happended and " + str(
                cacheVaDiTa[taIn[1]][2]) + " is not equal to " + str(taIn[0]))
                misCopRepFet[1] += 1
                #misCopRepFet[3] += 1
    else:

     if (wriAllMode[0] == "wt"):
         misCopRepFet[1] += 1
         print("there is a wt hit")
     else:
      print("there is a wb hit")
      print("a  write hit has happended and " + str(cacheVaDiTa[taIn[1]][2]) + " is  equal to " + str(taIn[0]))

        #elif( cacheVaDiTa[taIn[1]][1]==1):misCopRepFet[1] += int(blsize_arch_ass[0]/ 4)

    """print("a write with replacment has aqquired has happended")
            misCopRe[2][0] += 1
            print("a replacement because of writinghas accured")"""




#inputFile=open("r6.trace","r")
#specLines=inputFile.read().splitlines()
cacheSpecs=input()

cacheSpecs=cacheSpecs.split(" - ")


blockSize=int(cacheSpecs[0])

cacheArch=int(cacheSpecs[1])

associativity=int(cacheSpecs[2])

#bloack size,computer architecture,associsation

blsize_arch_ass=[]
blsize_arch_ass.append(blockSize)
blsize_arch_ass.append(cacheArch)
blsize_arch_ass.append(associativity)

print("blsize_arch_ass is")
print(blsize_arch_ass)


writeMode=cacheSpecs[3]
print("the write mode is")
print(writeMode)

allocateMode=cacheSpecs[4]
print("the allocate mode is")
print(allocateMode)

wriAllMode=[]
wriAllMode.append(writeMode)
wriAllMode.append(allocateMode)
print("the writeall mode is")
print(wriAllMode)



cacheSize=[0,0]
line1=input()
if(blsize_arch_ass[1]==0):
    cacheSize=[int(line1)for i in cacheSize]
    cacheSize[1]=0
    cacheSize[0]=cacheSize[0]//blsize_arch_ass[2]
    print("the cache size are")
    print(cacheSize)


else:
    temp=line1.split(" - ")
    temp=[int(i)for i in temp]
    temp.reverse()
    cacheSize=temp
    cacheSize[0] = cacheSize[0] // blsize_arch_ass[2]
    cacheSize[1] = cacheSize[1] // blsize_arch_ass[2]
    print("the cache size are")
    print(cacheSize)




requests=[]
misCopRepFet=[[0, 0], 0, [0, 0],0]
diAccesses=[0,0]



lines=input()
while(lines!=""):
    tempString=lines
    tempArray=tempString.split(" ")
    tempArray=tempArray[0:2]
    print("the request is ")
    print(tempArray)
    tempArray[0]=int(tempArray[0])
    tempArray[1] = int(tempArray[1], 16)
    requests.append(tempArray)
    lines=input()


print(requests)
accessCalculator(requests,diAccesses)

#this array is for the two caches we are working witb
d_iCacheVaDiTa=[[], []]
#every block of d_iCacheVaDiTa[0] and d_iCacheVaDiTa[1] contains an array which is composed of [validbit,dirtybit,tag]

if(blsize_arch_ass[2]>1):
    for i in range(cacheSize[0]):
        #we use linked list becasue of lru replacment policy
        temp=SinglyLinkedList(blsize_arch_ass[2])
        d_iCacheVaDiTa[0].append(temp)
else:d_iCacheVaDiTa[0]=[[0, 0, -1] for i in range(cacheSize[0])]

print("the size of data cache is"+str(len(d_iCacheVaDiTa[0])))

if(blsize_arch_ass[2]>1):
    for i in range(cacheSize[1]):
        temp=SinglyLinkedList(blsize_arch_ass[2])
        d_iCacheVaDiTa[1].append(temp)
else:d_iCacheVaDiTa[1]=[[0, 0, -1] for i in range(cacheSize[1])]

print("the size of data cache is"+str(len(d_iCacheVaDiTa[1])))

flag=0

for i in range(len(requests)):

 #here we go through requests

 if(requests[i][0]==0):
     cacheReader(d_iCacheVaDiTa[0], requests[i])
     flag+=1
 if (requests[i][0] == 1):
     cacheWriter(d_iCacheVaDiTa[0] , requests[i])
     #print("flag is"+str(flag))
     flag += 1

 if(requests[i][0]==2):
     cacheReader((d_iCacheVaDiTa[1] if blsize_arch_ass[1]==1 else d_iCacheVaDiTa[0]),requests[i])
     flag += 1
 #print("the fetch is now"+str(misCopRepFet[3]))


print("the dcahce is")
for i in range(len(d_iCacheVaDiTa[0])):
 print(d_iCacheVaDiTa[0][i])
 print("                  ")
 print("                  ")
 print("                  ")
 print("                  ")



if(wriAllMode[0]=="wb"):
    wbFinisher()




print("***CACHE SETTINGS***")
if(cacheArch==0):print("Unified I- D-cache")
else:print("Split I- D-cache")
if(cacheArch==1):
    print("I-cache size: "+str(cacheSize[0]))
    print("D-cache size: "+str(cacheSize[1]))
else:print("Size: "+str(cacheSize[0]))
print("Associativity: "+str(associativity))
print("Block size: "+str(blockSize))
if(writeMode=="wb"):
    print("Write policy: WRITE BACK")
else:print("Write policy: WRITE THROUGH")
if(allocateMode=="wa"):
    print("Allocation policy: WRITE ALLOCATE")
else:print("Allocation policy: WRITE NO ALLOCATE")
print("")
print("***CACHE STATISTICS***")

print("INSTRUCTIONS")
print("accesses: "+str(diAccesses[1]))
print("misses: " + str(misCopRepFet[0][1]))


missrate=truncate(round(misCopRepFet[0][1] / (diAccesses[1] if diAccesses[1]  else 1), 4), 4)

print("miss rate: "+str(missrate)+" (hit rate "+str(truncate(0.0,4) if not diAccesses[1] else truncate(1-float(missrate),4 ))+")")
print("replace: " + str(misCopRepFet[2][1]))

print("DATA")
print("accesses: "+str(diAccesses[0]))
print("misses: " + str(misCopRepFet[0][0]))

missrate=truncate(round(misCopRepFet[0][0] / (diAccesses[0] if diAccesses[0]  else 1), 4), 4)

print("miss rate: "+str(missrate)+" (hit rate "+str(truncate(0.0,4) if not diAccesses[0] else truncate(1-float(missrate),4 ))+")")
print("replace: " + str(misCopRepFet[2][0]))

print("TRAFFIC (in words)")
if(wriAllMode[1]=="wa"):
 print("demand fetch: " + str(int(blsize_arch_ass[0]/ 4)*(misCopRepFet[0][0]+misCopRepFet[0][1])))
 #elif(wriAllMode[0]=="wt"):print("demand fetch: " + str((misCopRepFet[0][0]+misCopRepFet[0][1])))
else:print("demand fetch: " + str(int(blsize_arch_ass[0]/ 4)*misCopRepFet[3]))
print("copies back: " + str( misCopRepFet[1]))


#THIS ASSIGNMENT WAS DONE BY ONE PERSON
#NAME:Mahdi Afarideh
#Student Number:9731131

























