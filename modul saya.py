def input_data():
    data_mahasiswa = []
    while True:
        nama = input("Masukkan Nama (atau ketik 'selesai' untuk mengakhiri): ")
        if nama.lower() == 'selesai':
            break
        nim = input("Masukkan NIM: ")
        semester = input("Masukkan Semester: ")
        data_mahasiswa.append((nama, nim, semester))
    return data_mahasiswa
def remove_duplicates(data):
    return list(set(data))
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write("Nama\tNIM\tSemester\n")
        for entry in data:
            file.write("\t".join(entry) + "\n")

if __name__ == "__main__":
    data_input = input_data()

    data_cleaned = remove_duplicates(data_input)

    save_to_file(data_cleaned, "data_mahasiswa.txt")
    print("Data berhasil disimpan tanpa duplikat.")