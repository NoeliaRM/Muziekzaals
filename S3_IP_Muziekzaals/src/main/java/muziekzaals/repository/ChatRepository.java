package muziekzaals.repository;

import java.util.ArrayList;

public interface ChatRepository {

    ArrayList<muziekzaals.model.Chat> getMessages(int messageID);

    boolean createChat(int ContactID, muziekzaals.model.Contact contact);
    boolean closeChat(int ContactID, muziekzaals.model.Contact contact);

}
