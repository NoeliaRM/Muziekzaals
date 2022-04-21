package muziekzaals.model;

import lombok.*;

@Data
@Builder
@AllArgsConstructor
//@NoArgsConstructor
@RequiredArgsConstructor

public class Contact
{
    private int ContactId; //autoassigned Id for each one of my contacts ((Maybe not useful?¿))
    private Zaal Acc; //I need the Nickname of the account add someone to my contacts

}
