import argparse

parser = argparse.ArgumentParser(description="Read Wikipedia Articles in your command prompt.")

##### Creating paramaters #####

parser.add_argument('-R', '--random', help='display n random wikipedia articles (1 <= n <= 10)', \
                    type=int, choices=[i for i in range(1,11)])
                    
parser.add_argument('-r', '--read', help='display the specified summarized wikipedia article', type=str)

args = parser.parse_args()