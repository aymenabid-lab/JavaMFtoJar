# J2ME MIDlet Compiler
---
> Dr. Aymen ABID- Master Professionnel en Ingénierie des Systèmes Embarqués - ESPIN - 2025/2026
---

## Overview
A web-based tool for compiling Java ME (J2ME) MIDlet applications into JAR files. This application provides a simple interface to upload Java source files and MANIFEST.MF files, compile them with J2ME libraries, and download the resulting JAR file for testing on J2ME emulators.

## Purpose
This tool simplifies the J2ME development workflow by providing:
- Easy compilation of MIDlet source code
- Automatic JAR packaging with proper manifest integration
- Real-time compilation logs and error reporting
- Direct JAR file download for testing

## Current State
The application is fully functional and ready to use. Users can:
1. Upload a .java source file and MANIFEST.MF file
2. Compile the MIDlet with MIDP 2.0 and CLDC 1.1 libraries
3. View detailed compilation logs
4. Download the compiled JAR file

## Project Architecture

### Backend (Flask)
- **app.py**: Main Flask application with endpoints for:
  - `/` - Serves the web interface
  - `/compile` - Handles file upload and compilation
  - `/download/<filename>` - Serves compiled JAR files

### Frontend
- **templates/index.html**: Single-page application with:
  - File upload interface
  - Real-time compilation status
  - Log viewer with syntax highlighting
  - Download functionality

### J2ME Libraries
- **lib/cldcapi11.jar**: CLDC 1.1 API (Connected Limited Device Configuration)
- **lib/midpapi20.jar**: MIDP 2.0 API (Mobile Information Device Profile)

### Directory Structure
```
.
├── app.py                 # Flask backend
├── templates/
│   └── index.html        # Web interface
├── lib/                  # J2ME libraries
│   ├── cldcapi11.jar
│   └── midpapi20.jar
├── src/                  # Example source files
├── uploads/              # Temporary upload storage
├── compiled/             # Generated JAR files
└── attached_assets/      # User-provided example files
    ├── MyFirstMIDlet_1761503916337.java
    └── MANIFEST_1761503916337.MF
```

## Dependencies

### System
- Java Development Kit (GraalVM 22.3)
- Python 3.11

### Python Packages
- Flask 3.1.2
- Werkzeug 3.1.3

### J2ME Libraries
- MicroEmulator CLDC 1.1 API (2.0.4)
- MicroEmulator MIDP 2.0 API (2.0.4)

### Bytecode Manipulation
- ASM 9.7 (for bytecode version downgrade)

## Recent Changes (October 26, 2025)
- Initial project setup
- Installed Java and Python development environments
- Downloaded J2ME libraries from Maven Central (CLDC 1.1 + MIDP 2.0)
- Downloaded ASM library for bytecode manipulation
- Created BytecodeDowngrader utility to convert Java 21 bytecode to Java 1.3
- Created Flask backend with file upload, compilation, and JAR generation endpoints
- Implemented 3-stage compilation pipeline: compile → downgrade → package
- Built responsive web interface with real-time feedback and detailed logs
- Tested compilation with provided MyFirstMIDlet example
- Verified bytecode downgrade (version 63 → 47) for J2ME compatibility
- Configured workflow to run on port 5000

## Usage Instructions

### For Users
1. Open the web interface
2. Select your .java source file
3. Select your MANIFEST.MF file
4. Click "Compile MIDlet"
5. View the compilation logs
6. Download the generated JAR file
7. Test the JAR on a J2ME emulator (e.g., MicroEmulator, KEmulator)

### For Developers
The compilation process uses:
```bash
javac -classpath lib/cldcapi11.jar:lib/midpapi20.jar <source>.java
jar cvfm <output>.jar MANIFEST.MF -C <work_dir> <class>.class
```

## Testing the Example
The provided example files (MyFirstMIDlet.java and MANIFEST.MF) demonstrate a simple J2ME application with:
- Display initialization
- Form UI with commands
- Command listener implementation
- Message display functionality

## Technical Notes
- Compilation uses modern Java 21 but bytecode is downgraded to Java 1.3 (version 47) for J2ME compatibility
- Bytecode downgrade is performed using ASM library to ensure emulator compatibility
- JAR files are fully compatible with J2ME emulators (CLDC 1.1 / MIDP 2.0)
- Temporary files are cleaned up after compilation
- Maximum upload size: 16MB
- Each compilation creates a unique working directory to avoid conflicts

## Compilation Pipeline
1. **Compile**: Java source compiled with modern Java using J2ME libraries (CLDC 1.1 + MIDP 2.0)
2. **Downgrade**: Bytecode version changed from 63 (Java 19) to 47 (Java 1.3) using ASM
3. **Package**: JAR created with downgraded classes and MANIFEST.MF
4. **Verify**: Output is J2ME-compatible and ready for emulator testing

## Future Enhancements
- In-browser J2ME emulator integration
- Multi-file MIDlet project support
- Code editor with syntax highlighting
- JAD (Java Application Descriptor) file generation
- Template library for common J2ME patterns
- Support for additional J2ME APIs (JSR-75, etc.)
