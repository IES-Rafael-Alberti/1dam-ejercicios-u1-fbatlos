#P24

cost=input("Dime cuanto vale en € (usa . para los centimos):")
sep=cost.split(".")
euro=sep[0]
cent=sep[1]
print(f"""Los euros son:{euro}€
Los centimos son: {cent} """)