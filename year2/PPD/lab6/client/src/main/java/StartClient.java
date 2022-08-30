import model.Vanzare;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import services.ServicesInterface;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
public class StartClient {
    private final static Random random = new Random();
    private final static int max_loc = 100;
    private final static int seconds = 2;
    public static void main(String[] args) throws InterruptedException, IOException {
        ApplicationContext factory = new ClassPathXmlApplicationContext("classpath:config.xml");
        ServicesInterface server = (ServicesInterface) factory.getBean("Service");
        System.out.println("S-a obtinut o referinta catre un server remote");
        FileWriter myWriter = new FileWriter("client/src/main/rezultate.txt");
        while(server.shouldContinue()) {
            Thread.sleep(seconds);
            Vanzare vanzare = getVanzareRandom();
            String rezultat = server.addVanzare(vanzare);
            myWriter.write(rezultat + " " + "\n");
        }

        server.clientDone();
        myWriter.close();
    }

    private static Vanzare getVanzareRandom() {
        List<Integer> locuri_vandute = new ArrayList<>();
        int nr_bilete = random.nextInt(max_loc);
        for(int i=0; i < nr_bilete; i++) {
            int loc = random.nextInt(max_loc);
            while (locuri_vandute.contains(loc))
                loc = random.nextInt(max_loc);
            locuri_vandute.add(loc);
        }

        Vanzare vanzare = new Vanzare();
        vanzare.setId_spectacol(1);
        vanzare.setData_vanzare(LocalDate.now());
        vanzare.setNr_bilete(nr_bilete);
        vanzare.setLocuri_vandute(locuri_vandute);
        return vanzare;
    }
}