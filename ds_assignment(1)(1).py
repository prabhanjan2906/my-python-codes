# TODO: Get rid of all flake8 warnings -- that means adding docstrings
#      to the file, classes, and methods.
import types


def terrible_hash(bin):
    """A terrible hash function that can be used for testing.

    A hash function should produce unpredictable results,
    but it is useful to see what happens to a hash table when
    you use the worst-possible hash function.  The function
    returned from this factory function will always return
    the same number, regardless of the key.

    :param bin:
        The result of the hash function, regardless of which
        item is used.

    :return:
        A python function that can be passes into the constructor
        of a hash table to use for hashing objects.
    """
    def hashfunc(item, arg2=None):
        return bin
    return hashfunc


class SinglyLinkedNode(object):

    def __init__(self, item=None, next_link=None):
        super(SinglyLinkedNode, self).__init__()
        self._item = item
        self._next = next_link

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __repr__(self):
        return repr(self.item)


class SinglyLinkedList(object):

    def __init__(self, data=None):
        super(SinglyLinkedList, self).__init__()
        self.list = SinglyLinkedNode(item=data)
        self.length_of_list = 1

    def __len__(self):
        return self.length_of_list

    def __iter__(self):
        iterator = self.list
        while iterator is not None:
            yield (iterator)
            iterator = iterator.next

    def __contains__(self, item):
        for l in self:
            if item == l.item:
                return True

        return False

    def removeBasedOnItem(self, item):
        """
        This API will delete a node containing the item from the list
        :param item: the value that needs to be deleted from the list
        :return:
        """
        #  find item and remove it.
        prev_node = None
        l = None

        for l in self:
            if item == l.item:
                if prev_node:
                    prev_node.next = l.next
                else:
                    self.list = l.next

                del(l)
                self.length_of_list = self.length_of_list - 1
                return
            prev_node = l

    def removeNode(self, node):
        """
        This API will remove the node from the list
        :param node: contains the node that is to be removed
        :return:
        """
        prev_node = None

        for l in self:
            if node == l:
                if prev_node:
                    prev_node.next = l.next
                else:
                    self.list = l.next

                del(l)
                self.length_of_list = self.length_of_list - 1
                return
            prev_node = l

    def prepend(self, item):
        """
        This Function is intended to insert a singly link list node to the beginning of the list.
        :param item: The value that is to be stored in the list.
        :return: Nothing
        """
        if not self.__contains__(item):
            temp = SinglyLinkedNode(item=item, next_link=self.list)
            self.list = temp
            self.length_of_list = self.length_of_list + 1

    def __repr__(self):
        s = "List:" + "->".join([str(item.item) for item in self])
        return s


