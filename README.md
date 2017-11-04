# fsbrute
fsbrute is ftp and ssh login bruter multithread program.
I'll add -u root options soon!

                    _____       ___.                    __           
                  _/ ____\______\_ |__ _______  __ __ _/  |_   ____  
                  \   __\/  ___/ | __ \\_  __ \|  |  \\   __\_/ __ \ 
                  |  |  \___ \  | \_\ \|  | \/|  |  / |  |  \  ___/ 
                  |__| /____  > |___  /|__|   |____/  |__|   \___  >
                            \/      \/                           \/ 
        
                by : fahri314
                

    fsbrute.py version 1.0
    Brute forcing ftp or ssh target
    Programmmer : Fahri Guresci
    Edited time : 09-08-2017
    fahri314[at]gmail[dot]com

    Usage: ./fsbrute.py [options]
    Options: -t, --target       <hostname/ip>    |   target to bruteforcing 
             -c, --combolist    <combolist>      |   combolist for bruteforcing
             -h, --help         <help>           |   print this help
             -b, --bot          <bot>            |   bot count
                                                  
    Example   : ./fsbrute.py -t 192.168.1.1 -c combolist.txt -b 10 ftp

