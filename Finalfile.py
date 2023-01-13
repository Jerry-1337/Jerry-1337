def interest( ):
    print("×--×" * 8)
    print('Enter 1 to Start a program:  ')
    i = int(input())
    while i == 1:
        am = int(input('Enter amount: '))
        it = float((input('Enter interest rate: ')))
        xday = int(input('Start Day: '))
        xmonth = int(input('Start Month: '))
        xyear = int(input('Start Year: '))
        zday = int(input('End Day: '))
        zmonth = int(input('End Month: '))
        zyear = int(input('End Year: '))
        xtotal = (xyear * 360) + (xmonth * 30) + xday
        ztotal = (zyear * 360) + (zmonth * 30) + zday
        dxz = ztotal - xtotal 
        it_d = ((am * it) / 100) /30
        it_t = dxz * it_d
        print(f"Interest ===>> {round(it_t, 2)} kyats")
        # year calculation
        if (dxz > 360):    	
            year = dxz / 360   
            if (year < 1):
                print(f">> {int(year)} year")
            else:
            	print(f">> {int(year)} years")
           # month calculation
            mmm = dxz % 360
            month = int(mmm / 30)
            if (month < 1):
                print(f">> {int(month)} month")
            else:
                print(f">> {int(month)} months")
            # day calculation
            ddd = int(mmm % 30)
            if (ddd == 1):
                print(f">> {ddd} day")
            else:
                print(f">> {ddd} days")
            
        # year calculation      
        else:
            print( ">> 0 year")
            # month calculation
            month = int(dxz / 30)
            if (month < 1):
                print(f">> {int(month)} month")
            else:
                print(f">> {int(month)} months")
            # day calculation
            ddd = int(dxz % 30)
            if (ddd == 1):
                print(f">> {ddd} day")
            else:
                print(f">> {ddd} days")
            
        print("-" * 20)
        print ("Developed by AungMyatSoe ")
        
        return interest ( )
   
    while i != 1:
        print("Restart the Program")
        return interest ( )

if __name__ == "__main__":
    interest ( )