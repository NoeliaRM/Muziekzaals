package muziekzaals.model;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.DiscriminatorValue;
import javax.persistence.Entity;

@Setter
@Getter

@Entity
@DiscriminatorValue("2")

@NoArgsConstructor
public class Customer extends User{
    public Customer(long userId, String username, String password, int userType) {
        super(userId, username, password, userType);
    }
}
