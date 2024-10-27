import os
import subprocess

# Lista de ferramentas para instalar
tools = [
    'git',
    'nmap',
    'sqlmap',
    'metasploit-framework',
    'john',
    'hydra',
    'wireshark',
    'burpsuite',
    'gobuster',
    'python3',
    'cyberchef',  # Pode precisar ser instalado via npm ou manualmente
    'metapicz',   # Para metadados, instalação manual ou via apt, se disponível
    'metadata2go', # Para metadados, instalação manual ou via apt, se disponível
    'fastthread',  # Java Thread Dump Analyzer
    'audacity',   # Editor de áudio
]

def install_tools():
    print("Você já está quase lá rei da colina...")
    subprocess.run(['sudo', 'apt', 'update'], check=True)
    subprocess.run(['sudo', 'apt', 'upgrade', '-y'], check=True)

    for tool in tools:
        print(f"Instalando {tool}...")
        subprocess.run(['sudo', 'apt', 'install', '-y', tool], check=True)

    print("Você já está pronto para jogar os CTF's mais radicais! mas lembre de ler a documentação das ferramentas que for usar...")

def main():
    try:
        install_tools()
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
