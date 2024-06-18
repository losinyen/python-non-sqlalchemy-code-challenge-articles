class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instance of the Author class")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of the Magazine class")
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not hasattr(self, 'title'):
            self._title = ""
        if isinstance(new_title, str) and (5 <= len(new_title) <= 50):
            self._title = new_title
        else:
            raise ValueError("Title must be of type str and between 5 and 50 characters")


class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name != "" and not hasattr(self, 'name'):
            self._name = name
        else:
            raise ValueError("Name must be of type str and must not be empty")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def add_magazine(self, magazine):
        return [self, magazine]

    def topic_areas(self):
        if self.articles():
            return list(set(article.magazine.category for article in self.articles()))
        else:
            return None

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be of type str and between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be of type str and more than 0 characters")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        author_article_count = {}
        for article in self.articles():
            if isinstance(article.author, Author):
                if article.author in author_article_count:
                    author_article_count[article.author] += 1
                else:
                    author_article_count[article.author] = 1
        return [author for author, count in author_article_count.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        magazines_with_articles = [magazine for magazine in cls.all if magazine.articles()]

        if magazines_with_articles:
            return max(magazines_with_articles, key=lambda magazine: len(magazine.articles()))
        else:
            return None
