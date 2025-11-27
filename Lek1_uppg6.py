log = "2025-11-13 12:55:21 - LOGIN FAILED - user = root"

datum = log[:10]
status = log[22:34]
username = log[44:]

print(datum)
print(status)
print(username)
print(log[::-1])
#print(username,status,datum)