def vypis_sklad(seznam):
    for polozka in seznam:
        print(f"Skladem: {polozka} -Aktualizováno v1.1")

if __name__ == "__main__":
    zbozi = ["Monitor", "Klávesnice", "Myš"]
    vypis_sklad(zbozi)
