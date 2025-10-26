import javax.microedition.midlet.*;
import javax.microedition.lcdui.*;

public class MyFirstMIDlet extends MIDlet implements CommandListener {

    private Display display;
    private Form form;
    private Command exitCommand;
    private Command showMsgCommand;
    private StringItem msgItem;

    public MyFirstMIDlet() {
        display = Display.getDisplay(this);
        form = new Form("Bienvenue J2ME");

        // Commandes
        exitCommand = new Command("Quitter", Command.EXIT, 1);
        showMsgCommand = new Command("Afficher message", Command.SCREEN, 1);

        // Item pour afficher un message
        msgItem = new StringItem("Message : ", "");
        form.append(msgItem);

        form.addCommand(exitCommand);
        form.addCommand(showMsgCommand);
        form.setCommandListener(this);
    }

    public void startApp() {
        display.setCurrent(form);
    }

    public void pauseApp() {}

    public void destroyApp(boolean unconditional) {}

    public void commandAction(Command c, Displayable d) {
        if (c == exitCommand) {
            destroyApp(true);
            notifyDestroyed();
        } else if (c == showMsgCommand) {
            msgItem.setText("Bonjour, MIDlet exécutée avec succès !");
        }
    }
}

