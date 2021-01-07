# Code: Singly Linked-List using Python
# Date: 01/06/2021
# Author: Pranav H. Deo

# Class Node
class Node:
    def __init__(self, Data=None, Next=None):
        self.Data = Data
        self.Next = None


print('****** Singly Linked-List ******\n')
# Creating the Head Node:
head = Node()
p = head
q = head

while 1:
    print('\n> Operations : 0. Create Linked-List ; 1. Append Data ; 2. Add Data to Location ; '
          '3. Search Data ; 4. Delete Data ; 5. Display Linked-List ; 6. Exit')
    choice = int(input('# Enter Choice : '))

    if choice == 0:
        print('\n----- Choice : Create Linked-List -----')
        n = int(input('> Enter Nodes : '))
        # Creating the Nodes for the Linked-List:
        for i in range(0, n):
            if i == 0:
                dt = int(input('* Enter Data for Head Node : '))
                head.Data = dt
                head.Next = None
            else:
                dt = int(input('* Enter Data for Node ' + str(i + 1) + ' : '))
                new_Node = Node(dt, None)
                p.Next = new_Node
                p = new_Node

    # Appending Data to the Linked-List
    elif choice == 1:
        print('\n----- Choice : Append Data -----')
        dt = int(input('* Enter Data : '))
        addn_node = Node(dt, None)
        p = head
        while p.Next is not None:
            p = p.Next
        p.Next = addn_node

    # Adding Data to a given Location
    elif choice == 2:
        print('\n----- Choice : Add Data to Location -----')
        dt = int(input('* Enter Data : '))
        loc = int(input('* Enter Location : '))
        addn_node = Node(dt, None)
        p = head
        q = head
        flag = 0
        count = 0
        while q is not None:
            if loc == count and loc == 0:
                addn_node.Next = head
                head = addn_node
                p = head
                q = head
                flag = 1
                print('# ', dt, ' Inserted..')
                break
            elif loc == count and loc != 0:
                while p.Next != q:
                    p = p.Next
                addn_node.Next = q
                p.Next = addn_node
                p = head
                q = head
                flag = 1
                print('# ', dt, ' Inserted..')
                break
            else:
                count += 1
                q = q.Next
        if q is None and loc == count and flag == 0:
            while p.Next is not None:
                p = p.Next
            p.Next = addn_node
            p = head
            q = head
            flag = 1
            print('# ', dt, ' Inserted..')
        if flag == 0:
            print('# ', dt, ' Cannot be Inserted...')

    # Searching Data inside the Linked-List
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

    # Delete Data from the Linked-List
    elif choice == 4:
        print('\n----- Choice : Delete Data -----')
        dt = int(input('* Enter Data : '))
        p = head
        q = p.Next
        flag = 0
        while q is not None:
            if dt == head.Data:
                head = q
                p = head
                q = p.Next
                flag += 1
                print('# ', dt, ' Found and Deleted..')
            if q.Data == dt:
                while p.Next != q:
                    p = p.Next
                p.Next = q.Next
                q.Next = None
                flag += 1
                print('# ', dt, ' Found and Deleted..')
                q = p.Next
            else:
                q = q.Next
        if flag == 0:
            print('# ', dt, ' Not Found and Not Deleted..')

    # Displaying the Linked-List
    elif choice == 5:
        print('\n----- Choice : Display Linked-List -----')
        p = head
        while p is not None:
            print(p.Data, end='->')
            p = p.Next
        print('\n')

    else:
        break
