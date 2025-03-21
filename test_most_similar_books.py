from most_similar_books import main
import os

def test_most_similar_books_main():
    correct_file = open("most-similar-books-correct-answer.txt", "r")

    main() # when main runs, it writes out most-similar-books.txt
    actual_output_filename = "most-similar-books.txt"
    actual_file = open(actual_output_filename, "r")

    correct_line = correct_file.readline()
    actual_line = actual_file.readline()
    while correct_line != "":
        assert correct_line == actual_line
        correct_line = correct_file.readline()
        actual_line = actual_file.readline()         

    correct_file.close()
    actual_file.close()
    os.remove( actual_output_filename )
   
