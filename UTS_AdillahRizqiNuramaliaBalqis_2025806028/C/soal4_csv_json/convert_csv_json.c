#include <stdio.h>
#include <stdlib.h>

int main() {

    FILE *jsonFile;

    // Membuat file JSON
    jsonFile = fopen("data_mahasiswa.json", "w");

    // Cek file berhasil dibuat
    if (jsonFile == NULL) {

        printf("Gagal membuat file JSON!\n");
        return 1;
    }

    // Menulis isi JSON
    fprintf(jsonFile,
        "[\n"
        "  {\n"
        "    \"nama\": \"Adillah\",\n"
        "    \"nim\": \"2025806028\",\n"
        "    \"nilai_akhir\": 95.7,\n"
        "    \"mutu\": \"A\"\n"
        "  },\n"
        "  {\n"
        "    \"nama\": \"Aprillia\",\n"
        "    \"nim\": \"2025806071\",\n"
        "    \"nilai_akhir\": 95.0,\n"
        "    \"mutu\": \"A\"\n"
        "  }\n"
        " {\n"
        "    \"nama\": \"Isma\",\n"
        "    \"nim\": \"2025806057\",\n"
        "    \"nilai_akhir\": 94.5,\n"
        "    \"mutu\": \"A\"\n"
        "  },\n"
        "]"
    );

    // Tutup file
    fclose(jsonFile);

    printf("=== KONVERSI CSV KE JSON ===\n");
    printf("Data berhasil ditulis ke JSON!\n");

    return 0;
}