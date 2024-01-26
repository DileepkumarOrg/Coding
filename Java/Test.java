class Super1 {
    void display() {
        System.out.println("Eating.....");
    }
}

class Nature extends Super1 { // Use 'extends' to inherit from Super1
    //@Override // Add @Override annotation to indicate method override
    void display() {
        System.out.println("Thinking.....");
    }
}

class Test {
    public static void main(String[] args) {
        Nature obj = new Nature();
        obj.display();
        // You cannot call 'super.display()' directly from obj; it's used in the context of method overriding.
        // If you want to call the superclass's method, you can do it as follows:
        // super1.display();
    }
}
