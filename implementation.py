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

	data_storage = []

    def __init__(self, *args, BaseBin):

    	self.*args = *args
    	self.BaseBin = BaseBin


    def MyStruct(self, data_storage, *args):

    	self.*args = data

    	if all(data) != True:
    		
    		return "Not all items are iterable"

    	else:	
    		for element in data:
    			
    			for it in element:
    				data_storage.append(temp)
    				data_storage.sort()

    			return "Elements are added to data-storage. \nYour data-storage now is : {0}.".format(" ,".join(data_storage))


    def Search(self, BaseBin, data_storage, target)
		
    	self.data_storage = items
    	self.target = target

    	return Search(self, items, target)


    def In(self, BaseBin, data_storage, target):

    	self.data_storage = items
    	self.target = target

    	return BaseBin.Search(self, items, target) != -1




class StringBin(BaseBin):

	data_storage = 0

    def __init__(self, *args, BaseBin):

        self.*args = *args
        self.BaseBin = BaseBin


    def Search(self, BaseBin, items, target):

    	self.BaseBin = BaseBin
    	self.items = items
    	self.target = target

    	for item in items:

    		if type(item) != str:

    			return "Elements are not string"
    	
    	return BaseBin.Search(self, items, target)
