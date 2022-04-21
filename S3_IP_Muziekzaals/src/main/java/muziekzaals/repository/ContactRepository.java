package muziekzaals.repository;

import muziekzaals.model.Contact;

import java.util.ArrayList;

public interface ContactRepository {


    ArrayList<Contact> getContact(String contactName);

    boolean createContact(Contact contact);

    boolean deleteContact(int ContactId);


}
