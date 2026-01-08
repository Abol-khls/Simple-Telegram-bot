# Telegram Bot Example

This project is a simple Telegram bot written in Python. It demonstrates how to use the `python-telegram-bot` library to interact with users, respond to commands, and fetch live data from the web.

## Features
- **/start**: Greets the user.
- **/who_am_i**: Tells you your Telegram username.
- **/btc**: Fetches and displays the current Bitcoin price from CoinMarketCap.
- **/help**: Shows a help message.
- **Echo**: Replies with the same text you send (for any non-command message).

## How it works
- The bot uses `python-telegram-bot` for Telegram integration.
- It uses `requests`, `BeautifulSoup`, and `lxml` to scrape the Bitcoin price from CoinMarketCap.
- Logging is enabled for easier debugging and monitoring.

## Setup
1. **Clone this repository** or copy the code to your machine.
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r 1/requirements.txt
   ```
4. **Set your Telegram bot token** in the code (replace the placeholder in `main()` with your own token).
5. **Run the bot**:
   ```bash
   python 1.py
   ```

## Notes
- Make sure your bot token is kept private!
- This is a basic example for learning and experimentation. For production, consider handling errors and edge cases more robustly.
