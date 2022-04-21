package muziekzaals.service.Impl;

import muziekzaals.model.Chat;
import muziekzaals.model.User;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

@Service
@Primary
@RequiredArgsConstructor
public class ChatServiceImpl implements muziekzaals.service.ChatService {

   /* private final ChatRepository responseRepository;
    private final ZaalService accountService;*/


    @Override
    public ArrayList<Chat> getChat(int contactID) {
        return null;
    }

    @Override
    public boolean createChat(int contactID, Chat chat, User user) {
        return false;
    }

    @Override
    public boolean closeChat(int contactID, Chat chat, User user) {
        return false;
    }

    @Override
    public ArrayList<Chat> getAllOfAUsersChats(User user) {
        return null;
    }
}
