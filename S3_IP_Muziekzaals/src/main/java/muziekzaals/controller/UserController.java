package muziekzaals.controller;


import muziekzaals.model.Admin;
import muziekzaals.model.Customer;
import muziekzaals.service.UserService;
import muziekzaals.model.User;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Optional;

@RestController
@CrossOrigin(origins = "*", allowedHeaders = "*")
public class UserController {

    private final UserService userService;
    public UserController(UserService userService)
    {
        this.userService = userService;
    }

    // Get all users
    @GetMapping @RequestMapping("/users")
    public ResponseEntity<List<User>> getAllUsers()
    {
        List<User> users = userService.getAllUsers();
        if(users != null) {
            return ResponseEntity.ok().body(users);
        } else {
            return ResponseEntity.notFound().build();
        }
    }
    @GetMapping @RequestMapping("/admins")
    public ResponseEntity<List<Admin>> getAllAdmins(@RequestParam(value = "userId")Optional <Long> userId)
    {
        List<Admin> admins = userService.getAllAdmins();
        if(admins != null) {
            return ResponseEntity.ok().body(admins);
        } else {
            return ResponseEntity.notFound().build();
        }
    }
    @GetMapping @RequestMapping("/customers")
    public ResponseEntity<List<Customer>> getAllCustomers(@RequestParam(value = "userId")Optional <Long> userId)
    {
        List<Customer> customers = userService.getAllCustomers();
        if(customers != null) {
            return ResponseEntity.ok().body(customers);
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}