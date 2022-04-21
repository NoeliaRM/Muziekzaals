package muziekzaals.repository;

import muziekzaals.model.Admin;
import muziekzaals.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
@Repository
public interface AdminRepository extends JpaRepository<Admin, Long> {
    List<Admin> findByUserIdIsLike(long userId);
}