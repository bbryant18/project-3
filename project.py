from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Alt.: supply an anonmymous callback function to print a simple progress bar to screen
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))

# Alt. 2: a progress bar with reduced output (every 1000 blocks)
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

# Open desired file to read and make code for
local_file = open('local_copy.log')

# Sort out log file to seperate correct lines from lines with errors
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
percent_of_errors = ((error/correct)*100)

# Determine how many requests were made per day, per week, and per month
mon = 0
tues = 0
wed = 0
thurs = 0
fri = 0
sat = 0
sun = 0
Mon = []
Tues = []
Wed = []
Thurs = []
Fri = []
Sat = []
Sun = []
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
Sixth_Week = 0
first = []
second = []
third = []
fourth = []
fifth = []
sixth = []
File = []
Code = []
a = 0
day = 0
week = 4
month = 0

for i in correct_list:
    whole_split = correct_list[a].split(' ')
    previous_day = correct_list[a - 1].split(' ')
    # If day on current line doesn't match with day on previous line increment day
    if whole_split[3][1:3] != previous_day[3][1:3]:
        if day == 1:
            Mon.append(mon)
            mon = 0
        elif day == 2:
            Tues.append(tues)
            tues = 0
        elif day == 3:
            Wed.append(wed)
            wed = 0
        elif day == 4:
            Thurs.append(thurs)
            thurs = 0
        elif day == 5:
            Fri.append(fri)
            fri = 0
        elif day == 6:
            Sat.append(sat)
            sat = 0
        elif day == 7:
            Sun.append(sun)
            sun = 0
        day += 1
    # If month on current line doesn't match with month on previous line increment month and resets month
    if whole_split[3][4:7] != previous_day[3][4:7]:
        # This is supposed to create a new file for each month
        if month == 1:
            newfile = open("Oct.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 2:
            newfile = open("Nov.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 3:
            newfile = open("Dec.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 4:
            newfile = open("Jan.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 5:
            newfile = open("Feb.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 6:
            newfile = open("Mar.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 7:
            newfile = open("Apr.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 8:
            newfile = open("May.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 9:
            newfile = open("Jun.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 10:
            newfile = open("Jul.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 11:
            newfile = open("Aug.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        elif month == 12:
            newfile = open("Sep.txt","w+")
            newfile.write("First Week = %s\n" % first[:1] + "Second Week = %s\n" % second[:1] + "Third Week = %s\n" % third[:1] + "Fourth Week = %s\n" % fourth[:1] + "Fifth Week = %s\n" % fifth[:1] + "Sixth Week = %s\n" % sixth[:1])
            newfile.close
        month += 1
        if week == 4:
            fourth.append(Fourth_Week)
            Fourth_Week = 0
        elif week == 5:
            fifth.append(Fifth_Week)
            Fifth_Week = 0
        elif week == 6:
            sixth.append(Sixth_Week)
            Sixth_Week = 0
        week = 1   
    # Resets days when it gets back to beginning of the week and increments week
    x = day % 8
    if x == 0:
        day = 1
        if week == 1:
            first.append(First_Week)
            First_Week = 0
        elif week == 2:
            second.append(Second_Week)
            Second_Week = 0
        elif week == 3:
            third.append(Third_Week)
            Third_Week = 0
        elif week == 4:
            fourth.append(Fourth_Week)
            Fourth_Week = 0
        elif week == 5:
            fifth.append(Fifth_Week)
            Fifth_Week = 0
        elif week == 6:
            sixth.append(Sixth_Week)
            Sixth_Week = 0
        week += 1
        
    # Resets months when it gets back to beginning of the year
    z = month % 13
    if z == 0:
        month = 1
    # Increments count of days based on what day of week it is
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
    # Increments count in each week based on which week of month it is 
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
    elif week == 6:
        Sixth_Week += 1
    # Increments count in each month based on which month it is
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
    # Appends Files to a list called File
    File.append(whole_split[6])
    # Appends Status Codes to a list called Codes
    Code.append(whole_split[8])
    a = a + 1



# Finds number of 3xx and 4xx Status Codes in log
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

#print("\nStatus 3xx = ", status_3xx)
#print("Status 4xx = ", status_4xx)
percent_of_4xx = ((status_4xx/(status_3xx+status_code))*100)
percent_of_3xx = ((status_3xx/(status_4xx+status_code))*100)


# Puts file name(key) and number of times that file name is called(value) into a dictionary
word_counter = {}
for word in File:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

# Finds and counts files that were only requested once
File_count = 0
Least_requested = []
for key, value in word_counter.items():
    if value == 1:
        Least_requested.append(key)
        File_count += 1

# Finds the most requested file
popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
#print(popular_words)
top_File = popular_words[:1]

    
print("1.   Total number of requests in lof file = ", (correct + error))
print("     Number of correct requests in log file = ", correct)
print("     Percent of errors removed in log file = %.2f" %percent_of_errors )

print("\n2.   Average number of requests on Mondays = %.2f" %(sum(Mon)/len(Mon)))
print("     Average number of requests on Tuesdays = %.2f" %(sum(Tues)/len(Tues)))
print("     Average number of requests on Wednsdays = %.2f" %(sum(Wed)/len(Wed)))
print("     Average number of requests Thursdays = %.2f" %(sum(Thurs)/len(Thurs)))
print("     Average number of requests on Fridays = %.2f" %(sum(Fri)/len(Fri)))
print("     Average number of requests on Saturdays = %.2f" %(sum(Sat)/len(Sat)))
print("     Average number of requests on Sundays = %.2f" %(sum(Sun)/len(Sun)))
print("\n     Average number of requests for the First week of month = %.2f" %(sum(first)/len(first)))
print("     Average number of requests for the Second week of month = %.2f" %(sum(second)/len(second)))
print("     Average number of requests for the Third week of month = %.2f" %(sum(third)/len(third)))
print("     Average number of requests for the Fourth week of month = %.2f" %(sum(fourth)/len(fourth)))
print("     Average number of requests for the Fifth week of month = %.2f" %(sum(fifth)/len(fifth)))
print("     Average number of requests for the Sixth week of month = %.2f" %(sum(sixth)/len(sixth)))
print("\n     Total in January = ",Jan)
print("     Total in Febuary = ", Feb)
print("     Total in March = ", Mar)
print("     Total in April = ", Apr)
print("     Total in May = ", May)
print("     Total in June = ", Jun)
print("     Total in July = ", Jul)
print("     Total in August = ", Aug)
print("     Total in September = ", Sep)
print("     Total in October = ", Oct)
print("     Total in November = ", Nov)
print("     Total in December = ", Dec)

print("\n3.   Percent of 4xx status codes = %.2f" %percent_of_4xx )
print("\n4.   Percent of 3xx status codes = %.2f" %percent_of_3xx )

print("\n5.   The most requested file is: ")
for i in top_File:
    print("         ",i)
print("\n6.   There were",File_count,"file(s) requested only once")
print("     Here are a few of those files:")
for i in Least_requested[0:5]:
    print("         ",i)
    

