package ctrl;

import Service.Service;
import domain.Manager;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import repo.Repository;

public class LoginController {
    Stage stage;
    Repository repo = new Repository();
    Service service=new Service();
    Manager manager;
    @FXML
    TextField nume, ora, username;
    @FXML
    PasswordField password;

    @FXML
    public void initialize() {

    }

    public void loginHandler(ActionEvent actionEvent) {

        try {
            Manager m = service.cautaUser(username.getText(), password.getText());
            if (m != null) {
                this.manager = m;
                FXMLLoader loader = new FXMLLoader(getClass().getResource("../views/ManagerWindow.fxml"));
                Parent root = loader.load();
                ManagerController ctrl = loader.getController();
                ctrl.setStage(stage);
                ctrl.setService(service);
                ctrl.setManage("add");
                ctrl.setManager(manager);
                Scene scene = new Scene(root);
                stage.setScene(scene);
                stage.setTitle("Teatru Management System: Manage Shows");
                stage.show();
            }
            else{
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Error ");
                alert.setContentText("Invalid login!");
                alert.showAndWait();
            }


        } catch (Exception e) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error ");
            alert.setContentText("Error while starting app " + e);
            System.out.println(e);
            alert.showAndWait();
        }

    }

    public void setStage(Stage primaryStage) {
        this.stage=primaryStage;
    }
}
