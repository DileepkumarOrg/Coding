import java.awt.*;

public class Gui {

    public static void main(String[] args) {
        Frame frame = new Frame("Hello");
        frame.setSize(400, 400);
        frame.setLayout(null);
        
        Button button = new Button("Next");
        button.setBounds(100, 100, 100, 40); // specify button location and size
        
        frame.add(button);
        frame.setVisible(true); // use correct method name for visibility
    }
}
