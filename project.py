from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Alt.: supply an anonmymous callback function to print a simple progress bar to screen
# local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))

# Alt. 2: a progress bar with reduced output (every 1000 blocks)
# local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

local_file = open('local_copy.log')

whole_list = []
for i in local_file:
  whole_list.append(i)
  #Puts each line of file as seperate character in a list

x = 0
for i in whole_list:
  x = x + 1
  # Counts every line in list giving total request count

File = []
Code = []
x = 0
for i in whole_list:
    whole_split = whole_list[x].split(' ')
    if len(whole_split) > 9:
        File.append(whole_split[6])
        Code.append(whole_split[8])
    x = x + 1

 

word_counter = {}
for word in File:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

#print(word_counter)
popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
top_3 = popular_words[:3]
print(top_3)

code_counter = {}
for code in Code:
    if code in code_counter:
        code_counter[code] += 1
    else:
        code_counter[code] = 1

#print(code_counter)
popular_code = sorted(code_counter, key = code_counter.get, reverse = True)
top = popular_code[:3]
print(top)

 
