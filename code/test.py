from lib.Ebay import Ebay
from lib.Category import Category
from lib.FileHandle import FileHandle

# categories = Ebay.getCategories();

# for cat in categories:
# 	print(cat);

catObj = Category();
#catObj.createTable();
#catObj.store(categories);
categories2 = catObj.getCategories();
for cat in categories2:
	print(cat);
#print (catObj.getCategoriesById(33333333333));

#FileHandle.saveFile('183627.html', catObj.detGetCategoryHtml(183627));