class BinaryTreeNode(object):

    def __init__(self, data=None, left=None, right=None, parent=None):
        super(BinaryTreeNode, self).__init__()
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTreeDict(object):

    def __init__(self):
        super(BinarySearchTreeDict, self).__init__()
        self._root = None
        self._height = -1
        self.count = 0

    @property
    def height(self):
        """
        This is a getter property function that will be called when ever an attempt is made to retrieve the height.
        called when "self.height" statement is executed within this class OR
        when "obj.height" statement is executed outside this class, where obj is object of this class.
        :return: the height of the tree.
        """
        return self._height

    @height.setter
    def height(self, h):
        """
        This is a setter property function that will be called when ever an attempt is made to assign height.
        called when "self.height = value" statement is executed within this class OR
        when "obj.height = value" statement is executed outside this class, where obj is object of this class.
        :param h: new value for the height
        :return: Nothing
        """
        self._height = h

    def reCalculateHeight(self, node):
        """
        This API will calculate the height of the binary search tree.
        :param node: contains the root node of the subtree
        :return: the length of the binary search tree
        """
        if(node is None):
            return -1

        return max(
            self.reCalculateHeight(
                node.left), self.reCalculateHeight(
                node.right)) + 1

    def GetItem(self, node, key):
        """
        This function will return the tuple associated with the key. None otherwise.
        :param node: contains the root node of the subtree
        :param key: contains the key that needs to be searched.
        :return: None/Tuple
        """
        # Get the VALUE associated with key
        if(node.data[0] > key):  # check if the key is less than the value at the node
            if (node.left):
                # traverse the left subtree
                return self.GetItem(node.left, key)

        elif (node.data[0] < key):  # check if the key is greater than the value at the node
            if(node.right):
                # traverse the right subtree
                return self.GetItem(node.right, key)
        else:    # the key is equal to the value at the node
            return (node.data[0], node.data[1])

        return None

    def _search_node_to_insert(self, node, key, val, TreeHeight):
        """
        Private function to search the node to determine the appropriate place to
        insert the new key. This function also dynamically calculates the height
        of the tree while inserting.
        :param node: contains the root node of the subtree.
        :param key: contains the key that needs to be inserted
        :param val: contains the value assoiciated with the key that needs to be inserted
        :param TreeHeight: contains the height of the tree.
        :return:
        """
        if(node.data[0] > key):  # check if the key is less than the value at the node
            if (node.left):
                self._search_node_to_insert(
                    node.left, key, val, TreeHeight + 1)  # traverse the left subtree
            else:
                # insert a new node as the left child
                node.left = BinaryTreeNode(data=(key, val), parent=node)
                self.count = self.count + 1
                if (self.height < TreeHeight):
                    self.height = TreeHeight + 1

        elif (node.data[0] < key):  # check if the key is greater than the value at the node
            if(node.right):
                self._search_node_to_insert(
                    node.right, key, val, TreeHeight + 1)  # traverse the right subtree
            else:
                # insert a new node as the right child
                node.right = BinaryTreeNode(data=(key, val), parent=node)
                self.count = self.count + 1
                if (self.height < TreeHeight):
                    self.height = TreeHeight + 1
        else:  # the key is equal to the value at the node
            return

    def setitem(self, key, value):
        """
        This api is a wrapper function for __setitem__() for the applications that wishes
        to invoke the function manually
        :param key: contains the key to be inserted
        :param value: contains the value associated with the key to be inserted
        :return: Nothing
        """
        if (self._root is None):  # check if the root node is null
            # create a new node to the root node
            self._root = BinaryTreeNode(data=(key, value))
            self.height = self.height + 1
            self.count = self.count + 1
        else:  # root is not null, lookup the apt position and insert the key.
            self._search_node_to_insert(self._root, key, value, 0)

    def __setitem__(self, key, value):
        """
        built-in function overridden to assign a new key and a value
        :param key: key
        :param value: the value associated with the key
        :return: Nothing
        """
        self.setitem(key, value)

    def inorder_keys(self, node):
        """
        recursive function that traverses the tree in in-order form and yields the result.
        :param node: contains the parent node whose subtrees are to be traversed.
        :return: yields the key of each node
        """
        if node:
            for node_data in self.inorder_keys(node.left):
                yield node_data
            yield node.data[0]
            for node_data in self.inorder_keys(node.right):
                yield node_data

    def postorder_keys(self, node):
        """
        recursive function that traverses the tree in post-order form and yields the result.
        :param node: contains the parent node whose subtrees are to be traversed.
        :return: yields the key of each node
        """
        if node:
            for node_data in self.postorder_keys(node.left):
                yield node_data
            for node_data in self.postorder_keys(node.right):
                yield node_data
            yield node.data[0]

    def preorder_keys(self, node):
        """
        recursive function that traverses the tree in pre-order form and yields the result.
        :param node: contains the parent node whose subtrees are to be traversed.
        :return: yields the key of each node
        """
        if node:
            yield node.data[0]
            for node_data in self.preorder_keys(node.left):
                yield node_data
            for node_data in self.preorder_keys(node.right):
                yield node_data

    def items(self, node):
        """
        recursive function that traverses the tree in inorder form and yields the result.
        :param node: contains the parent node whose subtrees are to be traversed.
        :return: yields the contents of each node
        """
        if node:
            for node_data in self.items(node.left):
                yield node_data
            yield (node.data[0], node.data[1])
            for node_data in self.items(node.right):
                yield node_data

    def find_Minimum_element(self, node):
        """
        Recursively traverses to the left most node of a given root node and returns the node.
        :param node: contains the parent node
        :return: the node containing the least element of the subtree.
        """
        if(not node.left):
            return node

        return self.find_Minimum_element(node.left)

    def DeleteItemFromTree(self, node, key):
        """
        recursively searches through the binary search tree for the node containing the key to be deleted and
        deletes that node.
        :param node: contains the parent node
        :param key: contains the key that is intended to be removed from the tree.
        :return: True/False
        """
        if(node.data[0] > key):  # check if the key is less than the value at the node
            if (node.left):
                return self.DeleteItemFromTree(
                    node.left, key)  # traverse the left subtree

        elif (node.data[0] < key):  # check if the key is greater than the value at the node
            if(node.right):
                return self.DeleteItemFromTree(
                    node.right, key)  # traverse the right subtree
        else:  # Found the node containing key to be deleted
            if (node.left is None) and (
                    node.right is None):  # the node is the leaf node
                if(node.parent.left == node):
                    node.parent.left = None  # set the pointer of the parent node to None
                else:
                    node.parent.right = None  # set the pointer of the parent node to None
                del(node)  # delete the node
                self.height = self.reCalculateHeight(self._root)
                self.count = self.count - 1
                return True
            elif (node.left) and (node.right):  # the node contains both the left and right subtrees
                # look for the node that has the least value in the right
                # subtree
                minimum_node = self.find_Minimum_element(node.right)
                # the minimum node is the leaf node.
                if (not minimum_node.right) and (not minimum_node.left):
                    # copy the data of the minimum node into the intended node
                    node.data = minimum_node.data
                    minimum_node.parent.left = None
                    del(minimum_node)  # delete the minimum node
                    self.height = self.reCalculateHeight(self._root)
                    self.count = self.count - 1
                    return True
                else:  # the minimum node is not the leaf node. it contains a right subtree
                    # copy the data of the minimum node into the intended node
                    node.data = minimum_node.data
                    # hook the right subtree of the minimum node to its parent.
                    minimum_node.parent.left = minimum_node.right
                    del(minimum_node)  # delete the minimum node
                    self.height = self.reCalculateHeight(self._root)
                    self.count = self.count - 1
                    return True
            else:  # the node contains either of the left or the right subtrees.
                if node.left:  # check if the node contains left subtree
                    if (node == node.parent.left):  # the node to be deleted is a left child of its parent
                        node.parent.left = node.left  # hook the left sub tree of the node to its parent
                        # assign the parent of the left child to node's parent
                        node.left.parent = node.parent
                    else:  # the node to be deleted is a right child of its parent
                        node.parent.right = node.left  # hook the right sub tree of the node to its parent
                        # assign the parent of the right child to node's parent
                        node.left.parent = node.parent
                else:  # the node contains right subtree
                    if (node == node.parent.left):  # the node to be deleted is a left child of its parent
                        # hook the right sub tree of the node to its parent's
                        # left
                        node.parent.left = node.right
                        # assign the parent of the right child to node's parent
                        node.right.parent = node.parent
                    else:  # the node to be deleted is a right child of its parent
                        # hook the right sub tree of the node to its parent's
                        # right
                        node.parent.right = node.right
                        # assign the parent of the right child to node's parent
                        node.right.parent = node.parent

                del(node)
                self.height = self.reCalculateHeight(self._root)
                self.count = self.count - 1
                return True

        return False

    def __delitem__(self, key):
        """
        built in function overridden to delete the key from the hash. called when del obj[key]
        is encountered.
        :param key: key to be deleted.
        :return: true or false
        """
        return self.DeleteItemFromTree(self._root, key)

    def deleteFromTree(self, key):
        """
        This api is a wrapper function for __delitem__() for the applications that wishes
        to invoke the function manually
        :param key: contains the key to be inserted
        :return: Nothing
        """
        self.DeleteItemFromTree(self._root, key)

    def __getitem__(self, item):
        """
        built in function overridden to retrieve the value in a key.
        called when obj[key] executed outside the class.
        :param item: the key
        :return: The value stored as part of the key, None if not found
        """
        temp = self.GetItem(self._root, key=item)
        if temp:
            return temp[1]
        return None

    def __contains__(self, key):
        """
        built in function overridden to know if the key is present or not. Called when an
        operator such as comparison operator is used on the object
        :param key:
        :return:
        """
        if self.GetItem(self._root, key):
            return True
        return False

    def __len__(self):
        """
        build in function. overridden to return the count of the objects. Called when
        len(obj) is executed outside the class or len(self) inside the class.
        :return: the count of the number of elements.
        """
        return self.count

    def display(self):
        """
        prints the keys using INORDER on one line, pre order on the next line, and
        post order on the successive line.
        :return: Nothing
        """
        # Print the keys using INORDER on one
        #      line and PREORDER on the next
        print ', '.join([str(key) for key in self.inorder_keys(self._root)])
        print ', '.join([str(key) for key in self.preorder_keys(self._root)])
        print ', '.join([str(key) for key in self.postorder_keys(self._root)])


