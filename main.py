import requests
import schedule
import time
import asyncio

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1360247632764731442/t1SxokkWvuyTxNgNJDIhTczIloIYFWvzuOxFfs-akHx2fN3cBY03aoXVNvvaPG4tgyOv"  # Byt till din riktiga webhook

async def send_poll():
    """ Skickar omröstningen via en Discord-webhook. """
    poll_text = (
        "**Hoppas ni har haft en fin vecka! Nu blickar vi framåt.**\n"
        "**Vilket av dessa ämnen vill ni lära er om på måndag?**\n"
        "⏪ Reversing\n"
        "#️⃣ Crypto\n"
        "💡 Hardware\n"
        "🌐 Web\n"
        "⛏️ Pwn\n"
        "🔍 Forensics"


       "                                                       "
    "obs:*För att kunna rösta, så måste du reagera med en emoji*"  
    
    
    
    )  

    payload = {
        "content": poll_text,
        "username": "CTF-Bot",  # valfritt visningsnamn
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code in [200, 204]:
            print("✅ Omröstning skickades via webhook.")
        else:
            print(f"❌ Fel vid skickning: {response.status_code} – {response.text}")
    except Exception as e:
        print(f"⚠️ Undantag vid skickning: {e}")

def schedule_poll():

    schedule.every().friday.at("15:57").do(lambda: asyncio.create_task(send_poll()))

async def main():
    schedule_poll()
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())