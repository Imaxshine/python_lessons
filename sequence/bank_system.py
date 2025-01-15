def Bank_system():
    try:
        print()
        import random
        # Compare user credentials
        print('Enter your NMB credentials')
        print('----------------------------')
        print('Enter your name:')
        userName = str(input())
        print('Enter your password')
        password = str(input())
        # ============Temple credentials storage===========
        saved_name = 'Emmanueli'
        saved_password = 'Imax8056'
        # =================================================
        if userName != saved_name or password != saved_password:
            print('Your credentials are invalid')
        else:
            repeat = '1'
            while repeat == '1':
                account_database = open(r'C:\Users\DELL\Desktop\project\sequence\account_balance.txt','r')
                read_amount = account_database.readline()
                account_database.close()
                main_balance = read_amount.rstrip()
                print('-----------------------\t------------------------')
                print('Welcome back Dear. {},'.format(userName),end='')
                print(' Your NMB account balance is Tsh.',format(float(main_balance), ',.2f'),sep='')
                print()
                print('Deposit some amount to your NMB account. Deposit amount not les than Tsh.',format(1000, ',.2f'))
                amount = float(input())
                print('---------------\t-----------------')
               
                current_balance = read_amount.rstrip()
                current_balance2 = float(current_balance)
                newBalance = current_balance2 + amount
                while amount < 1000:
                    print('Your deposit amount is les than Tsh.',format(1000, ',.2f'),' inter required amount.')
                    amount = float(input())
                print('Code ',random.randint(10000000000,90000000000),' Verifying that you have deposit Tsh.',format(amount, ',.2f'),'\n',sep='')
                print('Your current NMB balance is Tsh.',format(newBalance,',.2f'),sep='')
                print('-------------------------------------------------')
                infile = open(r'C:\Users\DELL\Desktop\project\sequence\account_balance.txt','w')
                infile.write(str(newBalance))
                infile.close()
                repeat = str(input('press 1 to deposit new amount or 0 to stop: '))

            print()
            account_database2 = open(r'C:\Users\DELL\Desktop\project\sequence\account_balance.txt','r')
            read1 = account_database2.readline().rstrip() 
            account_database2.close()
            print('Code ',random.randint(10000000000,90000000000),' Verifying that you have deposit Tsh.',format(amount, ',.2f'),'\n','Your NMB balance is Tsh.',format(float(read1), ',.2f'),sep='')
            print('------------\t---------------------------\t--------------')
    except Exception as er:
        print(er)
Bank_system()
