class Node:
  def __init__(self, data, nextNode=None):
    self.data = data
    self.nextNode = None

choice = 1
dt = int(input("Enter the value for the root node : "))
Head = Node(dt)
Head.nextNode = None

while(choice!=0):

  choice = int(input("\n\n####Enter operation : 0.Exit ; 1.Append Node; 2.Add Node at Pos ; 3.Delete Node ; 4.Display LinkedList : "))
  
  if(choice==0):
    break;

  elif(choice==1):
    p = Head
    while(p.nextNode!=None):
      p = p.nextNode
    num = int(input(">Enter the number of nodes to add : "))
    while(num!=0):
      dt = int(input(">Enter the value for the node : "))
      q = Node(dt)
      q.nextNode = None
      p.nextNode = q
      p = q
      num-=1

  elif(choice==2):
    pos = int(input(">Enter the Position : "))
    dt = int(input(">Enter the value of the Node : "))
    p = Head
    count = 0
    while(count!=pos-1):
      p = p.nextNode
      count+=1
    q = Node(dt)
    q.nextNode = p.nextNode
    p.nextNode = q

  elif(choice==3):
    flag=0
    dt = int(input(">Enter the Data to Delete : "))
    p = Head
    q = p.nextNode
    while(q.data!=dt):
      q = q.nextNode
      if(q.nextNode==None):
        flag=1
        break
      p = p.nextNode
    if(flag==0):
      p.nextNode = q.nextNode
      q.nextNode = None
    else:
      print("Data Not Present")
    

  elif(choice==4):
    p = Head
    while(p!=None):
      print(p.data,",", end='')
      p = p.nextNode
