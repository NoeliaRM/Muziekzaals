package muziekzaals.service.Impl;

import muziekzaals.model.Customer;
import muziekzaals.model.User;
import muziekzaals.model.Admin;
import muziekzaals.repository.AdminRepository;
import muziekzaals.repository.CustomerRepository;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@Primary
public class UserServiceImpl implements muziekzaals.service.UserService {

    private final AdminRepository adminRep;
    private final CustomerRepository customerRep;

    public UserServiceImpl(AdminRepository adminRep, CustomerRepository customerRep){
        this.adminRep = adminRep;
        this.customerRep = customerRep;
    }

    public List<User> getAllUsers() {
        List<User> result = new ArrayList<>();
        result.addAll(adminRep.findAll());
        result.addAll(customerRep.findAll());
        return result;
    }

    @Override
    public List<Admin> getAllAdmins() {
        List<Admin> result = new ArrayList<>();
        result.addAll(adminRep.findAll());
        return result;
    }

    @Override
    public List<Customer> getAllCustomers() {
        List<Customer> result = new ArrayList<>();
        result.addAll(customerRep.findAll());
        return result;
    }
}