class ChainedHashDict(object):

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(ChainedHashDict, self).__init__()
        self.n = 0
        self.m = bin_count
        self.hash_table = [None] * self.m
        self.alpha = 0
        self.HashFunc = hashfunc
        self.maxload = max_load

    @property
    def load_factor(self):
        """
        getter function that retrieves the current max load of the hash.
        :return: the current max load of the hash (alpha).
        """
        return self.alpha

    @load_factor.setter
    def load_factor(self, ALPHA):
        """
        setter function that sets the max load to a new value ALPHA
        :param ALPHA: new max load value of the hash
        :return: Nothing
        """
        self.alpha = ALPHA

    @property
    def bin_count(self):
        """
        getter function that retrieves the total bin count of the hash.
        :return: the current bin count
        """
        return self.m

    @bin_count.setter
    def bin_count(self, bincount):
        """
        setter function that sets the total bin count of the hash to a new value "bincount"
        :param bincount: the new size of bin
        :return: Nothing
        """
        self.m = bincount

    def __getitem__(self, KEY):
        """
        built in function overridden to retrieve the value associated with the KEY. called when
        obj[key] is invoked
        :param KEY: The Key to be searched.
        :return: item if present, None otherwise.
        """
        m = self.runHashAlgo(KEY)
        if not self.hash_table[m]:
            raise KeyError

        node = self.__contains__(m, KEY)
        if node is not None:
            return node.item

        return None

    def rebuild(self, bincount):
        """
        This API is responsible for doubling the size of the list and rehash each elements into the hash table.
        :param bincount: old bin count value
        :return:
        """
        self.hash_table.extend(
            [None] *
            bincount)  # add the same number of slots to the hash again. (doubling the size)
        self.bin_count = self.bin_count * 2  # double the size of the hash table
        self.n = 0  # reset the total elements
        oldTable = []
        for i in range(
                bincount):  # extract all the tuples stored in each of the chains
            if(self.hash_table[i] is None):
                continue

            for node in self.hash_table[i]:
                oldTable.append((node.item[0], node.item[1]))
                self.hash_table[i].removeNode(node)
                if(len(self.hash_table[i]) == 0):
                    self.hash_table[i] = None

        for everyTuple in oldTable:  # Now perform an insert into the hash table to insert the elements back into the hash
            self.insert(everyTuple[0], everyTuple[1])

    def runHashAlgo(self, key):
        """
        runs the hash algorithm h(k)
        :param key: the key k.
        :return: the object of the hash function that needs to be run
        """
        if(self.HashFunc == hash):
            return self.HashFunc(key) % self.bin_count
        else:
            return self.HashFunc(key, self.m)

    def __setitem__(self, KEY, VALUE):
        """
        inserts the desired KEY and VALUE tuple into the hash tables
        :param KEY: the key that needs to be stored
        :param VALUE: the value associated with the key
        :return: Nothing
        """
        key = self.runHashAlgo(
            KEY)  # run the h(k) on the KEY and get the index of the bin
        value = VALUE
        if(self.hash_table[key] is None):  # this location is empty.
            # create a new singly linked list object here
            self.hash_table[key] = SinglyLinkedList(data=(KEY, VALUE))
            self.n = self.n + 1
        else:
            # check if this list already contains the KEY
            NodeFound = self.__contains__(key, KEY)
            if NodeFound:  # if it contains then update the value to the new VALUE
                # Discard the old to Update the value to the new one.
                NodeFound.item = (KEY, VALUE)
            else:
                # put this node at the begining of the list
                self.hash_table[key].prepend((KEY, VALUE))
                self.n = self.n + 1

        # calculate the load factor
        self.load_factor = float(self.n) / float(self.m)

        # if load factor exceeds the desired value, the perform rehashing
        if(self.load_factor > self.maxload):
            self.rebuild(bincount=self.bin_count)

    def __delitem__(self, KEY):
        """
        deletes the desired key from the hash
        :param KEY: the key to be deleted
        :return: exception if key not present.
        """
        key = self.runHashAlgo(KEY)
        if not self.hash_table[key]:
            print "Key not found"

        # get the node of the list containing the key
        SLL_node = self.__contains__(key, KEY)

        if SLL_node is not None:
            # remove the node containing the key
            self.hash_table[key].removeNode(SLL_node)
            self.n = self.n - 1
            # if the deleted node was the last node of the list
            if(len(self.hash_table[key]) == 0):
                self.hash_table[key] = None  # mark the bin as empty

            # calculate the load factor
            self.load_factor = float(self.n) / float(self.bin_count)

    def __contains__(self, m, KEY):
        """
        check if the node containing key is present in the hash table or not.
        :param m: the index of the bin
        :param KEY: The key to be searched.
        :return: the node containing the key or None otherwise.
        """
        for node in self.hash_table[m]:
            if (KEY == node.item[0]):
                return node

        return None

    def __len__(self):
        """
        build in function. overridden to return the count of the objects. Called when
        len(obj) is executed outside the class or len(self) inside the class.
        :return: the count of the number of elements.
        """
        return self.n

    def insert(self, key, value):
        """
        A wrapper function that can be used by external applications to insert a key/values into the hash.
        :param key: the key that needs to be inserted
        :param value: the value that is associated with the key.
        :return: Nothing
        """
        self.__setitem__(key, value)

    def delete(self, key):
        """
        A wrapper function that can be used by external applications to insert a key/values into the hash.
        :param key: the key that needs to be inserted
        :return:
        """
        self.__delitem__(key)

    def __iter__(self):
        """
        built in function is called when the object needs to be iterated. called when
        for node in self: statement is executed inside the class and
        for node in obj: statement is executed outside the class and
        :return:
        """
        i = 0
        while i < len(self.hash_table):
            if(self.hash_table[i] is None):
                yield "[" + str(i) + "]: " + "None"
            else:
                yield ("[" + str(i) + "]: " + repr(self.hash_table[i]))
            i = i + 1

    def display(self):
        """
        Print a string showing the table with multiple lines. It displays the items in the respective bins
        :return: None
        """
        for item in self:
            print item

    def forceRebuild(self, maxLoad):
        """
        This API is used to force a rebuild operation with a new max load value
        :param maxLoad: new max load value (load factor)
        :return:
        """
        if(maxLoad == self.maxload):
            return  # don't have to rebuild when the bin count is the same

        self.maxload = maxLoad
        self.rebuild(self.bin_count)


