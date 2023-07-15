import whois

domain = input("target:")
whois_consult = whois.whois(domain)

print(whois_consult.text)