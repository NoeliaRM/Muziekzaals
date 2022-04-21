package muziekzaals.model;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Setter
@Getter
@Entity
@DiscriminatorValue("1")
@NoArgsConstructor
public class Admin extends User{
    public Admin(long userId, String username, String password, int userType) {
        super(userId, username, password, userType);
    }
}