def myHashFunction(key, tableSize):
    """
    the hash function h(k). Calculates the bin from the given key.
    :param key: the key to be inserted
    :param tableSize: the size of the table
    :return: the bin
    """
    if(isinstance(key, types.IntType)):
        return (key % tableSize)
    elif(isinstance(key, types.StringType)):
        sum = 0
        toInt = lambda x: ord(x)
        for i in range(len(key)):
            sum = sum + toInt(key[i]) * pow(17, i)

        return sum % tableSize
    else:
        pass  # raise KeyError exception.


class OpenAddressHashDict(object):

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(OpenAddressHashDict, self).__init__()
        self.n = 0
        self.m = bin_count
        self.hash_table = [None] * self.m
        self.alpha = 0
        self.HashFunc = hashfunc
        self.maxload = float(max_load)
        self.DELETED = "DELETED"

    @property
    def load_factor(self):
        """
        getter function that retrieves the current max load of the hash.
        :return: the current max load of the hash (alpha).
        """
        return self.alpha

    @load_factor.setter
    def load_factor(self, ALPHA):
        """
        setter function that sets the max load to a new value ALPHA
        :param ALPHA: new max load value of the hash
        :return: Nothing
        """
        self.alpha = ALPHA

    @property
    def bin_count(self):
        """
        getter function that retrieves the total bin count of the hash.
        :return: the current bin count
        """
        return self.m

    @bin_count.setter
    def bin_count(self, bincount):
        """
        setter function that sets the total bin count of the hash to a new value "bincount"
        :param bincount: the new size of bin
        :return: Nothing
        """
        self.m = bincount

    def runHashAlgo(self, key):
        """
        runs the hash algorithm h(k)
        :param key: the key k.
        :return: the object of the hash function that needs to be run
        """
        if(self.HashFunc == hash):
            return self.HashFunc(key)
        else:
            return self.HashFunc(key, self.m)

    def rebuild(self, bincount):
        """
        This API is responsible for doubling the size of the list and rehash each elements into the hash table.
        :param bincount: old bin count value
        :return:
        """
        self.hash_table.extend(
            [None] *
            bincount)  # add the same number of slots to the hash again. (doubling the size)
        self.bin_count = self.bin_count * 2  # double the size of the hash table
        self.n = 0  # reset the total elements
        oldTable = []
        for i in range(
                bincount):  # extract all the tuples stored in each of the chains
            if((self.hash_table[i] is None) or (self.hash_table[i] == self.DELETED)):
                continue

            oldTable.append((self.hash_table[i][0], self.hash_table[i][1]))
            self.hash_table[i] = None

        for everyTuple in oldTable:  # Now perform an insert into the hash table to insert the elements back into the hash
            self.insert(everyTuple[0], everyTuple[1])

    def __getitem__(self, KEY):
        """
        built in function overridden to retrieve the value associated with the KEY. called when
        obj[key] is invoked
        :param KEY: The Key to be searched.
        :return: item if present, None otherwise.
        """
        key = self.runHashAlgo(KEY)
        if not self.hash_table[key]:
            raise KeyError

        node = self.__contains__(key)
        if node is not None:
            return node.item

        return None

    def __setitem__(self, KEY, VALUE):
        """
        inserts the desired KEY and VALUE tuple into the hash tables
        :param KEY: the key that needs to be stored
        :param VALUE: the value associated with the key
        :return: Nothing
        """
        self.load_factor = float(self.n) / float(self.m)
        if(self.load_factor >= self.maxload):
            self.rebuild(bincount=self.bin_count)

        # run the h(k) on the KEY and get the index of the bin
        key = self.runHashAlgo(KEY)
        if(self.hash_table[key] is None):  # this location is empty.
            # add the tuple to the empty slot
            self.hash_table[key] = (KEY, VALUE)
            self.n = self.n + 1
        else:
            i = key
            while i < len(
                    self.hash_table):  # collision detected, search for the next available slot using Linear probing
                if((self.hash_table[i] is None) or (self.hash_table[i] == self.DELETED)):
                    self.hash_table[i] = (KEY, VALUE)
                    self.n = self.n + 1
                    break
                else:
                    if((self.hash_table[i] is not None) and (self.hash_table[i][0] == KEY)):
                        # found new value for the same key that was already
                        # present in the hash
                        self.hash_table[i] = (KEY, VALUE)
                        break
                i = (i + 1) % self.bin_count
                if(i == key):
                    break  # reached to where we began

    def __delitem__(self, KEY):
        """
        deletes the desired key from the hash
        :param KEY: the key to be deleted
        :return: exception if key not present.
        """
        key = self.runHashAlgo(KEY)
        if not self.hash_table[key]:
            return  # key not present

        i = key
        while i < len(self.hash_table):  # look for the key in the table.
            if ((self.hash_table[i]) and (self.hash_table[
                    i] == self.DELETED)):  # location that matches with DELETED matches
                return  # already deleted
            if ((self.hash_table[i]) and (
                    self.hash_table[i][0] == KEY)):  # key found
                # mark the location as DELETED
                self.hash_table[key] = self.DELETED
                break

            i = (i + 1) % self.bin_count  # linear probe for the next slot
            if(i == key):
                break  # reached to where we began

        self.n = self.n - 1
        self.load_factor = float(self.n) / float(self.bin_count)

    def __contains__(self, key):
        """
        check if the node containing key is present in the hash table or not.
        :param m: the index of the bin
        :param KEY: The key to be searched.
        :return: the node containing the key or None otherwise.
        """
        for node in self.hash_table[key]:
            if (key == node.item[0]):
                return node

        return None

    def __len__(self):
        """
        build in function. overridden to return the count of the objects. Called when
        len(obj) is executed outside the class or len(self) inside the class.
        :return: the count of the number of elements.
        """
        return self.n

    def insert(self, key, value):
        """
        A wrapper function that can be used by external applications to insert a key/values into the hash.
        :param key: the key that needs to be inserted
        :param value: the value that is associated with the key.
        :return: Nothing
        """
        self.__setitem__(key, value)

    def delete(self, key):
        """
        A wrapper function that can be used by external applications to insert a key/values into the hash.
        :param key: the key that needs to be inserted
        :return:
        """
        self.__delitem__(key)

    def __repr__(self):
        """
        built in function overridden to print the elements of the hash.
        :return: the each bin represented in string format.
        """
        i = 0
        s = ""
        for item in self:
            if item is None:
                s = s + "[" + str(i) + "]: " + "None\n"
            elif item == self.DELETED:
                s = s + "[" + str(i) + "]: " + "DELETED\n"
            else:
                s = s + "[" + str(i) + "]-> " + str(item[0]) + \
                    ": " + str(item[1]) + "\n"
            i = i + 1
        return s

    def __iter__(self):
        """
        built in function is called when the object needs to be iterated. called when
        for node in self: statement is executed inside the class and
        for node in obj: statement is executed outside the class and
        :return: Nothing
        """
        i = 0
        while i < len(self.hash_table):
            yield self.hash_table[i]
            i = i + 1

    def display(self):
        """
        Print a string showing the table with multiple lines. It displays the items in the respective bins
        :return: None
        """
        print self

    def forceRebuild(self, maxLoad):
        """
        This API is used to force a rebuild operation with a new max load value
        :param maxLoad: new max load value (load factor)
        :return:
        """
        if(maxLoad == self.maxload):
            return  # don't have to rebuild when the bin count is the same

        self.maxload = maxLoad
        self.rebuild(self.bin_count)


