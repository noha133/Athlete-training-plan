from datetime import datetime,timedelta

names = ["Recovery", "Build1", "Build2", "Key"]
def get_inputs(start_date,end_date):
    try:
        start_date_todate = datetime.strptime(start_date, "%A %dth of %B %Y")
        end_date_todate = datetime.strptime(end_date, "%A %dth of %B %Y")
        weeks=round((end_date_todate-start_date_todate).days/7)
        if(weeks>=8):
            print_test_weeks(start_date_todate,end_date_todate,weeks)
        # return weeks
        else:
            print("Weeks<8")
    except ValueError:
        print("Your input is not valid")

def print_test_weeks(start_week,end,weeks):
    for i in range(2):
        end_week = start_week+timedelta(days=6)
        print(f'Week #{i+1} - Test - from {start_week.day} {start_week.strftime("%B")} to {end_week.day} {end_week.strftime("%B")}')
        start_week = end_week + timedelta(days=1)
    Filler_MainBlocks(weeks,start_week,end_week)




def Filler_MainBlocks(weeks,start_week,end_week):

    a=int((weeks-8)%4)
    if(a==1):
        start_week = end_week + timedelta(days=1)
        end_week = start_week + timedelta(days=6)
        print(f'Week #3 - Filler - from {start_week.day} {start_week.strftime("%B")} to {end_week.day} {end_week.strftime("%B")}')
        Range=weeks-5
        start_block=4
        start_list=0
        print_MainBlock(start_week, end_week, Range, start_list, start_block)


    if (a == 2):
        start_list=2
        Range = weeks - 4
        start_block = 3
        print_MainBlock(start_week, end_week, Range, start_list, start_block)


    if (a == 3):
        start_list = 1
        Range = weeks - 4
        start_block = 3
        print_MainBlock(start_week, end_week, Range, start_list, start_block)


    print_Taper_Racer(weeks,start_week, end_week)

def print_MainBlock(start_week, end_week, Range, start_list, start_block):
    s=start_list
    for i in range(Range):
        start_week = end_week + timedelta(days=1)
        end_week = start_week + timedelta(days=6)
        print(
            f'Week #{start_block + i} - {names[s]} - from {start_week.day} {start_week.strftime("%B")} to {end_week.day} {end_week.strftime("%B")}')
        s = s + 1
        if (s == 4):
            s = 0

def print_Taper_Racer(weeks,start_week,end_week):
    names = ["Taper", "Racer"]
    for i in range(2):
        start_week = end_week + timedelta(days=1)
        end_week = start_week+timedelta(days=6)
        print(f'Week #{weeks-1} - {names[i]} - from {start_week.day} {start_week.strftime("%B")} to {end_week.day} {end_week.strftime("%B")}')
        weeks=weeks+1









start_date = str(input('Enter date(Sunday 6th of June 2021: '))
end_date = str(input('Enter date(Sunday 6th of June 2021: '))
week=get_inputs(start_date,end_date)





