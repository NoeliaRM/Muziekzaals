package muziekzaals.model;


public class Message extends Chat {

    private int MessageId; //to identify each message

    public Message(int MessageId, User U, Zaal Acc) {
        super(MessageId, U, Acc);
    }
}
