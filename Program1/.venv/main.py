from data.mahasiswa import DataMahasiswa
from view.input_form import display_menu, input_student_data
from view.mahasiswa import display_students

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        display_menu()
        choice = input().lower()
        if choice == 't':
            nim, nama, tugas, uts, uas = input_student_data()
            data_mahasiswa.tambah(nim, nama, tugas, uts, uas)
        elif choice == 'l':
            display_students(data_mahasiswa.tampilkan())
        elif choice == 'u':
            display_students(data_mahasiswa.tampilkan())
            nama = input("\nMasukkan nama mahasiswa yang akan diubah: ")
            nim, nama, tugas, uts, uas = input_student_data()
            data_mahasiswa.ubah(nim, nama, tugas, uts, uas)
        elif choice == 'h':
            display_students(data_mahasiswa.tampilkan())
            nama = input("\nMasukkan nama mahasiswa yang akan dihapus: ")
            data_mahasiswa.hapus(nama)
        elif choice == 'k':
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
