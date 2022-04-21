package muziekzaals;


import static org.junit.jupiter.api.Assertions.assertEquals;

import muziekzaals.model.Customer;
import muziekzaals.model.User;
import org.junit.jupiter.api.Test;

/**
 * Unit test for simple Dep.
 */
public class Test1

{
    /**
     * Tests if U.Hello(string name) adds "Hello " and "!" to a name
     */
    @Test
    public void TestHelloWithCorrectInputVariables()
    {
        // Arrange - Setup the code to be used
        Customer C = new Customer(10,"Noelia", "Noelia", 2);

        // Act - Execute the method to be tested
        String toCompare = C.hello("Noelia :)");
        
        // Assert - Check if the method postconditions is as expected
        assertEquals("Hello Noelia :)!", toCompare);
    }
}
