package app;

import javafx.stage.Stage;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.collections.transformation.FilteredList;
import javafx.collections.transformation.SortedList;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.geometry.*;

import model.Book;
import database.BookDatabase;
import database.AdminAccess;

public class MainApp extends Application {

    private TableView<Book> tableView;
    private ObservableList<Book> bookList;

    @Override
    public void start(Stage stage) {
        if (!AdminAccess.authenticate()) {
            Alert alert = new Alert(Alert.AlertType.ERROR, "Access Denied", ButtonType.CLOSE);
            alert.showAndWait();
            Platform.exit();
            return;
        }

        VBox root = new VBox(10);
        root.setPadding(new Insets(15));

        tableView = new TableView<>();
        bookList = FXCollections.observableArrayList(BookDatabase.getInitialBooks());

        FilteredList<Book> filteredData = new FilteredList<>(bookList, b -> true);
        SortedList<Book> sortedData = new SortedList<>(filteredData);
        sortedData.comparatorProperty().bind(tableView.comparatorProperty());

        TextField searchField = new TextField();
        searchField.setPromptText("Search by title or author...");
        Button searchBtn = new Button("Search");

        HBox searchBox = new HBox(10, searchField, searchBtn);
        searchBox.setAlignment(Pos.CENTER_LEFT);

        searchBtn.setOnAction(e -> {
            String query = searchField.getText().toLowerCase().trim();
            filteredData.setPredicate(book -> {
                if (query.isEmpty()) return true;
                return book.getTitle().toLowerCase().contains(query) ||
                       book.getAuthor().toLowerCase().contains(query) ||
                       book.getGenre().toLowerCase().contains(query) ||
                       String.valueOf(book.getId()).contains(query);
            });
        });

        tableView.setItems(sortedData);
        tableView.getColumns().addAll(
            createColumn("Book Code", book -> String.valueOf(book.getId())),
            createColumn("Title", Book::getTitle),
            createColumn("Author", Book::getAuthor),
            createColumn("Genre", Book::getGenre),
            createColumn("Available", book -> book.isAvailable() ? "Yes" : "No")
        );

        tableView.setColumnResizePolicy(TableView.CONSTRAINED_RESIZE_POLICY);

        Button manageBtn = new Button("Manage Books");
        manageBtn.setOnAction(e -> showManageBooksWindow());      
        
        Button exitBtn = new Button("Exit");
        exitBtn.setOnAction(e -> Platform.exit());

        HBox buttonBox = new HBox(10, manageBtn, exitBtn);
        buttonBox.setAlignment(Pos.CENTER_RIGHT);

        root.getChildren().addAll(searchBox, tableView, buttonBox);

        stage.setScene(new Scene(root, 1100, 700));
        stage.setTitle("Book Management System");
        stage.show();
    }

    private TableColumn<Book, String> createColumn(String title, javafx.util.Callback<Book, String> mapper) {
        TableColumn<Book, String> col = new TableColumn<>(title);
        col.setCellValueFactory(data -> new javafx.beans.property.SimpleStringProperty(mapper.call(data.getValue())));
        return col;
    }

    private void showManageBooksWindow() {
        Stage manageStage = new Stage();
        manageStage.setTitle("Manage Books");

        TableView<Book> manageTable = new TableView<>(bookList);
        manageTable.getColumns().addAll(
            createColumn("Book Code", book -> String.valueOf(book.getId())),
            createColumn("Title", Book::getTitle),
            createColumn("Author", Book::getAuthor),
            createColumn("Genre", Book::getGenre),
            createColumn("Available", book -> book.isAvailable() ? "Yes" : "No")
        );
        manageTable.setColumnResizePolicy(TableView.CONSTRAINED_RESIZE_POLICY);

        
        TextField idField = new TextField();
        idField.setPromptText("Code");

        TextField titleField = new TextField();
        titleField.setPromptText("Title");

        TextField authorField = new TextField();
        authorField.setPromptText("Author");

        TextField genreField = new TextField();
        genreField.setPromptText("Genre");

        CheckBox availableBox = new CheckBox("Available");
        availableBox.setSelected(true);

        HBox inputBox = new HBox(10, idField, titleField, authorField, genreField, availableBox);
        inputBox.setPadding(new Insets(10));
        inputBox.setAlignment(Pos.CENTER);

        Button addBtn = new Button("Add Book");
        Button removeBtn = new Button("Remove Selected");

        addBtn.setOnAction(e -> {
            String idText = idField.getText().trim();
            String title = titleField.getText().trim();
            String author = authorField.getText().trim();
            String genre = genreField.getText().trim();
            boolean available = availableBox.isSelected();

            if (idText.isEmpty() || title.isEmpty() || author.isEmpty() || genre.isEmpty()) {
                Alert alert = new Alert(Alert.AlertType.WARNING, "All fields must be filled.");
                alert.showAndWait();
                return;
            }

            try {
                long id = Long.parseLong(idText);
                bookList.add(new Book(id, title, genre, author, available));
                idField.clear();
                titleField.clear();
                authorField.clear();
                genreField.clear();
                availableBox.setSelected(true);
            } catch (NumberFormatException ex) {
                Alert alert = new Alert(Alert.AlertType.ERROR, "Invalid Book Code (must be a number).");
                alert.showAndWait();
            }
        });

        removeBtn.setOnAction(e -> {
            Book selected = manageTable.getSelectionModel().getSelectedItem();
            if (selected != null) {
                bookList.remove(selected);
            }
        });

        HBox manageButtons = new HBox(10, addBtn, removeBtn);
        manageButtons.setAlignment(Pos.CENTER_RIGHT);
        manageButtons.setPadding(new Insets(10));

        VBox layout = new VBox(10, manageTable, inputBox, manageButtons);
        layout.setPadding(new Insets(10));

        manageStage.setScene(new Scene(layout, 900, 600));
        manageStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
