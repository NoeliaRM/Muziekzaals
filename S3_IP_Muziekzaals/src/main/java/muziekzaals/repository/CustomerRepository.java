package muziekzaals.repository;

import muziekzaals.model.Customer;
import muziekzaals.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;


public interface CustomerRepository extends JpaRepository<Customer, Long>{
     List<Customer> findByUserIdIsLike(int userId);
}
