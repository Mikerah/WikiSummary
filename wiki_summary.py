import argparse
import wikipedia

def create_optional_arguments(parser):
    """ Given a parser, create optional arguments."""

    parser.add_argument('-R', '--random', help='display n random wikipedia articles (1 <= n <= 10)', \
                        type=int, choices=[i for i in range(1,11)])
                        
    parser.add_argument('-r', '--read', help='display the specified summarized wikipedia article', type=str)

    parser.add_argument('-rf', '--forever', help='display a random article until the user types stop', \
                        action="store_true")

def get_random_articles_v1(number_of_articles_wanted):
    """Given the wanted number of articles returned, get random wikipedia articles"""
    if number_of_articles_wanted == 1:
        print(wikipedia.summary(wikipedia.random()))
    else:    
        list_of_articles = wikipedia.random(number_of_articles_wanted)
        try:
            for a in list_of_articles:
                article = a[:]
                if ('disambiguation' in wikipedia.page(a).title) or ('it may refer to' in wikipedia.page(a).title):
                    list_of_articles.remove(a)
                    list_of_articles.append(wikipedia.random())
                    
                print(list_of_articles.index(a)+1," - "+wikipedia.summary(a))
                print()
        except wikipedia.exceptions.DisambiguationError:
            list_of_articles.remove(article)
            list_of_articles.append(wikipedia.random(article))
            
def get_random_articles_v2():
    """Retrieves random articles until the user types 'stop' """
    ans = input('Press enter to continue or stop to stop: ')
    while ans != 'stop':
        try:
            print(wikipedia.summary(wikipedia.random()))
            print()
            ans = input('Press enter to continue or stop to stop: ')
        except wikipedia.exceptions.DisambiguationError:
            print(wikipedia.summary(wikipedia.random()))
            print()
            ans = input('Press enter to continue or stop to stop: ')
            
def get_wanted_article(search_term):
    """Given a search term, find the associated article"""
    list_of_associated_articles = wikipedia.search(search_term)
    wanted_article = list_of_associated_articles[0]
    print(wikipedia.summary(wanted_article))
    print()
    
def choice(args):
    """ Given a namespace, determine what to do based of the parameters given. """
    if args.random:
        return get_random_articles_v1(args.random)
    elif args.read:
        return get_wanted_article(args.read)
    elif args.forever:
        return get_random_articles_v2()
        
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Read Wikipedia Articles in your command prompt.")
    create_optional_arguments(parser)
    args = parser.parse_args()
    choice(args)