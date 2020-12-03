
'''
*****************************************************
 HASHSET USING LINEAR PROBLEM FOR COLLISION DETECTION
*****************************************************
'''

'''
The main idea behind a LinearHashTable is that we would, ideally, like to store the
element x with hash value i <-- hash(x) in the table location t[i]. If we cannot
do this (because some element is already stored there) then we try to store it
at location t[(i+1) mod length(t)]; if that's not possible, then we try $
t[(i+2) mod length(t)], and so on, until we find a place for x.

There are three types of entries stored in t
1. data values: actual values in the USet that we are representing;
2. nil values: at array locations where no data has ever been stored; and
3. del values: at array locations where data was once stored but that has since
   been deleted.
In addition to the counter, n,  that keeps track of the number of elements in the
LinearHashTable, a counter, q, keeps track of the number of elements of Types 1 and
3. That is, q is equal to n plus the number of del values in t. To make this work
efficiently, we need t to be considerably larger than q, so that there are lots of nil
values in t. The operations on a LinearHashTable therefore maintain the invariant that
length(t) >= 2q.


To summarize, a LinearHashTable contains an array, t, that stores data elements,
and integers n and q that keep track of the number of data elements and non-nil
values of t, respectively. Because many hash functions only work for table sizes
 that are a power of 2, we also keep an integer d and maintain the invariant that
length(t) = 2^d.

'''



class Hashset():

    def __init__(self):
        self.del = -999
        self.d= 1
        self.n = 0              # counter for data elements
        self.q = 0              # q = n + del values
        self.max_length = 2**d
        # self.max_load_factor = 0.75
        self.table = [None] * self.max_length

    def hash(self, key):
        # TODO more robust
        return key % self.max_length

    def find(self,key):
        i = hash(key)           # i = hashcode
        while self.table[i] != None:
            if self.table[i] != del and key == self.table[i]:
                    return self.table[i]
            i = (i+1) % self.max_length

    def add(self,key):
        if find(key) != None:       # meaning the value already exists
            return False

        if 2*(self.q+1) > self.max_length:
            self.resize()

        i = hash(key)

        while self.table[i] != None and self.table[i] != self.del:
            i = (i+1) % self.max_length

        if self.table[i] == None:
            self.q = self.q+1
            self.n = self.n + 1
            self.table[i] = key
            return True




    def remove(self,key):
        if find(key) != None:       # meaning the value already exists
            return False

        if 2*(self.q+1) > self.max_length:
            self.resize()

        i = hash(key)

        while self.table[i] != None:
            y = self.table[i]
            if y != del or x == y:
                self.table[i] = self.del
                self.n-=self.n
                if 8*n < max.length(self.table):
                    self.resize()

            i = (i+1) % self.max_length

    return None

    def resize(self):
        '''
        The resize method is called by add method when the number of non-nil entries
        exceeds length(t)/2 or by remove(x) when the number of data entries is less
        than length(t)/8. We find the smallest non-negative integer d such that2^d >= 3n.
        We reallocate the array(t) so that it has size $ 2^d, and then we insert all
        the elements in the old version of t into the newly-resized copy of t While
        doing this, we reset q equal to n since the newly-allocated t contains no del
        values.
        '''

        while((2**self.d) < 3*n):
            self.d+=self.d

        old_table = self.table
        self.max_length = 2**self.d
        self.table = [None] * self.max_length
        self.q = self.n

        for x in old_table:
            if x != None and x != self.del:
                i = hash(x)
                while self.table[i] != None:
                    i = (i+1) % self.max_length
                self.table[i] = x
