import subprocess
import sys

def install_poetry():
    """Instala Poetry si no está disponible."""
    try:
        subprocess.run(["poetry", "--version"], check=True)
        print("✅ Poetry ya está instalado.")
    except FileNotFoundError:
        print("⚙️ Instalando Poetry...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--user", "poetry"], check=True)
        print("✅ Poetry instalado correctamente.")

def install_dependencies():
    """Instala las dependencias del proyecto."""
    print("⚙️ Instalando dependencias con Poetry...")
    subprocess.run(["poetry", "install"], check=True)
    print("✅ Todas las dependencias han sido instaladas.")

def main():
    install_poetry()
    install_dependencies()
    subprocess.run(["poetry", "run", "python", "spamdetector/code/model.py"])
    print("\n🚀 Instalación completa.")

if __name__ == "__main__":
    main()
