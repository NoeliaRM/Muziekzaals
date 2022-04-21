package muziekzaals.service;

import muziekzaals.model.Zaal;
import muziekzaals.model.Contact;

import java.util.ArrayList;

public interface ContactService {

    ArrayList<Contact> getContactbyUsername(String Username);
    ArrayList<Contact> getContactbyId(int ContactId);

    boolean addContact( Contact contact);

    boolean deleteContact( int contactID, Zaal account);

    //ADMIN gets every account as a Contact
    ArrayList<Contact> getAllOfAUsersContacts(Zaal account);
}
