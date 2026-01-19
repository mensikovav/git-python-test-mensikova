def vypis_sklad(seznam):
    for polozka in seznam:
        print(f"Skladem: {polozka} (Verze 1.0)")

if __name__ == "__main__":
    zbozi = ["Monitor", "Klávesnice", "Myš"]
    vypis_sklad(zbozi)
