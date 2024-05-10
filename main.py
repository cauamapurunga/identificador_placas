import matplotlib.pyplot as plt

def identificar_estado(placa):
    estados = {
        "Ceará": [
            ("HTX", "HZA"), ("NQL", "NRE"), ("NUM", "NVF"),
            ("OCB", "OCU"), ("OHX", "OIQ"), ("ORN", "OSV"),
            ("OZA", "OZA"), ("PMA", "POZ"), ("RIA", "RIN"),
            ("SAN", "SBV")
        ],
        "Maranhão": [
            ("HOL", "HQE"), ("NHA", "NHT"), ("NMP", "NNI"),
            ("NWS", "NXQ"), ("OIR", "OJQ"), ("OXQ", "OXZ"),
            ("PSA", "PTZ"), ("ROA", "ROZ")
        ],
        "Piauí": [
            ("LVF", "LWQ"), ("NHU", "NIX"), ("ODU", "OEI"),
            ("OUA", "OUE"), ("OVW", "OVY"), ("PIA", "PIZ"),
            ("QRN", "QRZ"), ("RSG", "RST")
        ]
    }
    
    for estado, intervalo in estados.items():
        for inicio, fim in intervalo:
            if inicio <= placa[:3] <= fim:
                return estado
            
    return "Desconhecido"

contagem_estados = {estado: 0 for estado in ["Ceará", "Maranhão", "Piauí", "Desconhecido"]}

while True:
    placa = input("Digite a placa do veículo (ou 'parar' para encerrar): ")
    if placa.lower() == "parar":
        print("Encerrando o programa...")
        break
    estado_identificado = identificar_estado(placa.upper())
    print(f"A placa {placa} pertence a {estado_identificado}")
    contagem_estados[estado_identificado] += 1

print("\nContagem de placas por estado:")
for estado, contagem in contagem_estados.items():
    print(f"{estado}: {contagem}")

labels = contagem_estados.keys()
sizes = contagem_estados.values()
colors = ['#0072BD', '#4DBEEE', '#6A5ACD', '#B0C4DE']
plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'white'})
plt.title("Contagem de placas por estado", fontsize=16, fontweight='bold', color='navy')
plt.axis('equal')  

for i, (label, size) in enumerate(zip(labels, sizes)):
    plt.text(1.3, 0.7 - i*0.1, f"{label}: {size}", horizontalalignment='left', verticalalignment='center', fontsize=12, color='black')

plt.show()
