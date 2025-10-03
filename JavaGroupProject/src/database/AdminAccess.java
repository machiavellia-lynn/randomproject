package database;

import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.scene.control.ButtonType;
import javafx.util.Pair;

import java.util.Optional;

public class AdminAccess {

    private static final String USERNAME = "admin";
    private static final String PASSWORD = "1234";

    public static boolean authenticate() {
        Dialog<Pair<String, String>> dialog = new Dialog<>();
        dialog.setTitle("Admin Login");

        Label userLabel = new Label("Username:");
        Label passLabel = new Label("Password:");
        TextField username = new TextField();
        PasswordField password = new PasswordField();

        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);
        grid.add(userLabel, 0, 0);
        grid.add(username, 1, 0);
        grid.add(passLabel, 0, 1);
        grid.add(password, 1, 1);

        dialog.getDialogPane().setContent(grid);
        dialog.getDialogPane().getButtonTypes().addAll(ButtonType.OK, ButtonType.CANCEL);

        dialog.setResultConverter(dialogButton -> {
            if (dialogButton == ButtonType.OK) {
                return new Pair<>(username.getText(), password.getText());
            }
            return null;
        });

        Optional<Pair<String, String>> result = dialog.showAndWait();
        return result.filter(credentials ->
                USERNAME.equals(credentials.getKey()) && PASSWORD.equals(credentials.getValue())
        ).isPresent();
    }
}
