import org.objectweb.asm.*;
import java.io.*;
import java.nio.file.*;

public class BytecodeDowngrader {
    
    public static void downgradeClass(String inputPath, String outputPath) throws IOException {
        byte[] classBytes = Files.readAllBytes(Paths.get(inputPath));
        ClassReader reader = new ClassReader(classBytes);
        ClassWriter writer = new ClassWriter(ClassWriter.COMPUTE_MAXS);
        
        ClassVisitor versionChanger = new ClassVisitor(Opcodes.ASM9, writer) {
            @Override
            public void visit(int version, int access, String name, 
                            String signature, String superName, String[] interfaces) {
                super.visit(Opcodes.V1_3, access, name, signature, superName, interfaces);
            }
        };
        
        reader.accept(versionChanger, ClassReader.SKIP_FRAMES);
        Files.write(Paths.get(outputPath), writer.toByteArray());
    }
    
    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java BytecodeDowngrader <input.class> <output.class>");
            System.exit(1);
        }
        
        try {
            downgradeClass(args[0], args[1]);
            System.out.println("Successfully downgraded bytecode to Java 1.3 (version 47)");
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
            System.exit(1);
        }
    }
}
