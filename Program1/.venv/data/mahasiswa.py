class Student:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.akhir = self.calculate_final_grade()

    def calculate_final_grade(self):
        return round((self.tugas * 0.3) + (self.uts * 0.35) + (self.uas * 0.35), 2)

class DataMahasiswa:
    def __init__(self):
        self.students = []

    def tambah(self, nim, nama, tugas, uts, uas):
        self.students.append(Student(nim, nama, tugas, uts, uas))

    def tampilkan(self):
        return self.students

    def hapus(self, nama):
        index = self.find_student_index(nama)
        if index is not None:
            del self.students[index]

    def ubah(self, nim, nama, tugas, uts, uas):
        index = self.find_student_index(nama)
        if index is not None:
            self.students[index] = Student(nim, nama, tugas, uts, uas)

    def find_student_index(self, nama):
        for index, student in enumerate(self.students):
            if student.nama == nama:
                return index
        return None
