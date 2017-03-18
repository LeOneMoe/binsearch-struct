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

        if isinstance(args[1], (set, tuple, list)):

            for element in args:

                if isinstance(element, int):
                    self.items.append(element)

                else:
                    raise TypeError("Not all elements are integer")

        elif isinstance(args[1], int):

            for element in args:

                if isinstance(element, int):
                    self.items.append(element)

                else:
                    raise TypeError("Not all elements are integer")

        else:
            raise TypeError("Not suported type")

        self.items.sort()

        print(self.items)



    def __contains__(self, target):

        return self._search(self.items, target) != -1


    def search(self, target):

        return self._search(self.items, target)




class StringBin(BaseBin):

    items = []

    def __init__(self, *args):

        if isinstance(args[1], (set, tuple, list)):

            for element in args:

                if isinstance(element, str):
                    self.items.append(element)

                else:
                    raise TypeError("Not all elements are string")

        elif isinstance(args[1], str):

            for element in args:

                if isinstance(element, str):
                    self.items.append(element)

                else:
                    raise TypeError("Not all elements are string")

        else:
            raise TypeError("Not suported type")

        self.items.sort()

        print(self.items)


    def search(self, target):

        self.target = target

        return self._search(self.items, target)
