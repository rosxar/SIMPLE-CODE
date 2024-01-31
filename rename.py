import os

def rename_files_in_folders(main_directory):
    # Masuk ke direktori utama
    os.chdir(main_directory)

    # Ambil daftar semua folder di direktori utama
    folders = [folder for folder in os.listdir() if os.path.isdir(folder)]

    # Untuk setiap folder dalam folders
    for folder in folders:
        # Masuk ke folder
        os.chdir(folder)
        
        # Ambil daftar semua file di dalam folder
        files = [file for file in os.listdir() if os.path.isfile(file)]

        # Jika files tidak kosong
        if files:
            # Untuk setiap file dalam files
            for i, file in enumerate(files, start=1):
                # Buat nama baru untuk file (nama_folder_jumlah_file.ext)
                new_name = f"{folder}_{i}{os.path.splitext(file)[1]}"

                # Ubah nama file menjadi nama baru
                os.rename(file, new_name)
                print(f"File {file} telah diubah menjadi {new_name}")

        # Keluar dari folder
        os.chdir('..')

# Ganti 'path/to/main_directory' dengan path aktual ke direktori utama
main_directory = 'D:\\Bisnis\\downloaded_images'
rename_files_in_folders(main_directory)
