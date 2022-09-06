package Service;

import domain.Manager;
import domain.Spectacol;
import repo.Repository;

import java.util.List;

public class Service {
    Repository repo= new Repository();

    public Manager cautaUser(String text, String text1) {
        Manager m = repo.cauta(text, text1);
        return m;
    }

    public List<Spectacol> getSpectacole() {
        return repo.getSpectacole();
    }

    public void addSpectacol(Spectacol spectacol) {
        repo.addSpectacol(spectacol);
    }

    public void modificareSpectacol(Spectacol spectacol) {
        repo.update(spectacol);
    }

    public void deleteSpectacol(int id) {
        repo.deleteSpectacol(id);
    }
}
