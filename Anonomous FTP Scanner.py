from ftplib import FTP

def check_anonymous_ftp(host):
    try:
        with FTP(host) as ftp:
            ftp.login('anonymous', 'anonymous@example.com')
            print(f"[+] {host} allows anonymous FTP login")
            return True
    except:
        print(f"[-] {host} does not allow anonymous FTP")
        return False

#usage
check_anonymous_ftp('151.101.2.219') # Checking on website https://www.speedtest.net/
