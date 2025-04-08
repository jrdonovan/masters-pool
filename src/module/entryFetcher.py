import datetime
import gspread
from typing import List
from src.module.entry import Entry

class EntryFetcher:
    def __init__(self, creds_file: str, sheet_name: str):
        self.gc = gspread.service_account(filename=creds_file)
        self.sheet = self.gc.open(sheet_name).sheet1

    def get_entries(self) -> List[Entry]:
        rows = self.sheet.get_all_records()
        entries = []
        for row in rows:
            timestamp_dt = datetime.datetime.strptime(row.get("Timestamp"), "%m/%d/%Y %H:%M:%S")
            players = {k:v for k,v in row.items() if k in {'BSDs', 'Tuna Fishies', 'Sleepers', 'Happy Bois'}} # TODO: Make this more robust
            entry = Entry(
                timestamp_dt,
                row.get("Email Address"),
                row.get("Entry Name"),
                players,
                row.get("Total Combined Strokes of Winner")
            )
            entries.append(entry)
            print(f"Entry fetched: {entry}")
        return entries
