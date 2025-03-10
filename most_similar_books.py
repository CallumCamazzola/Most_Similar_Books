from recsys import similarity

# Do not change this function.  You must use this function.
def format_similar_message(source_book_title, 
                           most_similar_title, 
                           similarity_score):
    """Function to produce a properly formatted string for output most similar book."""
    result = f'People who liked {source_book_title}, ' + \
             f'also liked {most_similar_title}. (Score = {similarity_score:.3f})'
    return result


def book_scores():
    '''Function to read the user scores for each book and 
       stores them in a list of lists aswell as storing all the books in a seperate list'''
   
    number_of_books = 53
    scores = open("ratings.txt", "r")
    book = open("books.txt", "r")
    
    i=2
    book_scores = []
    books = []
    k=0
    
    #putting all the book titles in a list
    while k<number_of_books:
        book_line = book.readline()
        books.append(book_line)
        k=k+1
    
    line = scores.readline()
    i=1
    index = 1
    while line != '':
        # creating a while loop to initialize the book_scores list with the proper amount of values
        while i<= number_of_books+1:
            #skipping the first user: 0 line
            if i != 1:
                score_list = []
                score_list.append(int(line))
                book_scores.append(score_list)
            line = scores.readline()
            i=i+1
        
        # filtering out the User: line every 53 lines
        if i == 1+index*(number_of_books+1):
            index = index+1
            #reseting the book number after reading a new user
            book_number = 0
        else:
            #adding the score to the correct book 
            book_scores[book_number].append(int(line))
            book_number = book_number +1
          
        line = scores.readline()
        i = i+1

    
        
            
        

    scores.close()
    book.close()

    #creating a list to return both the book_scores and books
    books_return = [books,book_scores]
    return(books_return)


def similarity_score(book_scores,books):
    '''this function takes in the books and their
       coorosponding scores and finds the most similar 
       book to each one and then prints the information on an ouput file'''
    output= open("most-similar-books.txt", "w")
    i=0
    while i<(len(book_scores)):
        j=0
        highest_score = -1000
        #creating a nested loop so that each book and be compared to every other book
        while j<(len(book_scores)):
            #making sure a book isn't comapred against itself
            if j != i:
                sim_score=similarity(book_scores[i],book_scores[j])
                #setting highest similarity score and the corresponding book
                if sim_score > highest_score:
                    highest_score = sim_score
                    most_similar_book = books[j]
            j=j+1
        
        #getting the proper format for the line to be outputed 
        line = format_similar_message(books[i].strip() , most_similar_book.strip(), highest_score)
        output.write(line)
        output.write("\n")
        i=i+1


        







def main():
    """
    For each book in books.txt, this program outputs to the file 
    most-similar-books.txt the book and the book that is most similar 
    to it given the cosine similarity between it and all other books
    using the ratings in ratings.txt. This program does not prompt
    the user for any input. For more details, see the homework assignment.
    """
    book_return = book_scores()
    book_score = book_return[1]
    books = book_return[0]
    similarity_score(book_score,books)



if __name__ == "__main__":
    main()




