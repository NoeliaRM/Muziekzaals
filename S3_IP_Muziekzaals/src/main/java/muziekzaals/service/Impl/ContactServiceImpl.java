package muziekzaals.service.Impl;

import muziekzaals.model.Zaal;
import muziekzaals.model.Contact;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

@Service
@Primary
@RequiredArgsConstructor
public class ContactServiceImpl implements muziekzaals.service.ContactService {

    /*private final ContactRepository contactRepository;*/

    @Override
    public ArrayList<Contact> getContactbyUsername(String Username) {
        return null;
    }

    @Override
    public ArrayList<Contact> getContactbyId(int ContactId) {
        return null;
    }

    @Override
    public boolean addContact(Contact contact) {
        return false;
    }

    @Override
    public boolean deleteContact(int contactID, Zaal account) {
        ArrayList<Contact> contacts = getAllOfAUsersContacts(account);
        for (Contact c : contacts) {
            if (c.getContactId() == contactID) {
                return false;
            }
        }
        return false;
    }

    @Override
    public ArrayList<Contact> getAllOfAUsersContacts(Zaal account) {
        return null;
    }

    //ADMIN gets every account as a Contact



}
