import org.junit.Assert;
import org.junit.Test;

import java.io.File;

public class TestWebidl {


    private static File gfile =  new File("../webidl/WebIDL.g4");

    @Test
    public void test(){
        Assert.assertTrue(GrammarTester.run(gfile));
    }

}
