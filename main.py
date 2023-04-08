import os
import PyPDF2

# nazwa pliku pdf
filename = "Adam Baranczyk_Wokol pojęcia kreatywności i twórczości.pdf"

# uzyskaj ścieżkę do katalogu, w którym znajduje się skrypt Python
script_dir = os.path.dirname(os.path.abspath(__file__))

# uzyskaj pełną ścieżkę do pliku pdf
pdf_path = os.path.join(script_dir, filename)
print(pdf_path)
# Otwórz plik PDF
pdf_file = open(pdf_path, 'rb')
#
# # Wczytaj plik PDF do obiektu PyPDF2
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#
# # Inicjuj zmienną do zliczania słów
# total_words = 0
#
# # Przetwórz każdą stronę w dokumencie
# for page_num in range(pdf_reader.getNumPages()):
#     # Pobierz tekst z aktualnej strony
#     page_obj = pdf_reader.getPage(page_num)
#     page_text = page_obj.extractText()
#
#     # Zlicz liczbę słów na stronie i dodaj do ogólnej liczby słów
#     page_words = len(page_text.split())
#     total_words += page_words
#
# # Zamknij plik PDF
# pdf_file.close()
#
# # Wyświetl liczbę słów
# print("Liczba słów w pliku:", total_words)