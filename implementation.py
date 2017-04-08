class BaseBin:

    items = []

    def search(self, target):

        raise NotImplementedError('Method `search` must be implemented')


    def _search(self, items, target):

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

    def __init__(self, *args):

        if len(args) > 0 and isinstance(args[0], (set, tuple, list)):

            for element in args[0]:

                if isinstance(element, int):
                    self.items.append(element)

                else:
                    raise TypeError("Not all elements are integer")

        elif len(args) > 0:

            for element in args:

                if isinstance(element, int):
                    self.items.append(element)

                else:
                    raise TypeError("Not all elements are integer")

        else:
            raise TypeError("Not suported type or empty input")

        self.items.sort()


    def __contains__(self, target):

        return self._search(self.items, target) != -1


    def search(self, target):

        return self._search(self.items, target)




class StringBin(BaseBin):

    items = []

    def __init__(self, *args):

        if len(args) > 0 and isinstance(args[0], (set, tuple, list)):

            for element in args[0]:

                if isinstance(element, str):
                    self.items.append(element)

                else:
                    raise TypeError("Not all elements are string")

        elif len(args) > 0:

            for element in args:

                if isinstance(element, str):
                    self.items.append(element)

                else:
                    raise TypeError("Not all elements are string")

        else:
            raise TypeError("Not suported type or empty input")

        self.items.sort()


    def search(self, target):

        self.target = target

        return self._search(self.items, target)


    def __contains__(self, target):

        return self._search(self.items, target) != -1



integers = IntBin(1, 5, 2, 7, 9, 9, 4)
print(integers.search(5) == 3)
print(integers.search(1) == 0)
print(integers.search(9) == 5)
print((4 in integers) == True)
print((10 in integers) == False)

strings = StringBin(['a', 'mama', 'papa', 'papa', 'vasa', 'kola'])
print(strings.search('mama') == 2)
print(strings.search('a') == 0)
print(strings.search('papa') == 3)
print(('vasa' in strings) == True)
print(('olala' in strings) == False)
