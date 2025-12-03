def celcius_ke_fahrenheit(celcius):
    """
    Mengkonversi suhu dari skala Celcius ke skala Fahrenheit.

    Rumus konversi adalah: Fahrenheit = (Celcius * 9/5) + 32
    """
    # Menghitung konversi
    fahrenheit = (celcius * 9/5) + 32
    
    # Mengembalikan nilai Fahrenheit
    return fahrenheit

# --- Contoh Penggunaan ---
# Menguji fungsi dengan nilai-nilai yang diberikan:
print(f"0 Celcius = {celcius_ke_fahrenheit(0)} Fahrenheit")
print(f"100 Celcius = {celcius_ke_fahrenheit(100)} Fahrenheit")

# Contoh tambahan
print(f"25 Celcius = {celcius_ke_fahrenheit(25)} Fahrenheit")