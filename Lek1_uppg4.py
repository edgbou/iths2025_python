target_ip = "10.5.20.234"
open_ports = [22, 80, 44]
vulnerable = True

print("The target IP is",target_ip)
print(type(target_ip))
print("\n")

print("The open ports on the network are", open_ports)
print(type(open_ports))
print("\n")

print("Vulnerable Network:", vulnerable)
print(type(vulnerable))