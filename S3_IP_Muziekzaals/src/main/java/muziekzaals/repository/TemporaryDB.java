package muziekzaals.repository;

import muziekzaals.model.*;
import java.util.ArrayList;
import java.util.List;

public class TemporaryDB {

    public final List<User> userList = new ArrayList<>();
    public ArrayList<Contact> reviews;
    public ArrayList<Zaal> accounts;
    public ArrayList<Chat> responses;

    public TemporaryDB()
    {
        //USERS DATA
        userList.add(new Admin(14,"A", "A", 1));
        userList.add(new Customer(12,"C1", "C1", 2));
        userList.add(new Customer(15, "C2", "C2", 2));
        userList.add(new Admin(34,"B", "B", 3));
    }
}
