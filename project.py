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

correct_list = []
error_list = []
correct = 0
error = 0

for i in local_file:
    length = i.split(' ')
    if len(length) != 10:
        error_list.append(i)
        error += 1
    else:
        correct_list.append(i)
        correct += 1
print("Correct requests = ", correct)
print("Percent of errors = ", (error/correct))

mon = 0
tues = 0
wed = 0
thurs = 0
fri = 0
sat = 0
sun = 0
Jan = 0
Feb = 0
Mar = 0
Apr = 0
May = 0
Jun = 0
Jul = 0
Aug = 0
Sep = 0
Oct = 0
Nov = 0
Dec = 0
First_Week = 0
Second_Week = 0
Third_Week = 0
Fourth_Week = 0
Fifth_Week = 0
File = []
Code = []
a = 0
day = 1
week = 4
month = 1
for i in correct_list:
    whole_split = correct_list[a].split(' ')
    next_day = correct_list[a - 1].split(' ')
    if whole_split[3][1:3] != next_day[3][1:3]:
        day += 1
    if int(whole_split[3][1:3]) > int(next_day[3][1:3]):
        month += 1
        week = 1
    x = day % 8
    z = month % 13
    if x == 0:
        day = 1
        week += 1
    if z == 0:
        month = 1
    if day == 1:
        mon += 1
    elif day == 2:
        tues += 1
    elif day == 3:
        wed += 1
    elif day == 4:
        thurs += 1
    elif day == 5:
        fri += 1
    elif day == 6:
        sat += 1
    elif day == 7:
        sun += 1
    if week == 1:
        First_Week += 1
    elif week == 2:
        Second_Week += 1
    elif week == 3:
        Third_Week += 1
    elif week == 4:
        Fourth_Week += 1
    elif week == 5:
        Fifth_Week += 1
    if month == 1:
        Oct += 1
    elif month == 2:
        Nov += 1
    elif month == 3:
        Dec += 1
    elif month == 4:
        Jan += 1
    elif month == 5: 
        Feb += 1
    elif month == 6:
        Mar += 1
    elif month == 7:
        Apr += 1
    elif month == 8:
        May += 1
    elif month == 9:
        Jun += 1
    elif month == 10:
        Jul += 1
    elif month == 11:
        Aug += 1
    elif month == 12:
        Sep += 1
    if len(whole_split) > 8:
        File.append(whole_split[6])
        Code.append(whole_split[8])
    a = a + 1

print("\nMonday = ", mon)
print("Tuesday = ", tues)
print("Wednsday = ", wed)
print("Thursday = ", thurs)
print("Friday = ", fri)
print("Saturday = ", sat)
print("Sunday = ", sun)
print("\nFirst week of month = ", First_Week)
print("Second week of month = ", Second_Week)
print("Third week of month = ", Third_Week)
print("Fourth week of month = ", Fourth_Week)
print("Fifth week of month = ", Fifth_Week)
print("\nJanuary = ",Jan)
print("Febuary = ", Feb)
print("March = ", Mar)
print("April = ", Apr)
print("May = ", May)
print("June = ", Jun)
print("July = ", Jul)
print("August = ", Aug)
print("September = ", Sep)
print("October = ", Oct)
print("November = ", Nov)
print("December = ", Dec)


word_counter = {}
for word in File:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

#print(word_counter)
popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
top_3 = popular_words[:1]
print("\n",top_3)

status_code = 0
status_4xx = 0
status_3xx = 0

for code in Code:
    if int(code) in range(400,499):
        status_4xx += 1
    elif int(code) in range(300,399):
        status_3xx += 1
    else:
        status_code += 1

print("\nStatus 3xx = ", status_3xx)
print("Status 4xx = ", status_4xx)
print("Percent of 4xx status codes = ", (status_4xx/(status_3xx+status_code)))
print("Percent of 3xx status codes = ", (status_3xx/(status_4xx+status_code)))

code_counter = {}
for code in Code:
    if code in code_counter:
        code_counter[code] += 1
    else:
        code_counter[code] = 1

print("\n",code_counter)
#popular_code = sorted(code_counter, key = code_counter.get, reverse = True)
#top = popular_code[:3]
#print(top)

 
