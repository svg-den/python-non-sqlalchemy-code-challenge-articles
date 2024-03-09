# Class variablesfor Storing all instances of Article
class Article:
    all = []
    def __init__(self, author, magazine, title):
 # Initializing Article object with author, magazine, and title.
        self.author = author
        self.magazine = magazine
#Ensure the title is a string.
        self._title = str(title) 
#Ensure current article instance to the list of articles.
        Article.all.append(self)

    @property
    def title(self):
# Getter method to retrive title of article.
        return self._title

    @title.setter
    def title(self, title):
        return self.title 
 # Title is immutable raising an AttributeError exception if tried to change it.
        raise AttributeError("Title is immutable")
        

class Author:
    def __init__(self, name):
# Initialize author object with name.
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_names):
        self.new_names = new_names
        return self._name
    
    def articles(self):
# Returns a list of articles written by the author.
        return [articles for articles in Article.all if articles.author == self]

    def magazines(self):
# Returns a list of articles written by the author.
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
# Creates and returns a new article given a magazine and title.
        articles = Article(self, magazine, title)
        return articles

    def topic_areas(self):
# Returns a list of topic areas for all articles written by the author.
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

    def contributing_authors(self):
# Returns a list of authors who have written more than 2 articles for the magazine.
        return [authors for authors in Author.all if len(authors.articles()) > 0]

class Magazine:
    def __init__(self, name, category):
        # Initialize Magazine object with name and category.
        self._name = name
        self._category = category
    
    @property
    def name(self):
        # Getter method for retrieving the name of the magazine
        return self._name
    
    @property
    def category(self):
        # Getter method for retrieving the category of the magazine
        return self._category
    
    @name.setter
    def name(self, new_names):
        # Setter method for updating the name of the magazine
        if isinstance(new_names, str):
            # Ensuring the new name meets length constraints
            if 2 <= len(new_names) <= 16:
                self._name = new_names
        return self._name
    
    @category.setter
    def category(self, new_categories):
        # Setter method for updating the category of the magazine
        if isinstance(new_categories, str):
            # Ensuring the new category is non-empty
            if len(new_categories) > 0:
                self._category = new_categories
        return self._category
    
    def articles(self):
        # Returns a list of articles associated with this magazine
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        # Returns a list of authors who have contributed to this magazine
        return list(set([articles.author for articles in self.articles()]))

    def article_titles(self):
        # Returns a list of titles of articles published in this magazine
        titles = [articles.title for articles in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # Returns a list of authors who have contributed more than 2 articles to the magazine
        authors = {}
        for articles in self.articles():
            if articles.author in authors:
                authors[articles.author] += 1
            else:
                authors[articles.author] = 1
        contributing_authors = [author for author, count in authors.items() if count > 2]
        return contributing_authors if contributing_authors else None
