package database;

import model.Book;
import java.util.ArrayList;
import java.util.List;

public class BookDatabase {
    public static List<Book> getInitialBooks() {
        List<Book> books = new ArrayList<>();
        books.add(new Book(10001, "Welcome to Dead House", "Horror", "R.L. Stine", true));
        books.add(new Book(10002, "Stay Out of the Basement", "Horror", "R.L. Stine", true));
        books.add(new Book(10003, "The Haunted Mask", "Horror", "R.L. Stine", true));
        books.add(new Book(10004, "Night of the Living Dummy", "Horror", "R.L. Stine", true));
        books.add(new Book(10005, "The Werewolf of Fever Swamp", "Horror", "R.L. Stine", true));
        books.add(new Book(10006, "Harry Potter and the Chamber of Secrets", "Fantasy", "J.K. Rowling", true));
        books.add(new Book(10007, "Harry Potter and the Prisoner of Azkaban", "Fantasy", "J.K. Rowling", true));
        books.add(new Book(10008, "Harry Potter and the Goblet of Fire", "Fantasy", "J.K. Rowling", true));
        books.add(new Book(10009, "Harry Potter and the Order of the Phoenix", "Fantasy", "J.K. Rowling", true));
        books.add(new Book(10010, "Harry Potter and the Half-Blood Prince", "Fantasy", "J.K. Rowling", true));
        books.add(new Book(10011, "The Lion, the Witch and the Wardrobe", "Fantasy", "C.S. Lewis", true));
        books.add(new Book(10012, "Prince Caspian", "Fantasy", "C.S. Lewis", true));
        books.add(new Book(10013, "The Voyage of the Dawn Treader", "Fantasy", "C.S. Lewis", true));
        books.add(new Book(10014, "The Silver Chair", "Fantasy", "C.S. Lewis", true));
        books.add(new Book(10015, "The Horse and His Boy", "Fantasy", "C.S. Lewis", true));
        books.add(new Book(10016, "The Little Mermaid", "Fantasy", "Disney", true));
        books.add(new Book(10017, "Beauty and the Beast", "Fantasy", "Disney", true));
        books.add(new Book(10018, "Aladdin", "Fantasy", "Disney", true));
        books.add(new Book(10019, "The Lion King", "Fantasy", "Disney", true));
        books.add(new Book(10020, "Cinderella", "Fantasy", "Disney", true));
        books.add(new Book(10021, "The Great Gatsby", "Classic", "F. Scott Fitzgerald", true));
        books.add(new Book(10022, "1984", "Dystopian", "George Orwell", true));
        books.add(new Book(10023, "To Kill a Mockingbird", "Classic", "Harper Lee", true));
        books.add(new Book(10024, "Pride and Prejudice", "Romance", "Jane Austen", true));
        books.add(new Book(10025, "The Catcher in the Rye", "Classic", "J.D. Salinger", true));
        books.add(new Book(10026, "The Hobbit", "Fantasy", "J.R.R. Tolkien", true));
        books.add(new Book(10027, "The Lord of the Rings", "Fantasy", "J.R.R. Tolkien", true));
        books.add(new Book(10028, "Harry Potter and the Sorcerer's Stone", "Fantasy", "J.K. Rowling", true));
        books.add(new Book(10029, "The Alchemist", "Fiction", "Paulo Coelho", true));
        books.add(new Book(10030, "The Da Vinci Code", "Thriller", "Dan Brown", true));
        books.add(new Book(10031, "The Hunger Games", "Dystopian", "Suzanne Collins", true));
        books.add(new Book(10032, "The Girl on the Train", "Thriller", "Paula Hawkins", true));
        books.add(new Book(10033, "The Shining", "Horror", "Stephen King", true));
        books.add(new Book(10034, "A Game of Thrones", "Fantasy", "George R.R. Martin", true));
        books.add(new Book(10035, "Moby-Dick", "Adventure", "Herman Melville", true));
        books.add(new Book(10036, "Brave New World", "Dystopian", "Aldous Huxley", true));
        books.add(new Book(10037, "Frankenstein", "Gothic", "Mary Shelley", true));
        books.add(new Book(10038, "Crime and Punishment", "Psychological Fiction", "Fyodor Dostoevsky", true));
        books.add(new Book(10039, "The Picture of Dorian Gray", "Philosophical Fiction", "Oscar Wilde", true));
        books.add(new Book(10040, "War and Peace", "Historical Fiction", "Leo Tolstoy", true));
        books.add(new Book(10041, "The Odyssey", "Epic Poetry", "Homer", true));
        books.add(new Book(10042, "The Kite Runner", "Drama", "Khaled Hosseini", true));
        books.add(new Book(10043, "Catch-22", "Satire", "Joseph Heller", true));
        books.add(new Book(10044, "Beloved", "Historical Fiction", "Toni Morrison", true));
        books.add(new Book(10045, "The Book Thief", "Historical Fiction", "Markus Zusak", true));
        books.add(new Book(10046, "The Chronicles of Narnia", "Fantasy", "C.S. Lewis", true));
        books.add(new Book(10047, "Little Women", "Classic", "Louisa May Alcott", true));
        books.add(new Book(10048, "Wuthering Heights", "Gothic Fiction", "Emily Brontë", true));
        books.add(new Book(10049, "Don Quixote", "Classic", "Miguel de Cervantes", true));
        books.add(new Book(10050, "Dracula", "Horror", "Bram Stoker", true));
        books.add(new Book(10051, "The Secret Garden", "Classic", "Frances Hodgson Burnett", true));
        books.add(new Book(10052, "Anne of Green Gables", "Classic", "Lucy Maud Montgomery", true));
        books.add(new Book(10053, "The Outsiders", "Young Adult", "S.E. Hinton", true));
        books.add(new Book(10054, "The Grapes of Wrath", "Historical Fiction", "John Steinbeck", true));
        books.add(new Book(10055, "Slaughterhouse-Five", "Science Fiction", "Kurt Vonnegut", true));
        books.add(new Book(10056, "Lord of the Flies", "Allegorical Novel", "William Golding", true));
        books.add(new Book(10057, "The Handmaid's Tale", "Dystopian", "Margaret Atwood", true));
        books.add(new Book(10058, "The Fault in Our Stars", "Romance", "John Green", true));
        books.add(new Book(10059, "The Road", "Post-apocalyptic", "Cormac McCarthy", true));
        books.add(new Book(10060, "Shogun", "Historical Fiction", "James Clavell", true));
        books.add(new Book(10061, "The Count of Monte Cristo", "Adventure", "Alexandre Dumas", true));
        books.add(new Book(10062, "The Secret Life of Bees", "Drama", "Sue Monk Kidd", true));
        books.add(new Book(10063, "Sapiens: A Brief History of Humankind", "Non-fiction", "Yuval Noah Harari", true));
        books.add(new Book(10064, "The Seven Habits of Highly Effective People", "Self-help", "Stephen R. Covey", true));
        books.add(new Book(10065, "Educated", "Memoir", "Tara Westover", true));
    
        
        return books;
    }
}
