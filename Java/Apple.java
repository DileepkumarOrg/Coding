interface New {
    void display();

    void copy();

    void paste();
}

class Apple implements New {
    public void copy() {
        System.out.println("Copy code");
    }

    public void paste() {
        System.out.println("Paste code");
    }

    public void display() {
        System.out.println("Display code");
    }

    

public static void main(String[] args) {
    Apple obj = new Apple();
    obj.copy();
    obj.paste();
    obj.display();
    }