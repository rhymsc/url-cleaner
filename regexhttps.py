import re

def tambahkan_http(url):
    # Definisikan pola regex untuk mencocokkan URL yang sudah memiliki protokol atau tidak
    pattern = re.compile(r'^(https?://)?(.+)$')

    # Temukan hasil cocok dengan pola regex
    match = pattern.match(url)

    # Jika URL sudah memiliki protokol, biarkan URL tidak berubah
    if match and match.group(1):
        return url
    else:
        # Tambahkan "https://" jika protokol tidak ada
        return f"https://{url}"

def baca_file_dan_tambahkan(input_file):
    try:
        with open("resulthttps.txt", 'w') as output_file:
            for line in open(input_file, 'r'):
                url = line.strip()  # Hilangkan karakter whitespace seperti newline
                hasil = tambahkan_http(url)
                output_line = f"{hasil}/"
                print(output_line)
                output_file.write(output_line + "\n")

    except FileNotFoundError:
        print(f"File '{input_file}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Meminta input dari pengguna
input_file_path = input("Masukkan path file input: ")

# Contoh penggunaan
baca_file_dan_tambahkan(input_file_path)
