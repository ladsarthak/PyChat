# PyChat
PyChat is my first Chatbot series, with each version varying in its complexities and capabilities. Some versions also include secret modes.

Each version of PyChat adds usability, flexibility, or safety features. The progression moves from a simple, command-based chatbot to a more robust, user-trainable, and modular conversational agent, with PyChat 3.0 introducing persistent learning and PyChat 4.0 focusing on structure and caution. The pairs.json file is central to PyChat 3.0’s learning capability.

Here’s a concise summary of the features and evolution of each PyChat version based on the code and data files in your workspace:

**PyChat 1.0**  
This is the foundational version of the chatbot. It offers basic conversational abilities, including telling jokes, sharing fun facts, providing the user's current location, drawing simple graphics (using the `sketchpy` library), and setting timers. The code includes input correction for common user command variations, making it more user-friendly. The chatbot responds to a set of predefined commands and aims to be interactive and entertaining.

**PyChat 2.0**  
Building on 1.0, this version significantly expands input correction, handling a much wider range of user command typos and phrasings. The core features—jokes, fun facts, location, drawing, and timers—remain, but the user experience is improved through more robust command recognition. This makes the chatbot more forgiving and accessible to users who may not type commands exactly as expected.

**PyChat 3.0**  
This version marks a shift to a more flexible, data-driven approach. It uses the NLTK library’s `Chat` class and loads conversational pairs from an external pairs.json file, allowing for easier expansion and customization of responses. Users can train the bot with new input-response pairs, and the bot can save and load user names. There’s also basic math question recognition and a simple mechanism for learning new responses, making the chatbot more adaptive and interactive.

**PyChat 3.0 Directory - pairs.json**  
This JSON file is created while using PyChat 3.0. It stores user-defined input-response pairs, enabling persistent learning across sessions. It is directly linked to PyChat 3.0, supporting its customizable and extensible conversation model.

**PyChat 4.0 (Secret Mode embedded)**  
The latest version introduces a more modular structure, with separate functions for jokes and facts, and a warning about potential destructive actions if mishandled. The chatbot retains all previous features but is designed for greater extensibility and caution. The code hints at advanced capabilities and a more serious approach to user interaction, including error handling for keyboard interruptions.
