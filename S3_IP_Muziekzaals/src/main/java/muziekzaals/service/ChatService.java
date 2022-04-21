package muziekzaals.service;

import muziekzaals.model.User;

import java.util.ArrayList;

public interface ChatService {

    ArrayList<muziekzaals.model.Chat> getChat(int contactID);

    boolean createChat(int contactID, muziekzaals.model.Chat chat, User user);

    boolean closeChat( int contactID, muziekzaals.model.Chat chat, User user);

    public ArrayList<muziekzaals.model.Chat> getAllOfAUsersChats(User user);
}
