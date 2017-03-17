class BaseBin:

    items = []

    def search(self, items, target):

        self.items = items
        self.target = target
        
        min_ = 0
        max_ = len(items) - 1


        while min_ <= max_:
            mid = (max_ + min_) // 2

            if items[mid] == target:

                while items[mid - 1] == target:
                        mid -= 1

                return mid

            if target > items[mid]:
                min_ = mid + 1
            else:
                max_ = mid - 1

        return - 1




class IntBin(BaseBin):

    items = []

    def __init__(self, *args):

        self.args = args


    def __contains__(self, target):

        self.target = target


        for element in self.args:

            if type(element) in (list, tuple, set):

                for it in element:
                    self.items.append(int(it))

            elif type(element) == int:
                self.items.append(int(element))

            else:

                return "TypeError: not all numbers are integers."

        self.items.sort()

        if BaseBin.search(self, self.items, self.target) != -1:

            return True


    def _search(self, target):

        items = []

        self.target = target

        for element in self.args:

            if type(element) in (list, tuple, set):

                for it in element:
                        items.append(int(it))

            elif type(element) == int:
                    items.append(int(element))

            else:

                    return "TypeError: not all numbers are integers."

            items.sort()

        return BaseBin.search(self, items, target)




class StringBin(BaseBin):

    items = []

    def __init__(self, *args):

        self.args = args


    def _search(self, target):


        self.target = target

        for element in self.args:

            if type(element) != str:

                return "TypeError: not all elements are string."

            else:
                self.items.append(element)

        self.items.sort()

        return BaseBin.search(self, self.items, target)



numbers = BaseBin()
print(numbers.search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
print(numbers.search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 21))
print(numbers.search([0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9], 4))


numbers = IntBin(1,2,3,4,5,6,7,8)
print(numbers._search(3))
print(numbers._search(9))
print(5 in numbers)
print(10 in numbers)


string = StringBin("a", "b" ,"c" ,"d", "e", "f")
print(string._search("c"))
print(string._search("h"))



