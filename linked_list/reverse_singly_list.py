from linked_list import LinkedList

if __name__=="__main__":
    mylist=LinkedList()
    mylist.insert(4)
    mylist.insert(5)
    mylist.insert(67)
    mylist.insert(45)
    mylist.insert(11)
    mylist.insert(3)
    mylist.print_list()
    mylist.delete(45)
    mylist.print_list()
    mylist.delete(3)
    mylist.print_list()
    print "\n"
    mylist.delete(4)
    mylist.print_list()
    mylist.delete(11)
    mylist.print_list()
    mylist.delete(5)
    mylist.print_list()
    print "\n"
    mylist.delete(6)
    mylist.print_list()