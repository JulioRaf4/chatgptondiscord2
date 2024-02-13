# Discord Bot with GPT Chat API Tutorial

## Introduction

This tutorial will guide you through the process of creating a Discord bot that utilizes the OpenAI GPT Chat API. The provided code in `main.py` allows your bot to respond to messages in a specified channel using the GPT-3.5 Turbo model. Before you begin, make sure you have the required tokens and dependencies.

## Prerequisites

1. Discord Bot Token: [Create a Discord bot](https://discordpy.readthedocs.io/en/latest/discord.html) and obtain the bot token. Tutorial to [get bot token](https://www.youtube.com/watch?v=mcsbmv7mZus&ab_channel=HowToTech).
2. OpenAI API Key: [Sign up](https://beta.openai.com/signup/) for the OpenAI API and get your API key. Tutorial to [api key](https://www.youtube.com/watch?v=nafDyRsVnXU&ab_channel=TutorialsHub).
3. Python Dependencies: Install required Python packages using `pip install -r requirements.txt`.

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/JulioRaf4/chatgptondiscord2
   cd chatgptondiscord2

   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your Discord bot token, OpenAI API key, and the desired channel ID:
   ```env
   DISCORD_BOT_TOKEN="your_discord_bot_token_here"
   OPENAI_API_KEY="your_openai_api_key_here"
   CHANNEL_ID="your_discord_channel_id_here"
   ```

## Running the Bot

Execute the bot using the following command:

```bash
python main.py
```

Your Discord bot should now be active and responding in the specified channel.

## Usage

1. Invite your bot to your Discord server.
2. In the specified channel (as defined in `CHANNEL_ID`), mention your bot and start chatting.

**Note:** Ensure that your bot has the necessary permissions and is added to the correct channel.

## Customization

Feel free to modify the code to suit your specific needs. You can experiment with different GPT-3.5 Turbo parameters, add more features, or enhance the functionality according to your preferences.

## Conclusion

Congratulations! You have successfully created a Discord bot using the OpenAI GPT Chat API. If you encounter any issues or want to explore further, refer to the [Discord.py documentation](https://discordpy.readthedocs.io/) and [OpenAI API documentation](https://beta.openai.com/docs/).

Happy coding!
