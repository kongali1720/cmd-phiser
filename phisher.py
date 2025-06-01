import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
╔═══════════════════════════════════════════════╗
║     🎣 CMD-PHISHER - SIMULASI PHISHING       ║
║       Edukasi Aman. Tidak Mengandung Bahaya  ║
╚═══════════════════════════════════════════════╝
""")

def fake_login_page():
    print("\n📄 Simulasi Halaman Login Palsu\n")
    print("=======================================")
    print("          LOGIN FACEBOOK FAKE          ")
    print("=======================================\n")
    username = input("📧 Email atau Nomor HP: ")
    password = input("🔑 Kata Sandi           : ")

    print("\n📡 Mengirim data...")
    time.sleep(2)

    print(f"\n[!] SIMULASI: Data tersimpan.")
    print(f"    Email/No HP : {username}")
    print(f"    Kata Sandi  : {password}")
    print("\n✅ Jangan khawatir! Ini cuma simulasi offline.\n")
    input("Tekan Enter untuk kembali ke menu...")

def edukasi():
    clear()
    print("""
📚 Edukasi Singkat: Apa itu Phishing?

Phishing adalah teknik serangan siber di mana pelaku
membuat halaman palsu (mirip aslinya) untuk mencuri
data pengguna seperti username dan password.

💡 Tips Aman:
✔ Selalu cek URL situs login
✔ Jangan asal klik link dari email/SMS
✔ Aktifkan 2FA untuk perlindungan ekstra
✔ Jangan pernah masukkan data penting di halaman mencurigakan

Ingat: cmd-phisher ini 100% offline & buat edukasi! 🛡️
""")
    input("\nTekan Enter untuk kembali ke menu...")

def menu():
    while True:
        clear()
        banner()
        print("1. Jalankan Simulasi Phishing")
        print("2. Edukasi Tentang Phishing")
        print("3. Keluar")
        pilihan = input("\n>> Pilih opsi (1-3): ")

        if pilihan == '1':
            clear()
            fake_login_page()
        elif pilihan == '2':
            edukasi()
        elif pilihan == '3':
            print("\nTerima kasih sudah belajar dengan aman! 🙏")
            break
        else:
            print("\n[!] Pilihan tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    menu()
