class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        # if not isinstance(author, Author):
        #     raise ValueError("Author must be an instance of the Author class.")
        # if not isinstance(magazine, Magazine):
        #     raise ValueError("Magazine must be an instance of the Magazine class.")
        # if not isinstance(title, str) or not (5 <= len(title) <= 50):
        #     raise ValueError("Title must be a string between 5 and 50 characters.")
        # if hasattr(self, '_title'):
        #     raise AttributeError("Title cannot be changed after instantiation ")
        
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, "_title") :
            self._title = title    
    @property
    def author(self) :
        return self._author 
    @author.setter
    def author(self, author) :
        if not isinstance(author, Author) :
            raise ValueError("Author must be an instance of the Author class")
        else :
            self._author = author    
    @property 
    def magazine(self):
        return self._magazine 
    @magazine.setter 
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine) :
            raise ValueError("Magazine must be an instance of the Magazine class")
        else :
            self._magazine = magazine                          

class Author:
    def __init__(self, name):
        # if not isinstance(name, str) or len(name) == 0:
        #     raise ValueError("Name must be a non-empty string.")
        # if hasattr(self, '_name'):
        #     raise AttributeError("Name cannot be changed after instantiation.")
        self._name = name
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name, str) and not len(name) == 0 and not hasattr(self, "_name") :
            self._name = name

    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        categories = list(set(magazine.category for magazine in self.magazines()))
        return categories if categories else None


class Magazine:
    all = []
    
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        
        self._name = name
        self._category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list(set(article.author for article in self.articles()))
    
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        frequent_authors = [author for author in set(authors) if authors.count(author) > 2]
        return frequent_authors if frequent_authors else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)



   