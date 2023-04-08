import os
import PyPDF2

# nazwa pliku pdf
print("Podaj nazwe pliku")
filename = input()

# uzyskaj ścieżkę do katalogu, w którym znajduje się skrypt Python
script_dir = os.path.dirname(os.path.abspath(__file__))
print("podaj litere dysku do przeszukania")
disk = input().upper()
disk += ":\\"
for root, dirs, files in os.walk("D:\\"):
    if filename in files:
        pdf_path = os.path.join(root, filename)
        print(f"Znaleziono plik {filename} w ścieżce: {pdf_path}")
        break
else:
    print(f"Plik {filename} nie został znaleziony.")
# Otwórz plik PDF

pdf_file = open(pdf_path, 'rb')

# Wczytaj plik PDF do obiektu PyPDF2
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Inicjuj zmienną do zliczania słów
total_words = 0

# Przetwórz każdą stronę w dokumencie
for page_num in range(len(pdf_reader.pages)):
    # Pobierz tekst z aktualnej strony
    page_obj = pdf_reader.pages[page_num]
    page_text = page_obj.extract_text()

    # Zlicz liczbę słów na stronie i dodaj do ogólnej liczby słów
    page_words = len(page_text.split())
    total_words += page_words

# Zamknij plik PDF
pdf_file.close()

# Wyświetl liczbę słów
print("Liczba słów w pliku:", total_words)
