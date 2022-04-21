package muziekzaals.service;

import muziekzaals.model.Admin;
import muziekzaals.model.Customer;
import muziekzaals.model.User;

import java.util.List;

public interface UserService {

    List<User>getAllUsers();
    List<Admin>getAllAdmins();
    List<Customer>getAllCustomers();
}