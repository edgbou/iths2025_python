#klar
test_tuple = ("SSH Login", "Port Scan", "File Upload", "SQL Injection", "PrivilegeEscalation", "Data Exfiltration")

tre_första = test_tuple[:3]
tre_sista = test_tuple[4:]
varannan = test_tuple[::2]

print(tre_första)
print(tre_sista)
print(varannan)