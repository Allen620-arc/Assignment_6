'''
    Name: Allen Keettikkal
    NSID: alk423
    Student Number: 11278995
    Instructor: Jeffrey Long
'''


class node(object):
    """ A version of the Node class with public attributes.
        This makes the use of node objects a bit more convenient for 
        implementing LList class.  
        
        Since there are no setters and getters, we use the attributes directly.
        
        This is safe because the node class is defined in this module.  
        No one else will use this version of the class.
    """

    def __init__(self, data, next=None):
        """
        Create a new node for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the node
            next:  Another node (or None, by default)
        """
        self.data = data
        self.next = next

    # Note: use the attributes directly; no setters or getters!


class LList(object):
    def __init__(self):
        """
        Purpose
            creates an empty list
        """
        self._size = 0  # how many elements in the stack
        self._head = None  # the node chain starts here; initially empty
        self._tail = None

    def is_empty(self):
        """
        Purpose
            Checks if the given list has no data in it
        Return:
            :return True if the list has no data, or False otherwise
        """
        return self._size == 0

    def size(self):
        """
        Purpose
            Returns the number of data values in the given list
        Return:
            :return The number of data values in the list
        """
        return self._size

    def prepend(self, val):
        """
        Purpose
            Insert val at the front of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is at index 0.
            The values previously in the list appear after the new value.
        Return:
            :return None
        """
        new_node = node(val, self._head)
        self._head = new_node
        self._size += 1
        if self._size == 1:
            self._tail = self._head

    def append(self, val):
        """
        Purpose
            Insert val at the end of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is last in the list.
        Return:
            :return None
        """
        new_node = node(val, None)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            prev_last_node = self._tail
            prev_last_node.next = new_node
            self._tail = new_node

        self._size += 1
        return None

    def get_index_of_value(self, val):
        """
        Purpose
            Return the smallest index of the given val.
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            none
        Return:
            :return True, idx if the val appears in self
            :return False, None if the vale does not appear in self
        """
        # walk along the chain
        current = self._head
        idx = 0
        while current is not None:
            if val == current.data:
                return True, idx
            current = current.next
            idx += 1
        return False, None

    def remove_from_front(self):
        """
        Purpose
            Removes and returns the first value 
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair (True, value) if self is not empty
            :return The pair (False, None) if self is empty
        """
        if self._size != 0:
            prev_first_node = self._head
            value = prev_first_node.data
            self._head = prev_first_node.next
            self._tail = prev_first_node.next
            self._size -= 1
            return True, value
        if self._size == 0:
            return False, None

    def remove_from_back(self):
        """
        Purpose
            Removes and returns the last value
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair True, value if self is not empty
            :return The pair False, None if self is empty
        """
        current = self._head
        prev = None

        # If the node chain is empty, return False, None.
        if current is None:
            return False, None

        # If your node chain has a size of 1, you're going to have to set the head, tail to None, size to 0,
        # and return True, value.
        if self._size == 1:
            value = self._head.data
            self._head = None
            self._tail = None
            self._size = 0
            return True, value

        # If your node chain has a size greater than 1, you're going to have to find the last value, remove it,
        # and return the value.
        while current is not None:
            if current.next is None:
                prev.next = None
                self._tail = prev
                value = current.data
                self._size -= 1
                return True, value
            prev = current
            current = current.next


    def retrieve_data(self, idx):
        """
        Purpose
            Return the value stored at the index idx
        Preconditions:
            :param idx:   a non-negative integer
        Post-conditions:
            none
        Return:
            :return (True, val) if val is stored at index idx and idx is valid
            :return (False, None) if the idx is not valid for the list
        """
        current = self._head
        idx_chain = 0
        while current is not None:
            if idx == idx_chain:
                val = current.data
                return True, val
            current = current.next
            idx_chain += 1
        return False, None

    def set_data(self, idx, val):
        """
        Purpose
            Store val at the index idx
        Preconditions:
            :param val:   a value of any kind
            :param idx:   a non-negative integer
        Post-conditions:
            The value stored at index idx changes to val
        Return:
            :return True if the index was valid, False otherwise
        """
        current = self._head
        idx_chain = 0
        while current is not None:
            if idx_chain == idx:
                current.data = val
                return True
            current = current.next
            idx_chain += 1
        return False
