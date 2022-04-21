package muziekzaals.service;

import muziekzaals.model.Zaal;
import muziekzaals.model.User;

import java.util.ArrayList;

public interface ZaalService {

    ArrayList<Zaal> getZaalById(int accountId);

    boolean createZaal(Zaal acc);


    boolean closeZaal( int accID, User user);
}
