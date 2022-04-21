package muziekzaals.model;

import lombok.*;
import javax.persistence.*;


@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name="user_")
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name="user_type_fk", discriminatorType = DiscriminatorType.INTEGER)

public class User {
    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    @Column(name="user_id")
    private long userId;

    @Column(name="user_username")
    private String username;

    @Column(name="user_password")
    private String password;

    @Column(name="user_type_fk", columnDefinition = "longtext",insertable = false, updatable = false)
    private int userType;

    public User(String username, String password, int userType){
        this.username = username;
        this.password = password;
        this.userType = userType;
    }

public String hello(String s) {
        return "Hello" + " " + username + " :)!" ;
    }
}
