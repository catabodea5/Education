package ctrl;

import Service.Service;
import domain.Loc;
import domain.Manager;
import domain.Spectacol;
import domain.Status;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

import java.util.ArrayList;
import java.util.List;

public class ManagerController {
    Stage stage;
    Service service=new Service();
    Manager manager;
    Spectacol spectacol;
    @FXML
    ListView spectacole;
    @FXML
    TableView locuri;
    @FXML
    TextField nume, ora;
    @FXML
    Button adauga, modifica, sterge;
    @FXML
    public void initialize() {
        List<Spectacol> s = service.getSpectacole();

        ObservableList<Spectacol> model = FXCollections.observableArrayList();
        model.setAll(s);
        spectacole.setItems(model);

        locuri.getSelectionModel().setSelectionMode(
                SelectionMode.MULTIPLE
        );
    }
    public void handleAdaugaSpectacol(ActionEvent actionEvent) {
        service.addSpectacol(new Spectacol(nume.getText(), ora.getText()));
        List<Spectacol> a = service.getSpectacole();

        ObservableList<Spectacol> model = FXCollections.observableArrayList();
        model.setAll(a);
        spectacole.setItems(model);

        locuri.getSelectionModel().setSelectionMode(
                SelectionMode.MULTIPLE
        );
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
        alert.setTitle("Good ");
        alert.setContentText("Operation successful!");
        alert.showAndWait();
    }

    public void handleModificare(ActionEvent actionEvent) {
        Spectacol s = (Spectacol) spectacole.getSelectionModel().getSelectedItem();
        service.modificareSpectacol(new Spectacol(s.getId(), nume.getText(), ora.getText()));
        List<Spectacol> a = service.getSpectacole();

        ObservableList<Spectacol> model = FXCollections.observableArrayList();
        model.setAll(a);
        spectacole.setItems(model);

        locuri.getSelectionModel().setSelectionMode(
                SelectionMode.MULTIPLE
        );
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
        alert.setTitle("Good ");
        alert.setContentText("Operation successful!");
        alert.showAndWait();
    }

    public void handleDeleteSpectacol(ActionEvent actionEvent) {
        Spectacol s = (Spectacol) spectacole.getSelectionModel().getSelectedItem();
        service.deleteSpectacol(s.getId());
        spectacole.getItems().remove(s);
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
        alert.setTitle("Good ");
        alert.setContentText("Operation successful!");
        alert.showAndWait();
    }

    public void setStage(Stage stage) {
        this.stage = stage;
    }



    public void setManage(String add) {
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }

    public void showHandler(MouseEvent mouseEvent) {
        Spectacol s = (Spectacol) spectacole.getSelectionModel().getSelectedItem();
        nume.setText(s.getNume());
        ora.setText(s.getOra());

        ObservableList<Loc> model = FXCollections.observableArrayList();
        List<Loc> locs = new ArrayList<>();
        for (Loc l : s.getLocuri()) {
            if (l.getStare() == Status.liber) {
                locs.add(l);
            }
        }
        model.setAll(locs);
        locuri.setItems(model);
    }

    public void setService(Service service) {
        this.service=service;
    }
}
