# Code: Doubly Linked-List using Python
# Date: 01/09/2021
# Author: Pranav H. Deo

# Class Node
class Node:
    def __init__(self, Data=None, Next=None, Prev=None):
        self.Data = Data
        self.Next = Next
        self.Prev = Prev


print('****** Doubly Linked-List ******\n')
# Creating the Head Node:
head = Node()
p = head

while 1:
    print('\n> DLL Operations : 0. Create Linked-List ; 1. Append Data ; 2. Add Data to Location ; '
          '3. Search Data ; 4. Delete Data ; 5. Display Linked-List ; 6. Exit')
    choice = int(input('# Enter Choice : '))

    if choice == 0:
        print('\n----- Choice : Create DLL -----')
        n = int(input('> Enter Nodes : '))
        # Creating the Nodes for the DLL:
        for i in range(0, n):
            if i == 0:
                dt = int(input('* Enter Data for Head Node : '))
                head.Data = dt
                head.Prev = None
                head.Next = None
            else:
                dt = int(input('* Enter Data for Node ' + str(i + 1) + ' : '))
                new_Node = Node(dt, None, None)
                p.Next = new_Node
                new_Node.Prev = p
                p = p.Next

    elif choice == 1:
        print('\n----- Choice : Append Data -----')
        dt = int(input('* Enter Data : '))
        new_Node = Node(dt, None, None)
        p = head
        while p.Next is not None:
            p = p.Next
        p.Next = new_Node
        new_Node.Prev = p

    elif choice == 2:
        print('\n----- Choice : Add Data to Location -----')
        dt = int(input('* Enter Data : '))
        loc = int(input('* Enter Location : '))
        count = 0
        flag = 0
        p = head
        while p is not None:
            if loc == count and loc == 0:
                new_Node = Node(dt, head, None)
                head = new_Node
                p = head
                flag = 1
                print('# ', dt, ' Inserted..')
                break
            elif loc == count and loc != 0:
                new_Node = Node(dt, None, None)
                new_Node.Next = p
                new_Node.Prev = p.Prev
                p.Prev.Next = new_Node
                p.Prev = new_Node
                flag = 1
                print('# ', dt, ' Inserted..')
                break
            else:
                count += 1
                p = p.Next
        if p is None and loc == count and flag == 0:
            new_Node = Node(dt, None, None)
            p = head
            while p.Next is not None:
                p = p.Next
            p.Next = new_Node
            p = head
            flag = 1
            print('# ', dt, ' Inserted..')
        if flag == 0:
            print('# ', dt, ' Cannot be Inserted...')

    elif choice == 3:
        print('\n----- Choice : Search Data -----')
        dt = int(input('* Enter Data : '))
        p = head
        flag = 0
        while p is not None:
            if p.Data == dt:
                print('# ', dt, ' Found..')
                flag = 1
                break
            else:
                p = p.Next
        if flag == 0:
            print('# ', dt, ' Not Found..')

    elif choice == 4:
        print('\n----- Choice : Delete Data -----')
        dt = int(input('* Enter Data : '))
        p = head
        flag = 0
        while p is not None:
            if p.Data == dt and p == head:
                head = p.Next
                head.Prev = None
                p = head
                flag += 1
                print('# ', dt, ' Found and Deleted..')
            elif p.Data == dt and p != head:
                p.Prev.Next = p.Next
                p.Next.Prev = p.Prev
                p.Next = None
                p.Prev = None
                p = head
                flag += 1
                print('# ', dt, ' Found and Deleted..')
            else:
                p = p.Next
        if p is None and flag == 0:
            print('# ', dt, ' Not Found and Not Deleted..')

    elif choice == 5:
        print('\n----- Choice : Display DLL -----')
        ch = input('> 1. Normal Display ; 2. Reverse Display : ')
        p = head
        if ch == '1':
            while p is not None:
                print(p.Data, end='<->')
                p = p.Next
            print('\n')
        else:
            while p.Next is not None:
                p = p.Next
            while p is not None:
                print(p.Data, end='<->')
                p = p.Prev
            print('\n')

    else:
        break
