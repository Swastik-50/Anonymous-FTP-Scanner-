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

# Example usage
check_anonymous_ftp('127.0.0.1')