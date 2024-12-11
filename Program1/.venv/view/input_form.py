class tampilkan_menu:
    def display_menu():
        print("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]: ", end=' ')

class masukan_dataMahasiswa:
    def input_student_data():
        nim = input("\nNIM: ")
        nama = input("Nama: ")
        tugas = int(input("Nilai Tugas: "))
        uts = int(input("Nilai UTS: "))
        uas = int(input("Nilai UAS: "))
        return nim, nama, tugas, uts, uas
