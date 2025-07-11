import math

def hitung_mol(massa, mr):
    try:
        return massa / mr
    except ZeroDivisionError:
        return None

def setarakan_reaksi(mol_a, mol_b):
    try:
        rasio = mol_a / mol_b
        if math.isclose(rasio, 1, rel_tol=0.01):
            return "Reaksi setara: A + B → Produk"
        elif rasio > 1:
            return f"Reaksi setara: {round(rasio)}A + B → Produk"
        else:
            return f"Reaksi setara: A + {round(1/rasio)}B → Produk"
    except ZeroDivisionError:
        return "Mol reaktan B tidak boleh nol"

def hitung_konsentrasi(massa_mg, volume_ml):
    try:
        return (massa_mg / volume_ml) * 1000
    except ZeroDivisionError:
        return None

def hitung_kadar_logam(konsentrasi_mg_L, faktor_pengencer):
    try:
        return konsentrasi_mg_L * faktor_pengencer
    except TypeError:
        return None

# Contoh penggunaan
if __name__ == "__main__":
    # Massa molar
    massa = float(input("Masukkan massa (gram): "))
    mr = float(input("Masukkan Mr: "))
    mol = hitung_mol(massa, mr)
    print(f"Mol = {mol:.4f} mol")

    # Persamaan reaksi
    mol_a = float(input("Masukkan mol reaktan A: "))
    mol_b = float(input("Masukkan mol reaktan B: "))
    reaksi = setarakan_reaksi(mol_a, mol_b)
    print(reaksi)

    # Konsentrasi
    massa_zat = float(input("Masukkan massa zat (mg): "))
    volume_larutan = float(input("Masukkan volume larutan (mL): "))
    kons = hitung_konsentrasi(massa_zat, volume_larutan)
    print(f"Konsentrasi = {kons:.2f} mg/L")

    # Kadar logam
    kons_terukur = float(input("Masukkan konsentrasi terukur (mg/L): "))
    faktor = float(input("Masukkan faktor pengenceran: "))
    kadar = hitung_kadar_logam(kons_terukur, faktor)
    print(f"Kadar logam = {kadar:.2f} mg/L")
