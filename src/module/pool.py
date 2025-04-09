from collections import OrderedDict
import datetime
from dataclasses import dataclass, field
import pandas as pd
from typing import List, Dict

from src.module.entry import Entry


@dataclass
class Pool:
    """
    Represents a pool for a golf tournament.
    Attributes:
        _name (str): The name of the pool.
        _entries (List[Entry]): A list of entries in the pool.
    """

    _name: str
    _entries: List[Entry] = field(default_factory=list)

    @property
    def name(self) -> str:
        return self._name

    @property
    def entries(self) -> List[Entry]:
        return self._entries

    @entries.setter
    def entries(self, value: List[Entry]) -> None:
        if not isinstance(value, list):
            raise ValueError("Entries must be a list.")
        self._entries = value

    def initialize_entries(self, rows: List[Dict[str, int | float | str]]) -> None:
        """
        Initializes the entries for the pool from the provided rows.
        Args:
            rows (List[Dict[str, int | float | str]]): A list of dictionaries representing the entries.
        """
        entries = []
        for row in rows:
            timestamp_dt = datetime.datetime.strptime(
                row.get("Timestamp"), "%m/%d/%Y %H:%M:%S"
            )
            players = {
                k: list(map(lambda x: x.strip(), v.split(",")))
                for k, v in row.items()
                if k in {"BSDs", "Tuna Fishies", "Sleepers", "Happy Bois"}
            }  # TODO: Make this more robust
            d = OrderedDict()
            for category, player in players.items():
                if category == "Sleepers":
                    d["Sleeper"] = player[0]
                elif category == "Happy Bois":
                    d["Happy Boi"] = player[0]
                elif category == "BSDs":
                    d["BSD 1"] = player[0]
                    d["BSD 2"] = player[1]
                elif category == "Tuna Fishies":
                    d["Tuna Fish 1"] = player[0]
                    d["Tuna Fish 2"] = player[1]
            entry = Entry(
                timestamp_dt,
                row.get("Email Address"),
                row.get("Entry Name"),
                d,
                row.get("Total Combined Strokes of Winner"),
            )
            entries.append(entry)
        self.entries = entries

    def to_dataframe(self) -> pd.DataFrame:
        df = pd.DataFrame([e.to_dict() for e in self.entries])
        df.index += 1
        return df
