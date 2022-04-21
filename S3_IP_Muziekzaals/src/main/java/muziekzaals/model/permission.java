package muziekzaals.model;

import lombok.*;
import javax.persistence.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name="permission")

public class permission {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "permission_id")
    protected long permissionId;

    @Column(name = "permission_description")
    protected String permissionDescription;
}
