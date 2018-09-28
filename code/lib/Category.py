import sqlite3

class Category:

	def __init__(self):
		self.connection = sqlite3.connect('test.db');

	def test():
		print ("Test Category");

	def createTable(self):
		c = self.connection.cursor();
		c.execute("CREATE TABLE categories (id real, name text, level real, parent_id real)");
		self.connection.commit();

	def deleteTable(self):
		c = self.connection.cursor();
		c.execute("DROP TABLE categories");
		self.connection.commit();

	def store(self, categories):
		c = self.connection.cursor();
		c.executemany('INSERT INTO categories VALUES (?,?,?,?)', categories)
		self.connection.commit();

	def getCategories(self):
		c = self.connection.cursor();
		c.execute('SELECT * FROM categories ORDER BY parent_id ASC');
		return c.fetchall();

	def getCategoriesById(self, id=0):
		c = self.connection.cursor();
		c.execute('SELECT * FROM categories WHERE id = ?', (id,));
		return c.fetchone();

	def getCategoriesByParent(self, parent_id=0):
		c = self.connection.cursor();
		c.execute('SELECT * FROM categories WHERE parent_id = ?', (parent_id,));
		return c.fetchall();

	def getCategoryChildrenHtml(self, category_id, max = 0):
		categories = self.getCategoriesByParent(category_id); 
		html = "";
		if ( len(categories) > 0 ):
			html += "<ul>"
			for cat in categories: 
				html += "<li>";
				html += cat[1];
				html += self.getCategoryChildrenHtml(cat[0], max+1);
				html += "</li>";
			html += "</ul>";
		return html;

	def detGetCategoryHtml(self, category_id):
		category = self.getCategoriesById(category_id);
		if category is not None: 
			html = "<h1>"+category[1]+" - "+str(category[2])+"</h1>";
			html += self.getCategoryChildrenHtml(category_id);
		else: 
			html = "Error";
		return html;

