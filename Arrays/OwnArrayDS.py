class MyOwnArray:
    def __init__(self):
        self.length = 0
        # we cannot use list. Need to use dict
        self.data = {}

    def __str__(self):
        return str(self.__dict__)


    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length = self.length + 1


    def pop(self):
        # we have to decrement the index at [length-1] because we increment the length after each push() so that
        # the new element can be inserted at the position of the incremented length
        print("The deleted element is ", self.data[self.length-1])
        del self.data[self.length-1]
        self.length = self.length-1

    def delete(self, index):
        print("The deleted element is ", self.data[index])
        # including self.length-1 because the limit is excluded in range()
        for item in range(index, self.length-1):
            #swapping the elements on the right of the index position to be deleted
            self.data[item] = self.data[item+1]
        #deleting the last element in the array because the swapping is complete and the last element has been copied to
        #the previous position thus making the last element obsolete
        del self.data[self.length-1]
        #updating length because the last element is obsolete
        self.length = self.length-1


    def printArray(self):
        print("The elements in the array are: ")
        for items in self.data:
            print(self.data[items])


myownarray = MyOwnArray()
myownarray.push('a')
myownarray.push('b')
myownarray.push('c')
myownarray.delete(0)
myownarray.push('a')

myownarray.printArray()


















