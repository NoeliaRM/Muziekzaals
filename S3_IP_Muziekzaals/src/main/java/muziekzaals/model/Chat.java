package muziekzaals.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

@Data
@Builder
@AllArgsConstructor
public class Chat {

    private int id; //message Id
    private User U; //me
    private Zaal Acc; //user in my contact list with who i wanna talk

}
