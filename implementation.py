class BaseBin:

    items = []

    def Search(self, items, target):

        self.items = items
        self.target = target
        
        min_ = 0
        max_ = len(items) - 1


        while min_ <= max_:
            mid = (max_ + min_) // 2

            if items[mid] == target:
            
                if items[mid - 1] == target:

                    while items[mid - 1] == target:
                        mid -= 1

                else:
                    return mid 

            if target > items[mid]:
                min_ = mid + 1
            else:
                max_ = mid - 1

        return - 1




class IntBin(BaseBin):

    def __init__(self, *args):

        self.args = args


    def IntBinSearch(self, target):

        intbin_items = []

        self.target = target

        for element in self.args:

            if type(element) in (list, tuple, set):

                for it in element:
                        intbin_items.append(int(it))

            elif type(element) == int:
                    intbin_items.append(int(element))

            else:

                    return "TypeError: not all numbers are integers."

            intbin_items.sort()

        return BaseBin.Search(self, intbin_items, target)


    def In(self, target):

        intbin_items = []

        self.target = target


        for element in self.args:

            if type(element) in (list, tuple, set):

                for it in element:
                    intbin_items.append(int(it))

            elif type(element) == int:
                intbin_items.append(int(element))

            else:

                return "TypeError: not all numbers are integers."

        intbin_items.sort()

        return BaseBin.Search(self, intbin_items, target) != -1




class StringBin(BaseBin):

    stringbin_items = []

    def __init__(self, *args):

        self.args = args


    def StringBinSearch(self, target):

        self.target = target

        for element in self.args:

            if type(element) != str:

                return "TypeError: not all elements are string."

        return BaseBin.Search(self, self.args, target)



numbers = BaseBin()
print(numbers.Search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
print(numbers.Search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 21))


numbers = IntBin(1,2,3,4,5,6,7,8)
print(numbers.IntBinSearch(3))
print(numbers.IntBinSearch(9))
print(numbers.In(3))
print(numbers.In(12))


string = StringBin("a", "b" ,"c" ,"d", "e", "f")
print(string.StringBinSearch("c"))
print(string.StringBinSearch("h"))