def main():
    """
    # # Singly Link list
    # >>> sll = SinglyLinkedList(1)
    # >>> sll.prepend(2)
    # >>> sll.prepend(4)
    # >>> sll.prepend(6)
    # >>> sll.prepend(8)
    # >>> sll.prepend(4)
    # >>> print sll
    # List:8->6->4->2->1
    # >>> print (len(sll))
    # 5
    # >>> sll.removeBasedOnItem(1)
    # >>> sll.removeBasedOnItem(8)
    # >>> print sll
    # List:6->4->2
    # >>> print len(sll)
    # 3
    #
    # Binary Tree
    >>> bst = BinarySearchTreeDict()
    >>> bst[200] = 10
    >>> bst[100] = 5
    >>> bst[50] = 8
    >>> bst[150] = 9
    >>> bst[25] = 3
    >>> bst[75] = 1
    >>> bst[20] = 4
    >>> bst[30] = 14
    >>> bst[70] = 14
    >>> bst[80] = 14
    >>> bst[125] = 3
    >>> bst[175] = 1
    >>> bst[120] = 3
    >>> bst[130] = 3
    >>> bst[170] = 3
    >>> bst[180] = 3
    >>> bst[400] = 3
    >>> bst[300] = 3
    >>> bst[500] = 3
    >>> bst[250] = 3
    >>> bst[450] = 3
    >>> print bst[11111]
    None
    >>> bst.display()
    20, 25, 30, 50, 70, 75, 80, 100, 120, 125, 130, 150, 170, 175, 180, 200, 250, 300, 400, 450, 500
    200, 100, 50, 25, 20, 30, 75, 70, 80, 150, 125, 120, 130, 175, 170, 180, 400, 300, 250, 500, 450
    20, 30, 25, 70, 80, 75, 50, 120, 130, 125, 170, 180, 175, 150, 100, 250, 300, 450, 500, 400, 200

    >>> del (bst[100])
    >>> del bst[120]
    >>> bst.display()
    20, 25, 30, 50, 70, 75, 80, 125, 130, 150, 170, 175, 180, 200, 250, 300, 400, 450, 500
    200, 125, 50, 25, 20, 30, 75, 70, 80, 150, 130, 175, 170, 180, 400, 300, 250, 500, 450
    20, 30, 25, 70, 80, 75, 50, 130, 170, 180, 175, 150, 125, 250, 300, 450, 500, 400, 200

    >>> del bst[300]
    >>> bst.display()
    20, 25, 30, 50, 70, 75, 80, 125, 130, 150, 170, 175, 180, 200, 250, 400, 450, 500
    200, 125, 50, 25, 20, 30, 75, 70, 80, 150, 130, 175, 170, 180, 400, 250, 500, 450
    20, 30, 25, 70, 80, 75, 50, 130, 170, 180, 175, 150, 125, 250, 450, 500, 400, 200

    >>> del bst[500]
    >>> bst.display()
    20, 25, 30, 50, 70, 75, 80, 125, 130, 150, 170, 175, 180, 200, 250, 400, 450
    200, 125, 50, 25, 20, 30, 75, 70, 80, 150, 130, 175, 170, 180, 400, 250, 450
    20, 30, 25, 70, 80, 75, 50, 130, 170, 180, 175, 150, 125, 250, 450, 400, 200

    >>> del bst[5000]
    >>> bst[750] = "seven hundred and fifty"
    >>> bst.display()
    20, 25, 30, 50, 70, 75, 80, 125, 130, 150, 170, 175, 180, 200, 250, 400, 450, 750
    200, 125, 50, 25, 20, 30, 75, 70, 80, 150, 130, 175, 170, 180, 400, 250, 450, 750
    20, 30, 25, 70, 80, 75, 50, 130, 170, 180, 175, 150, 125, 250, 750, 450, 400, 200

    >>> del bst[750]
    >>> del bst[20]
    >>> del bst[30]
    >>> del bst[70]
    >>> bst.display()
    25, 50, 75, 80, 125, 130, 150, 170, 175, 180, 200, 250, 400, 450
    200, 125, 50, 25, 75, 80, 150, 130, 175, 170, 180, 400, 250, 450
    25, 80, 75, 50, 130, 170, 180, 175, 150, 125, 250, 450, 400, 200

    # Chained hash dictionary
    >>> ch = ChainedHashDict(bin_count=10, hashfunc=myHashFunction)
    >>> ch[19] = "ABC"
    >>> ch[18] = "B"
    >>> ch[17] = "c"
    >>> ch[16] = "D"
    >>> ch[15] = "E"
    >>> ch[14] = "f"
    >>> ch[7] = "G"
    >>> ch[8] = "H"
    >>> ch[9] = "I"
    >>> ch[10] = "J"
    >>> ch[13] = "hello world!"
    >>> ch[33] = "new world!"
    >>> ch.display()
    [0]: None
    [1]: None
    [2]: None
    [3]: None
    [4]: None
    [5]: None
    [6]: None
    [7]: List:(7, 'G')
    [8]: List:(8, 'H')
    [9]: List:(9, 'I')
    [10]: List:(10, 'J')
    [11]: None
    [12]: None
    [13]: List:(33, 'new world!')->(13, 'hello world!')
    [14]: List:(14, 'f')
    [15]: List:(15, 'E')
    [16]: List:(16, 'D')
    [17]: List:(17, 'c')
    [18]: List:(18, 'B')
    [19]: List:(19, 'ABC')

    # Open address hash dictionary with linear probing
    >>> ohd = OpenAddressHashDict(bin_count=29, hashfunc=terrible_hash(1), max_load=1)
    >>> ohd["ASU"] = "Arizona State University"
    >>> del ohd["ASU"]

    >>> ohd["UA"] = "University of Arizona Tucson"
    >>> ohd["OSU"] = "Ohio State University"
    >>> ohd["FSU"] = "Florida State University"
    >>> ohd["UCLA"] = "University of California Los Angeles"
    >>> ohd["UCB"] = "University of California Berkeley"
    >>> ohd["UCI"] = "University of California Irvine"
    >>> print ohd
    [0]: None
    [1]-> UA: University of Arizona Tucson
    [2]-> OSU: Ohio State University
    [3]-> FSU: Florida State University
    [4]-> UCLA: University of California Los Angeles
    [5]-> UCB: University of California Berkeley
    [6]-> UCI: University of California Irvine
    [7]: None
    [8]: None
    [9]: None
    [10]: None
    [11]: None
    [12]: None
    [13]: None
    [14]: None
    [15]: None
    [16]: None
    [17]: None
    [18]: None
    [19]: None
    [20]: None
    [21]: None
    [22]: None
    [23]: None
    [24]: None
    [25]: None
    [26]: None
    [27]: None
    [28]: None
    <BLANKLINE>

    # ch = ChainedHashDict(bin_count=10, hashfunc=terrible_hash(1))
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
