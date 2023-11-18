import re

def pisahkan_host_domain(url):
    pattern = re.compile(r'(https?://www\.|http://www\.|https?://|http://)?([a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})+(\.[a-zA-Z0-9]{2,})?)')
    match = pattern.search(url)

    if match:
        host_domain = match.group(2)
        return host_domain
    else:
        return None

def baca_file_dan_pisahkan():
    try:
        banner = r"""
______ _   ___   ____  ___ _____ _____ 
| ___ \ | | \ \ / /  \/  |/  ___/  __ \
| |_/ / |_| |\ V /| .  . |\ `--.| /  \/
|    /|  _  | \ / | |\/| | `--. \ |    
| |\ \| | | | | | | |  | |/\__/ / \__/\
\_| \_\_| |_/ \_/ \_|  |_/\____/ \____/ 
        """
        print(banner)
        file_path = input("Masukkan path file: ")

        # Memasukkan nama file output
        output_file = "hasil.txt"

        print(f"\nPath File: {file_path}\n")

        with open(file_path, 'r') as file, open(output_file, 'w') as output:
            for line in file:
                url = line.strip()  # Hilangkan karakter whitespace seperti newline
                hasil = pisahkan_host_domain(url)
                if hasil:
                    output_line = f"{hasil}\n"
                    print(output_line, end='')

                    # Add the print statement for the modified URL here
                    subdomain = "subdomain"  # Replace this with your desired subdomain
                    host = "host"  # Replace this with your desired host
                    print(f"https://{subdomain + host + '.' + match.group(3)}/")

                    output.write(output_line)
                else:
                    print(f"{url}")
    except FileNotFoundError:
        print(f"File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
baca_file_dan_pisahkan()
