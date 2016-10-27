from linked_list import LinkedList



if __name__=="__main__":
    mylist=LinkedList()
    mylist.insert(4)
    mylist.insert(5)

    mylist.print_list()
    #mylist.recursive_reverse(mylist.head)
    print "\n"
    mylist.iterative_reverse()
    mylist.print_list()