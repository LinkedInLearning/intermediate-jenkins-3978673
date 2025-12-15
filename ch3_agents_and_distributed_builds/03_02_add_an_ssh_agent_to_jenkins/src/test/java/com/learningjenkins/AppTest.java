package com.learningjenkins;

// Changed import from org.junit.Assert.assertEquals to org.junit.jupiter.api.Assertions.assertEquals
import static org.junit.jupiter.api.Assertions.assertEquals;

// Changed import from org.junit.Test to org.junit.jupiter.api.Test
import org.junit.jupiter.api.Test;

/**
 * Unit test for simple App.
 */
public class AppTest
{
    // The @Test annotation is now from the junit.jupiter package
    @Test
    void checkHelloWorld() // Changed to void and generally better to use camelCase for test names
    {
        App app = new App();
        // The assertEquals method is now from the Assertions class
        assertEquals( "Hello World!", app.main() );
    }
}
