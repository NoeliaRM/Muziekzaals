package muziekzaals.service.Impl;

import muziekzaals.model.Zaal;
import muziekzaals.model.User;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

@Service
@Primary
@RequiredArgsConstructor
public class ZaalServiceImpl implements muziekzaals.service.ZaalService {

    @Override
    public ArrayList<Zaal> getZaalById(int accountId) {
        return null;
    }

    @Override
    public boolean createZaal(Zaal acc) {
        return false;
    }

    @Override
    public boolean closeZaal(int accID, User user) {
        return false;
    }
}
