scanned_hosts = 50
found_vulnerable = 8

vulnerable_machine = found_vulnerable / scanned_hosts * 100

print(vulnerable_machine > 10 )

print(f"{vulnerable_machine:g}% of the scanned hosts are vulnerable")