def get_book_text(path):
    with open(path, 'r') as file:
        return file.read()

def main():
    book_path = './books/frankenstein.txt'
    book_text = get_book_text(book_path)
    print(book_text)
    
if __name__ == "__main__":
    main()