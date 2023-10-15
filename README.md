# Chat Application { NOT COMPLETE YET }

## Overview

The Chat Application is a real-time messaging platform that provides users and businesses with a convenient way to communicate. It offers features like real-time chat, FAQs storage, quick assistance, and away messages. The application is designed to be embedded into websites, making it a valuable tool for businesses to engage with their customers.

![Chat Application Screenshot](screenshot.png)

## Features

- Real-time messaging using WebSockets.
- User authentication and secure messaging.
- FAQs storage for businesses to provide quick answers.
- Customizable chat widget for website integration.
- Away messages to inform users when agents are unavailable.
- Responsive and user-friendly interface.

## Tech Stack

- **Backend**: Quart (Python)
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **TUI (Textual)**: [Optional]
- **Database**: [SQL and MongoDB]
- **Deployment**: [Github]

## Installation

To run the Chat Application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/AchiraALX/final_project.git
   cd chat-application
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the application (e.g., database connection, environment variables).

5. Run the application:

   ```bash
   python server.py
   ```

6. Access the Chat Application in your web browser at `http://localhost:8000`.

## Configuration

You can customize the application's configuration by modifying the `config.py` file. Update the database connection settings, secret keys, and other configuration options as needed.

## Usage

- Sign in or create an account to start using the chat application.
- Businesses can manage FAQs and customize the chat widget in the admin panel.
- Users can chat with agents in real-time, receive quick assistance, and view FAQs.
- Use the away message feature to notify users when agents are not available.

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the [MIT License] License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please contact Jacob at [ed127720@students.mu.ac.ke].

---

**Note**: Customize the sections with information specific to your project. Include details about deployment, database choices, and any additional technologies or libraries you've used. Also, update the [LICENSE](LICENSE) file with the appropriate license information for your project.
