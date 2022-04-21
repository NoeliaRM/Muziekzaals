package muziekzaals.controller;

import muziekzaals.service.ZaalService;
import muziekzaals.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/account")
@RequiredArgsConstructor
@CrossOrigin(origins = "*", allowedHeaders = "*")
public class ZaalControl {

    private final ZaalService zaalService;
    private final UserService userService;





}
