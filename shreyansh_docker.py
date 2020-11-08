import os
            import subprocess as sr
            import socket
            while True: 
                os.system('clear')
                print("\n\n\t 1. To install docker\n\t 2. To start docker services\n\t 3. O.S to install\n\t 4. Exit")
                a= input("Enter your choice ")
                if a=='1':
                    op=sr.getstatusoutput('dnf install docker-ce --nobest')
                    if op[0]==0:
                        print("Docker installed successfully")
                    input("Press enter button to continue...")
                elif a=='2':
                    print("Start docker permanently")
                    x=input("yes/no\n")
                    if x=='yes':
                        op=sr.getstatusoutput('systemctl start docker')
                        op=sr.getstatusoutput('systemctl enable docker')
                    else:
                        op=sr.getstatusoutput('systemctl start docker')
                elif a=='3':
                    print('''\nSelect O.S to install and run
                    \n\t\t1. Ubuntu
                    \n\t\t2. Centos
                    \n\t\t3. Amazonlinux''')
                    ch=input("Enter your choice\n")
                    if ch=='1':
                        ver=input("Enter version of O.S : ")
                        print('\n\t\tPlease wait...')
                        op=sr.getstatusoutput('docker pull ubuntu:{}'.format(ver))
                        os.system ('clear')
                        os.system('docker run -it ubuntu:{}'.format(ver))
                    elif ch=='2':
                        ver=input("Enter version of O.S : ")
                        print('\n\t\tPlease wait...')
                        op=sr.getstatusoutput('docker pull centos:{}'.format(ver))
                        os.system('clear')
                        os.system('docker run -it centos:{}'.format(ver))
                    elif ch=='3':
                        ver=input("Enter version of O.S : ")
                        print('\n\t\tPlease wait...')
                        op=sr.getstatusoutput('docker pull amazonlinux:{}'.format(ver))
                        os.system('clear')
                        os.system('docker run -it amazonlinux:{}'.format(ver))
                elif a=='4':
                    os.system('clear')
                    exit()
