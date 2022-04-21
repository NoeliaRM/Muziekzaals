package muziekzaals.controller;

import muziekzaals.service.ChatService;
import muziekzaals.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/response")
@RequiredArgsConstructor
@CrossOrigin(origins = "*", allowedHeaders = "*")
public class ChatController {

    private final ChatService chatService;
    private final UserService userService;

}
