#  check if user input is digit
# print("Ingiza pesa za Kitanzania")
# tz_sh = input("> ")
# if tz_sh.isdigit():
#     usd_crc = float(tz_sh) / 2500
#     print(f'Tsh {tz_sh} ni sawa sawa na USD {usd_crc}')
# else:
#     print("Tafadhali ingiza tarakimu kwa usahihi")

# Default value
try:
    print("Ingiza mwaka wako wa kuzaliwa.")
    birth_day = int(input("> ")) or "0"
    current_year = 2025
    age = current_year - birth_day
    print(f"Una jumla ya miaka {age}")
except ValueError:
    print("Invalid input data!")