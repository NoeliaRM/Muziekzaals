package muziekzaals.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.RequiredArgsConstructor;


import java.util.ArrayList;

@Data
@Builder
@AllArgsConstructor
@RequiredArgsConstructor
public class Zaal {
    private int zaalId; //ID of my account (automatically generated)
    private User U; //me
    private ArrayList<User> usersInZaal; //for admin will be allUsers, for customer addedUsers
    private Chat C;
    public Zaal(int accountId, String accountName) {
    }
    public Zaal(int accountId, String accountName, Chat C, ArrayList<User> usersInZaal) {
    }
}
