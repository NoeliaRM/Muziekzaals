package muziekzaals.controller;

import muziekzaals.service.ContactService;
import muziekzaals.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

@RestController
@RequestMapping("/contact")
@RequiredArgsConstructor
@CrossOrigin(origins = "*", allowedHeaders = "*")
public class ContactController {

    private final ContactService contactService;
    private final UserService userService;
}
