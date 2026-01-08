# Telegram Bot Example

This project is a simple Telegram bot written in Python. It demonstrates how to use the `python-telegram-bot` library to interact with users, respond to commands, and fetch live data from the web.

## Features
- **/start**: Greets the user.
- **/who_am_i**: Tells you your Telegram username.
- **/price <coin-name>**: Fetches and displays the current price for any cryptocurrency from CoinMarketCap. Example: `/price bitcoin` or `/price solana`.
- **/help**: Shows a help message.
- **Echo**: Replies with the same text you send (for any non-command message).

## How it works
- The bot uses `python-telegram-bot` for Telegram integration.
- It uses `requests`, `BeautifulSoup`, and `lxml` to scrape cryptocurrency prices from CoinMarketCap.
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
   pip install -r requirements.txt
   ```
4. **Set your Telegram bot token** in the code (replace the placeholder in `main()` with your own token).
5. **Run the bot**:
   ```bash
   python 1.py
   ```

## Notes
- Make sure your bot token is kept private!
- This is a basic example for learning and experimentation. For production, consider handling errors and edge cases more robustly.

## Usage Example

- To get the price of Bitcoin:
   `/price bitcoin`
- To get the price of Solana:
   `/price solana`

If you enter an invalid coin name or the coin is not found, the bot will let you know.
