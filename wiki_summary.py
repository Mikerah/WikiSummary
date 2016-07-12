import argparse
import wikipedia

def create_optional_arguments(parser):
    """ Given a parser, create optional arguments."""

    parser.add_argument('-R', '--random', help='display n random wikipedia articles (1 <= n <= 10)', \
                        type=int, choices=[i for i in range(1,11)])
                        
    parser.add_argument('-r', '--read', help='display the specified summarized wikipedia article', type=str)

    parser.add_argument('-rf', '--forever', help='display a random article until the user types stop')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Read Wikipedia Articles in your command prompt.")
    create_optional_arguments(parser)
    args = parser.parse_args()